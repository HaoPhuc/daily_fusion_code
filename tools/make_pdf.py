#!/usr/bin/env python3
"""Render an exercise (task README.md + theory note) into PDFs.

The theory note lives in theory/<folder>.md (older exercises: <folder>/THEORY.md).

Usage:  python3 tools/make_pdf.py exercises/<folder> [exercises/<folder> ...]
Output: exercises/<folder>/<folder>.pdf          task + theory
        exercises/<folder>/<folder>_theory.pdf   theory only (if a theory note exists)

Needs pandoc, npm (KaTeX is installed into a cache dir on first run) and
Python Playwright with Chromium.
"""
import html
import os
import pathlib
import posixpath
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
CACHE = pathlib.Path(os.environ.get("DFC_PDF_CACHE", pathlib.Path.home() / ".cache" / "dfc-pdf"))
GH = "https://github.com/HaoPhuc/daily_fusion_code"
KATEX_VERSION = "0.16.11"

LANG_COLORS = {
    "python": "#2f6db0",
    "matlab": "#c8551f",
    "fortran": "#5b45b0",
    "simulink": "#13807a",
    "c++": "#b8326a",
}
DEFAULT_COLOR = "#3b4a63"


def katex_dist():
    dist = CACHE / "node_modules" / "katex" / "dist"
    if not (dist / "katex.min.js").exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["npm", "install", "--silent", "--no-audit", "--no-fund",
             "--prefix", str(CACHE), f"katex@{KATEX_VERSION}"],
            check=True,
        )
    return dist


def md_to_html(text):
    out = subprocess.run(
        ["pandoc", "-f", "gfm+tex_math_dollars-strikeout", "-t", "html5",
         "--katex", "--wrap=none"],
        input=text, capture_output=True, text=True, check=True,
    )
    return out.stdout


def split_head(md):
    """Pull the '# Title' line and the '**meta · line**' out of a markdown file."""
    lines = md.splitlines()
    title, meta, body = "", "", []
    for line in lines:
        s = line.strip()
        if not title and s.startswith("# "):
            title = s[2:].strip()
            continue
        if title and not meta and not body and s.startswith("**") and "·" in s:
            meta = s.strip("*").strip()
            continue
        if title and not body and not s:
            continue
        body.append(line)
    return title, meta, "\n".join(body)


def rewrite_links(fragment, rel_folder, folder_name=""):
    def fix(m):
        href = m.group(1)
        if re.match(r"^(https?:|mailto:|#)", href):
            return m.group(0)
        name = href.split("#")[0]
        if name.lstrip("./") in ("THEORY.md", f"{folder_name}_theory.pdf"):
            return 'href="#theory" data-theory="1"'
        if name.lstrip("./") == "README.md":
            return 'href="#exercise"'
        path = posixpath.normpath(posixpath.join(rel_folder, href))
        kind = "blob" if posixpath.splitext(path)[1] else "tree"
        return f'href="{GH}/{kind}/main/{path}"'
    fragment = re.sub(r'href="([^"]*)"', fix, fragment)
    return re.sub(r'(<a [^>]*data-theory="1"[^>]*>).*?</a>', r'\1the Theory pages</a>', fragment)


def theory_file(folder):
    """Theory note for an exercise folder, and the repo-relative dir its links are relative to."""
    new = REPO / "theory" / f"{folder.name}.md"
    if new.exists():
        return new, "theory"
    old = folder / "THEORY.md"
    return (old, folder.resolve().relative_to(REPO).as_posix()) if old.exists() else (None, None)


def wrap_sections(fragment):
    """Wrap each <h2> and the content after it in <section class="s s-<id>">."""
    parts = re.split(r"(?=<h2[ >])", fragment)
    out = []
    for part in parts:
        m = re.match(r'<h2(?: id="([^"]*)")?[^>]*>(.*?)</h2>', part, re.S)
        if not m:
            out.append(part)
            continue
        sid = m.group(1) or re.sub(r"[^a-z0-9]+", "-", re.sub("<[^>]+>", "", m.group(2)).lower()).strip("-")
        out.append(f'<section class="s s-{sid}">{part}</section>')
    return "".join(out)


def tint(hex_color, amount):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    mix = lambda c: round(c + (255 - c) * (1 - amount))
    return "#%02x%02x%02x" % (mix(r), mix(g), mix(b))


CSS = """
@page { size: A4; margin: 15mm 18mm 18mm 18mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: 'Bitstream Charter', Charter, 'DejaVu Serif', Georgia, serif;
       font-size: 10.4pt; line-height: 1.48; color: #1c2230; }
h1, h2, h3, .kicker, .chip, table, th, td, .footer-note { font-family: Inter, 'DejaVu Sans', sans-serif; }
p { margin: 0 0 6.5pt; }
p:has(+ table), p:has(+ pre), p:has(+ div.sourceCode) { break-after: avoid; }
a { color: var(--acc-dark); text-decoration: none; border-bottom: 0.6pt solid var(--acc-soft); }
strong { font-weight: 700; }

.top { border-top: 5pt solid var(--acc); padding-top: 12pt; margin-bottom: 14pt; }
.kicker { font-size: 7.6pt; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--acc-dark); }
.top h1 { font-size: 21pt; line-height: 1.18; font-weight: 700; margin: 5pt 0 9pt; letter-spacing: -0.01em; }
.chips { display: flex; gap: 5pt; flex-wrap: wrap; }
.chip { font-size: 8pt; font-weight: 500; padding: 2.5pt 8pt; border-radius: 20pt; background: #eef0f3; color: #3b4352; }
.chip.lang { background: var(--acc); color: #fff; font-weight: 600; }

.theory { break-before: page; }
.theory .top { border-top-width: 2pt; }
.theory .top h1 { font-size: 17pt; }

h2 { font-size: 12.2pt; font-weight: 650; margin: 13pt 0 5pt; color: #141a26; break-after: avoid; }
h2::before { content: ""; display: inline-block; width: 7pt; height: 7pt; border-radius: 2pt;
             background: var(--acc); margin-right: 7pt; vertical-align: 1pt; }
h3 { font-size: 10.6pt; font-weight: 650; margin: 11pt 0 4pt; break-after: avoid; }

ol, ul { margin: 0 0 8pt; padding-left: 17pt; }
li { margin: 2.5pt 0; }
li > ul, li > ol { margin: 3pt 0 4pt; }
ol > li::marker { font-family: Inter, sans-serif; font-weight: 600; color: var(--acc-dark); font-size: 9.5pt; }
ul > li::marker { color: var(--acc); }

code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #f1f2f5;
       padding: 0.6pt 3.5pt; border-radius: 3pt; }
pre { background: #f6f7f9; border: 0.6pt solid #e3e6eb; border-radius: 5pt; padding: 7pt 9pt;
      margin: 4pt 0 9pt; overflow: hidden; white-space: pre-wrap; break-inside: avoid; line-height: 1.42; }
pre code { background: none; padding: 0; font-size: 8.4pt; }
pre a { border: none; color: inherit; }
.kw, .cf, .im { color: #7a3fc4; } .dt, .at { color: #0f6f87; } .dv, .fl, .bn, .sc, .cn { color: #a85a07; }
.st, .ch, .vs, .ss { color: #187a3c; } .co, .do, .cv, .an { color: #8a909b; font-style: italic; }
.fu, .bu, .ex { color: #1f55c2; } .er, .al { color: #b42318; }

table { border-collapse: collapse; width: 100%; font-size: 8.8pt; margin: 4pt 0 10pt; break-inside: avoid; line-height: 1.38; }
th { text-align: left; font-weight: 600; background: #f1f2f5; color: #353c4a; }
th, td { padding: 4pt 7pt; border-bottom: 0.6pt solid #e3e6eb; vertical-align: top; }
td code { font-size: 8pt; }

.katex { font-size: 1.06em; }
.katex-display { margin: 5pt 0 7pt; break-inside: avoid; }
p:has(> .katex-display:only-child), p:has(> span.display:only-child) { margin: 0; }

.s-check-yourself, .s-submit { border-radius: 6pt; padding: 1pt 11pt 3pt; margin: 12pt 0 8pt; break-inside: avoid; }
.s-check-yourself { background: var(--acc-bg); border-left: 3pt solid var(--acc); }
.s-submit { background: #f4f5f7; }
.s-recall { border: 1pt dashed var(--acc-soft); border-radius: 6pt; padding: 1pt 11pt 3pt; margin: 12pt 0 8pt; break-inside: avoid; }
.s-recall h2 { margin-top: 8pt; }
.s-syntax-youll-need { background: #f6f7f9; border-radius: 6pt; padding: 1pt 11pt 3pt; margin: 10pt 0 8pt; }
.s-syntax-youll-need h2 { margin-top: 8pt; }
.s-syntax-youll-need h2::before { display: none; }
.s-check-yourself h2, .s-submit h2 { margin-top: 8pt; }
.s-check-yourself h2::before, .s-submit h2::before { display: none; }

blockquote { margin: 6pt 0; padding: 2pt 10pt; border-left: 2.5pt solid var(--acc-soft); color: #424a59; }
hr { border: none; border-top: 0.6pt solid #e3e6eb; margin: 12pt 0; }
img { max-width: 100%; }
.only-theory .theory { break-before: auto; }
.only-theory .theory .top { border-top-width: 5pt; }
"""


def build_html(folder, theory_only=False):
    rel = folder.resolve().relative_to(REPO).as_posix()
    readme = (folder / "README.md").read_text(encoding="utf-8")
    title, meta, body = split_head(readme)
    meta_parts = [p.strip() for p in meta.split("·")] if meta else []
    week = next((p for p in meta_parts if p.lower().startswith("week")), "")
    # language: from the meta line, else from an old-style folder name (date_lang_slug)
    lang_label = next((p for p in meta_parts if p.lower() in LANG_COLORS), "")
    if not lang_label:
        m = re.match(r"\d{4}-\d{2}-\d{2}_(?:(?:mon|tue|wed|thu|fri|sat|sun)_)?([a-z+]+)_", folder.name)
        lang_label = m.group(1).capitalize() if m else ""
    acc = LANG_COLORS.get(lang_label.lower(), DEFAULT_COLOR)
    chips = [f'<span class="chip lang">{html.escape(lang_label)}</span>']
    chips += [f'<span class="chip">{html.escape(p)}</span>' for p in meta_parts if p not in (lang_label, week)]
    kicker = "Daily fusion code" + (f" · {week}" if week else "")

    sections = [] if theory_only else [
        f'<article id="exercise"><header class="top"><div class="kicker">{html.escape(kicker)}</div>'
        f'<h1>{md_inline(title)}</h1><div class="chips">{"".join(chips)}</div></header>'
        f'{wrap_sections(rewrite_links(md_to_html(body), rel, folder.name))}</article>'
    ]

    theory_path, theory_rel = theory_file(folder)
    if theory_path:
        t_title, _, t_body = split_head(theory_path.read_text(encoding="utf-8"))
        t_title = re.sub(r"^(Theory|Refresher)\s*:\s*", "", t_title, flags=re.I)
        t_title = t_title[:1].upper() + t_title[1:]
        t_html = rewrite_links(md_to_html(t_body), theory_rel, folder.name)
        if theory_only:
            t_html = t_html.replace('href="#exercise"', f'href="{GH}/tree/main/{rel}"')
            bits = ["Theory", lang_label] + [p for p in meta_parts if re.match(r"^[A-Z]+-\d", p)] + ([week] if week else [])
            head = f'<div class="kicker">{html.escape(" · ".join(bits))}</div><h1>{md_inline(t_title)}</h1>'
        else:
            head = f'<div class="kicker">Theory</div><h1>{md_inline(t_title)}</h1>'
        sections.append(
            f'<article id="theory" class="theory"><header class="top">{head}</header>'
            f'{wrap_sections(t_html)}</article>'
        )

    kx = katex_dist()
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{(kx / 'katex.min.css').as_uri()}">
<style>:root {{ --acc: {acc}; --acc-dark: {shade(acc)}; --acc-soft: {tint(acc, 0.45)}; --acc-bg: {tint(acc, 0.08)}; }}
{CSS}</style></head><body class="{'only-theory' if theory_only else ''}">
{''.join(sections)}
<script src="{(kx / 'katex.min.js').as_uri()}"></script>
<script>
document.querySelectorAll('span.math').forEach(function (el) {{
  katex.render(el.textContent, el, {{displayMode: el.classList.contains('display'), throwOnError: false}});
}});
window.__rendered = true;
</script></body></html>"""


def md_inline(text):
    frag = md_to_html(text).strip()
    return re.sub(r"^<p>(.*)</p>$", r"\1", frag, flags=re.S)


def shade(hex_color, f=0.78):
    h = hex_color.lstrip("#")
    return "#%02x%02x%02x" % tuple(round(int(h[i:i + 2], 16) * f) for i in (0, 2, 4))


def render(folders):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for folder in folders:
            folder = pathlib.Path(folder)
            CACHE.mkdir(parents=True, exist_ok=True)
            footer = (
                '<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#8a909b;'
                'padding:0 18mm;display:flex;justify-content:space-between;">'
                f'<span>HaoPhuc/daily_fusion_code · {html.escape(folder.name)}</span>'
                '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
            )
            jobs = [(False, folder / f"{folder.name}.pdf")]
            if theory_file(folder)[0]:
                jobs.append((True, folder / f"{folder.name}_theory.pdf"))
            for theory_only, out in jobs:
                html_path = CACHE / f"{out.stem}.html"
                html_path.write_text(build_html(folder, theory_only), encoding="utf-8")
                page.goto(html_path.as_uri())
                page.wait_for_function("window.__rendered === true")
                page.evaluate("document.fonts.ready")
                errors = page.evaluate("document.querySelectorAll('.katex-error').length")
                page.pdf(path=str(out), prefer_css_page_size=True, print_background=True,
                         display_header_footer=True, header_template="<span></span>",
                         footer_template=footer)
                note = f" ({errors} math errors)" if errors else ""
                print(f"wrote {out}{note}")
        browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    render(sys.argv[1:])
