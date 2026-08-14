#!/usr/bin/env python3
"""
Export a DAS Markdown file (with embedded Mermaid diagrams) to PDF.

Pipeline (two mature, independent tools, no bundled CDN dependency):
1. Render every ```mermaid code block in the input .md to SVG using `mmdc`
   (@mermaid-js/mermaid-cli) in a single pass — one browser launch handles
   all diagrams via mmdc's native Markdown mode, and mmdc itself writes a
   temporary copy of the markdown with the mermaid fences replaced by image
   references to the rendered SVGs.
2. Convert that temporary markdown to PDF using `md-to-pdf`.

Both tools run on a local headless Chrome/Chromium. If a system Chrome/Edge
install is found, it is reused (via Puppeteer's `executablePath`) to avoid
downloading a private ~300MB Chromium copy. If none is found, Puppeteer
falls back to its own managed Chromium (downloaded on first use).

Performance note: this script prefers globally-installed `mmdc`/`md-to-pdf`
binaries and only falls back to `npx` (which re-resolves the dependency tree
on every call — slow, especially on constrained networks) if they aren't
found on PATH. Run this once for fast, repeatable exports:

    npm install -g @mermaid-js/mermaid-cli md-to-pdf

Usage:
    # Basic: writes DAS-foo.pdf next to DAS-foo.md
    python das_to_pdf.py .specs/das/DAS-foo.md

    # Custom output path
    python das_to_pdf.py .specs/das/DAS-foo.md --output out/DAS-foo.pdf

    # Keep the temporary working directory (diagrams + intermediate .md)
    python das_to_pdf.py .specs/das/DAS-foo.md --keep-temp

    # Force a specific browser executable instead of auto-detecting one
    python das_to_pdf.py .specs/das/DAS-foo.md --chrome-path "C:\\path\\to\\chrome.exe"

Requirements:
    - Node.js >= 18 on PATH.
    - `mmdc` and `md-to-pdf` installed globally (recommended, see above) or
      npm/npx on PATH as a fallback.
    - Internet access is only needed the first time `npx` fetches a package
      that isn't installed globally (or if no local Chrome/Edge is found and
      Puppeteer must download one).
    - See ../references/pdf-export.md for details and troubleshooting.
"""

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Optional, Tuple

MERMAID_PATTERN = re.compile(r'```mermaid\s*\n(.*?)```', re.DOTALL | re.MULTILINE)

MMDC_PACKAGE = "@mermaid-js/mermaid-cli"
MD_TO_PDF_PACKAGE = "md-to-pdf"

# Common install locations for a system browser, checked in order.
CHROME_CANDIDATES = {
    "Windows": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ],
    "Darwin": [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ],
    "Linux": [
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/usr/bin/microsoft-edge",
    ],
}

CHROME_WHICH_NAMES = [
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
    "microsoft-edge", "msedge",
]


def find_chrome() -> Optional[str]:
    """Best-effort detection of a local Chrome/Edge/Chromium executable."""
    for name in CHROME_WHICH_NAMES:
        found = shutil.which(name)
        if found:
            return found

    for path_str in CHROME_CANDIDATES.get(platform.system(), []):
        path = Path(path_str)
        if path.is_file():
            return str(path)

    return None


def npx_env(skip_chromium_download: bool) -> dict:
    """
    Environment for npx-spawned subprocesses. When we already have a local
    Chrome/Edge to reuse via `executablePath`, we skip Puppeteer's own
    Chromium download entirely — that download happens at *install* time
    (i.e. the first time `npx` fetches `mmdc`/`md-to-pdf`), independent of
    the runtime `executablePath` override, and is by far the slowest part
    of a first run (~300MB) if left enabled unnecessarily.
    """
    env = os.environ.copy()
    if skip_chromium_download:
        env["PUPPETEER_SKIP_DOWNLOAD"] = "true"
        env["PUPPETEER_SKIP_CHROMIUM_DOWNLOAD"] = "true"  # older Puppeteer versions
    return env


def run_cmd(cmd: List[str], **kwargs) -> subprocess.CompletedProcess:
    """
    Run a command that may resolve to a .cmd/.bat shim on Windows (npx,
    mmdc, md-to-pdf are all npm-installed shims there). subprocess cannot
    exec .cmd files directly without a shell, so we route through cmd.exe
    on Windows and use argv lists directly everywhere else.
    """
    if platform.system() == "Windows":
        return subprocess.run(subprocess.list2cmdline(cmd), shell=True, **kwargs)
    return subprocess.run(cmd, **kwargs)


def check_node_available() -> bool:
    """Node.js itself is always required; npx is only needed as a fallback
    when mmdc/md-to-pdf aren't installed globally (see resolve_tool_command)."""
    return shutil.which("node") is not None


def resolve_tool_command(bin_name: str, package: str) -> Tuple[List[str], bool]:
    """
    Prefer a globally-installed binary (fast: no dependency resolution).
    Fall back to `npx --yes <package>` (slow on first use / flaky networks,
    since it re-resolves the whole dependency tree) only if the binary isn't
    on PATH.

    Returns (command_prefix, via_npx).
    """
    global_bin = shutil.which(bin_name)
    if global_bin:
        return [global_bin], False
    return ["npx", "--yes", package], True


def count_mermaid_blocks(markdown: str) -> int:
    return len(MERMAID_PATTERN.findall(markdown))


def render_markdown_diagrams(
    markdown_path: Path,
    diagrams_dir: Path,
    chrome_path: Optional[str],
    theme: str,
    background: str,
) -> Path:
    """
    Render every Mermaid block in `markdown_path` to SVG and return a new
    markdown file with the mermaid fences replaced by image references.

    Uses mmdc's native Markdown mode (`-i file.md -o out.md -a artefacts/`),
    which extracts and renders *all* diagrams in a single Chrome/Chromium
    launch. This is both faster and far more reliable than launching a
    fresh browser instance per diagram (one launch per diagram multiplies
    the odds of a slow/stuck launch under system load, antivirus scanning,
    etc. — exactly what caused multi-minute hangs/timeouts in practice).
    """
    diagrams_dir.mkdir(parents=True, exist_ok=True)
    rendered_md_path = diagrams_dir / markdown_path.name

    puppeteer_config_path = None
    if chrome_path:
        puppeteer_config_path = diagrams_dir / "_puppeteer-config.json"
        # Written via json.dumps + write_text (no BOM) — a BOM here (e.g. from
        # PowerShell's default `Out-File`/`Set-Content -Encoding utf8`) makes
        # mmdc's JSON.parse fail immediately with a cryptic syntax error.
        puppeteer_config_path.write_text(
            json.dumps({"executablePath": chrome_path}), encoding="utf-8"
        )

    mmdc_prefix, via_npx = resolve_tool_command("mmdc", MMDC_PACKAGE)
    if via_npx:
        print(
            "  (mmdc not found globally — using npx, which is slower on "
            "first use. Run `npm install -g @mermaid-js/mermaid-cli` to "
            "speed this up.)"
        )

    cmd = mmdc_prefix + [
        "-i", str(markdown_path),
        "-o", str(rendered_md_path),
        "-a", str(diagrams_dir),
        "-t", theme,
        "-b", background,
    ]
    if puppeteer_config_path:
        cmd.extend(["-p", str(puppeteer_config_path)])

    print("Rendering Mermaid diagrams (single browser session)...", end=" ", flush=True)
    result = run_cmd(
        cmd, capture_output=True, text=True, timeout=240 if via_npx else 120,
        env=npx_env(skip_chromium_download=bool(chrome_path)),
    )

    if result.returncode != 0 or not rendered_md_path.exists():
        print("FAILED")
        error = (result.stderr or result.stdout or "unknown error").strip()
        raise RuntimeError(f"mmdc failed rendering diagrams:\n{error}")

    print("OK")
    return rendered_md_path


def convert_to_pdf(
    markdown_path: Path,
    basedir: Path,
    output_pdf: Path,
    chrome_path: Optional[str],
    stylesheet: Optional[Path],
) -> None:
    """Convert a markdown file (with image refs, no mermaid fences) to PDF."""
    config = {
        "dest": str(output_pdf),
        "basedir": str(basedir),
        "pdf_options": {
            "format": "A4",
            "margin": "20mm",
            "printBackground": True,
        },
    }
    if chrome_path:
        config["launch_options"] = {"executablePath": chrome_path}
    if stylesheet:
        config["stylesheet"] = [str(stylesheet)]

    config_path = basedir / "_md-to-pdf-config.json"
    config_path.write_text(json.dumps(config), encoding="utf-8")

    md_to_pdf_prefix, via_npx = resolve_tool_command("md-to-pdf", MD_TO_PDF_PACKAGE)
    if via_npx:
        print(
            "\n  (md-to-pdf not found globally — using npx, which is slower "
            "on first use. Run `npm install -g md-to-pdf` to speed this up.)"
        )

    cmd = md_to_pdf_prefix + [
        str(markdown_path),
        "--config-file", str(config_path),
    ]

    print("Converting to PDF...", end=" ", flush=True)
    result = run_cmd(
        cmd, capture_output=True, text=True, timeout=240 if via_npx else 60,
        env=npx_env(skip_chromium_download=bool(chrome_path)),
    )

    if result.returncode != 0 or not output_pdf.exists():
        print("FAILED")
        error = (result.stderr or result.stdout or "unknown error").strip()
        raise RuntimeError(f"md-to-pdf failed:\n{error}")

    print("OK")


def export_das_to_pdf(
    markdown_file: Path,
    output_pdf: Optional[Path] = None,
    chrome_path: Optional[str] = None,
    theme: str = "default",
    background: str = "white",
    stylesheet: Optional[Path] = None,
    keep_temp: bool = False,
) -> Path:
    if not markdown_file.is_file():
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")

    if not check_node_available():
        raise EnvironmentError(
            "Node.js not found on PATH. Install Node.js >= 18 to use this "
            "script (see ../references/pdf-export.md)."
        )

    output_pdf = output_pdf or markdown_file.with_suffix(".pdf")
    output_pdf = output_pdf.resolve()
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    if chrome_path is None:
        chrome_path = find_chrome()
        if chrome_path:
            print(f"Reusing local browser: {chrome_path}")
        else:
            print(
                "No local Chrome/Edge found; Puppeteer will download its "
                "own Chromium on first use (~300MB, requires internet)."
            )

    markdown_content = markdown_file.read_text(encoding="utf-8")
    diagram_count = count_mermaid_blocks(markdown_content)
    print(f"Found {diagram_count} Mermaid diagram(s) in {markdown_file.name}")

    temp_dir_ctx = tempfile.TemporaryDirectory(prefix="das_to_pdf_")
    temp_dir = Path(temp_dir_ctx.name)
    try:
        if diagram_count:
            diagrams_dir = temp_dir / "diagrams"
            temp_md_path = render_markdown_diagrams(
                markdown_file, diagrams_dir, chrome_path, theme, background
            )
            basedir = diagrams_dir
        else:
            temp_md_path = temp_dir / markdown_file.name
            temp_md_path.write_text(markdown_content, encoding="utf-8")
            basedir = temp_dir

        convert_to_pdf(temp_md_path, basedir, output_pdf, chrome_path, stylesheet)
    finally:
        if keep_temp:
            print(f"Temporary working directory kept at: {temp_dir}")
        else:
            temp_dir_ctx.cleanup()

    return output_pdf


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export a DAS Markdown file (with Mermaid diagrams) to PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python das_to_pdf.py .specs/das/DAS-foo.md
  python das_to_pdf.py .specs/das/DAS-foo.md --output out/DAS-foo.pdf
  python das_to_pdf.py .specs/das/DAS-foo.md --keep-temp
  python das_to_pdf.py .specs/das/DAS-foo.md --theme dark
        """,
    )
    parser.add_argument("markdown_file", type=Path, help="Path to the DAS .md file")
    parser.add_argument("--output", "-o", type=Path, help="Output PDF path (default: <input>.pdf)")
    parser.add_argument("--chrome-path", type=str, help="Force a specific browser executable")
    parser.add_argument(
        "--theme", default="default",
        choices=["default", "forest", "dark", "neutral"],
        help="Mermaid theme for the rendered diagrams (default: default)",
    )
    parser.add_argument(
        "--background", default="white",
        help="Mermaid diagram background color (default: white)",
    )
    parser.add_argument(
        "--stylesheet", type=Path,
        help="Extra CSS file for the PDF (default: ../assets/pdf-style.css if present)",
    )
    parser.add_argument(
        "--keep-temp", action="store_true",
        help="Do not delete the temporary working directory (useful for debugging)",
    )

    args = parser.parse_args()

    try:
        sys.stdout.reconfigure(line_buffering=True)  # show progress as it happens
    except AttributeError:
        pass

    stylesheet = args.stylesheet
    if stylesheet is None:
        default_stylesheet = Path(__file__).parent.parent / "assets" / "pdf-style.css"
        if default_stylesheet.is_file():
            stylesheet = default_stylesheet

    try:
        output_pdf = export_das_to_pdf(
            markdown_file=args.markdown_file,
            output_pdf=args.output,
            chrome_path=args.chrome_path,
            theme=args.theme,
            background=args.background,
            stylesheet=stylesheet,
            keep_temp=args.keep_temp,
        )
    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"\nSuccess: {output_pdf}")


if __name__ == "__main__":
    main()
