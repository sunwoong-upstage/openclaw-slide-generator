#!/usr/bin/env python3
"""
generate_slides.py — Create a standalone HTML reveal.js slide deck from JSON.

Usage:
    python3 generate_slides.py --input slides.json --output deck.html
    cat slides.json | python3 generate_slides.py --output deck.html
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Theme CSS
# ---------------------------------------------------------------------------

THEMES = {
    "modern": """
:root{--bg:#0f172a;--surface:#111827;--fg:#e5eefb;--accent:#38bdf8;--accent-2:#7dd3fc;--muted:#cbd5e1;--border:rgba(148,163,184,0.28);--font:'Inter','Noto Sans KR',sans-serif;}
html,body{background:var(--bg)!important;color:var(--fg)!important;font-family:var(--font);}
body{margin:0;}
.reveal,.reveal .slides,.reveal section{background:var(--bg)!important;color:var(--fg)!important;}
.reveal section{padding:0.2em 0.6em;}
.reveal,.reveal p,.reveal li,.reveal ul,.reveal ol,.reveal div,.reveal span,.reveal strong,.reveal em,.reveal td,.reveal th,.reveal blockquote,.reveal cite{color:var(--fg)!important;}
.reveal h1,.reveal h2,.reveal h3,.reveal h4{font-weight:700;letter-spacing:-0.02em;line-height:1.2;}
.reveal h1{font-size:2.2em;color:#f8fbff!important;}
.reveal h2{font-size:1.6em;color:var(--accent)!important;}
.reveal h3,.reveal h4{color:var(--accent-2)!important;}
.reveal p,.reveal li{font-size:0.95em;line-height:1.65;}
.reveal li{margin-bottom:0.42em;}
.reveal a{color:#93c5fd!important;text-decoration:underline;}
.reveal strong{color:#ffffff!important;}
.reveal blockquote{background:rgba(56,189,248,0.12)!important;border-left:4px solid var(--accent)!important;padding:1em 1.5em;font-size:1.1em;font-style:italic;color:var(--fg)!important;border-radius:10px;}
.reveal code{background:rgba(255,255,255,0.12)!important;color:#f8fafc!important;padding:0.2em 0.4em;border-radius:4px;font-family:'Fira Code',monospace;font-size:0.85em;}
.reveal pre{background:rgba(255,255,255,0.05)!important;border:1px solid var(--border);border-radius:10px;padding:0.2em;}
.reveal pre code{background:transparent!important;color:#f8fafc!important;padding:1em;display:block;border-radius:8px;font-size:0.75em;}
.reveal table{font-size:0.8em;border-collapse:collapse;width:100%;background:var(--surface)!important;border-radius:12px;overflow:hidden;}
.reveal th,.reveal td{padding:0.7em 1em;border-bottom:1px solid var(--border);text-align:left;background:transparent!important;}
.reveal th{color:#e0f2fe!important;font-weight:700;border-bottom:2px solid var(--accent);}
.reveal tr:last-child td{border-bottom:none;}
.reveal .title-slide h1{font-size:2.8em;margin-bottom:0.2em;}
.reveal .title-slide .subtitle{font-size:1.1em;color:var(--muted)!important;margin-top:0.5em;}
.reveal .title-slide .meta{font-size:0.8em;color:#94a3b8!important;margin-top:1.5em;}
.reveal .closing-slide h2{font-size:2em;color:var(--accent)!important;}
.reveal .two-col{display:flex;gap:2em;text-align:left;align-items:flex-start;}
.reveal .two-col > div{flex:1;background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:12px;padding:1em;}
.reveal .slide-number{color:#94a3b8!important;font-size:0.6em;}
.reveal .controls,.reveal .progress{color:var(--accent)!important;}
""",
    "academic": """
:root{--bg:#ffffff;--fg:#1a1a1a;--accent:#2563eb;--muted:#525252;--font:'Merriweather','Noto Serif KR',serif;}
body{background:var(--bg);color:var(--fg);font-family:var(--font);}
.reveal{background:var(--bg);}
.reveal h1,.reveal h2,.reveal h3{color:var(--fg);font-weight:700;}
.reveal h1{font-size:2em;border-bottom:2px solid var(--accent);padding-bottom:0.3em;}
.reveal h2{font-size:1.5em;color:var(--accent);}
.reveal li{font-size:0.9em;line-height:1.7;margin-bottom:0.5em;}
.reveal blockquote{background:#f3f4f6;border-left:4px solid var(--accent);padding:1em 1.5em;font-size:1em;font-style:italic;}
.reveal code{background:#f3f4f6;padding:0.2em 0.4em;border-radius:3px;font-family:'Courier New',monospace;font-size:0.85em;}
.reveal pre code{background:#f3f4f6;padding:1em;display:block;border-radius:6px;font-size:0.75em;}
.reveal table{font-size:0.8em;border-collapse:collapse;width:100%;}
.reveal th,.reveal td{padding:0.6em 1em;border:1px solid #e5e7eb;text-align:left;}
.reveal th{background:#f3f4f6;color:var(--accent);font-weight:600;}
.reveal .title-slide h1{font-size:2.4em;}
.reveal .title-slide .subtitle{font-size:1em;color:var(--muted);}
.reveal .title-slide .meta{font-size:0.75em;color:var(--muted);margin-top:1.5em;}
.reveal .closing-slide h2{font-size:1.8em;color:var(--accent);}
.reveal .two-col{display:flex;gap:2em;text-align:left;}
.reveal .two-col > div{flex:1;}
.reveal .slide-number{color:var(--muted);font-size:0.6em;}
""",
    "playful": """
:root{--bg:#fef3c7;--fg:#451a03;--accent:#ea580c;--muted:#92400e;--font:'Comic Neue','Noto Sans KR',sans-serif;}
body{background:var(--bg);color:var(--fg);font-family:var(--font);}
.reveal{background:var(--bg);}
.reveal h1,.reveal h2,.reveal h3{color:var(--fg);font-weight:700;}
.reveal h1{font-size:2.4em;transform:rotate(-1deg);}
.reveal h2{font-size:1.6em;color:var(--accent);transform:rotate(0.5deg);}
.reveal li{font-size:1em;line-height:1.7;margin-bottom:0.5em;}
.reveal blockquote{background:rgba(234,88,12,0.1);border-left:5px solid var(--accent);padding:1em 1.5em;font-size:1.1em;font-style:italic;border-radius:0 12px 12px 0;}
.reveal code{background:rgba(234,88,12,0.1);padding:0.2em 0.5em;border-radius:6px;font-family:'Fira Code',monospace;font-size:0.85em;}
.reveal pre code{background:rgba(234,88,12,0.05);padding:1em;display:block;border-radius:12px;font-size:0.75em;}
.reveal table{font-size:0.85em;border-collapse:separate;border-spacing:0;width:100%;}
.reveal th,.reveal td{padding:0.6em 1em;border-bottom:2px solid var(--accent);text-align:left;}
.reveal th{color:var(--accent);font-weight:700;font-size:1.1em;}
.reveal .title-slide h1{font-size:2.8em;}
.reveal .title-slide .subtitle{font-size:1.1em;color:var(--muted);}
.reveal .title-slide .meta{font-size:0.8em;color:var(--muted);margin-top:1.5em;}
.reveal .closing-slide h2{font-size:2em;color:var(--accent);}
.reveal .two-col{display:flex;gap:2em;text-align:left;}
.reveal .two-col > div{flex:1;}
.reveal .slide-number{color:var(--muted);font-size:0.6em;}
""",
    "minimal": """
:root{--bg:#fafafa;--fg:#171717;--accent:#525252;--muted:#a3a3a3;--font:'Helvetica Neue','Noto Sans KR',sans-serif;}
body{background:var(--bg);color:var(--fg);font-family:var(--font);}
.reveal{background:var(--bg);}
.reveal h1,.reveal h2,.reveal h3{color:var(--fg);font-weight:400;}
.reveal h1{font-size:2.6em;letter-spacing:-0.03em;}
.reveal h2{font-size:1.4em;color:var(--accent);text-transform:uppercase;letter-spacing:0.1em;}
.reveal li{font-size:0.95em;line-height:1.8;margin-bottom:0.6em;}
.reveal blockquote{border-left:2px solid var(--muted);padding:0.5em 1.5em;font-size:1em;font-style:italic;color:var(--muted);}
.reveal code{background:#e5e5e5;padding:0.15em 0.4em;border-radius:3px;font-family:monospace;font-size:0.85em;}
.reveal pre code{background:#f0f0f0;padding:1em;display:block;border-radius:4px;font-size:0.75em;}
.reveal table{font-size:0.8em;border-collapse:collapse;width:100%;}
.reveal th,.reveal td{padding:0.5em 1em;border-bottom:1px solid #e5e5e5;text-align:left;}
.reveal th{color:var(--fg);font-weight:500;border-bottom:2px solid var(--fg);}
.reveal .title-slide h1{font-size:3em;}
.reveal .title-slide .subtitle{font-size:1em;color:var(--muted);margin-top:1em;}
.reveal .title-slide .meta{font-size:0.75em;color:var(--muted);margin-top:2em;}
.reveal .closing-slide h2{font-size:2em;color:var(--fg);font-weight:300;}
.reveal .two-col{display:flex;gap:2em;text-align:left;}
.reveal .two-col > div{flex:1;}
.reveal .slide-number{color:var(--muted);font-size:0.55em;}
""",
    "corporate": """
:root{--bg:#f8fafc;--fg:#0f172a;--accent:#0369a1;--muted:#475569;--font:'Segoe UI','Noto Sans KR',sans-serif;}
body{background:var(--bg);color:var(--fg);font-family:var(--font);}
.reveal{background:var(--bg);}
.reveal h1,.reveal h2,.reveal h3{color:var(--fg);font-weight:600;}
.reveal h1{font-size:2em;}
.reveal h2{font-size:1.4em;color:var(--accent);border-bottom:1px solid #cbd5e1;padding-bottom:0.3em;}
.reveal li{font-size:0.9em;line-height:1.7;margin-bottom:0.5em;}
.reveal blockquote{background:#f1f5f9;border-left:3px solid var(--accent);padding:1em 1.5em;font-size:1em;font-style:italic;}
.reveal code{background:#e2e8f0;padding:0.2em 0.4em;border-radius:4px;font-family:'Consolas',monospace;font-size:0.85em;}
.reveal pre code{background:#f1f5f9;padding:1em;display:block;border-radius:8px;font-size:0.75em;}
.reveal table{font-size:0.8em;border-collapse:collapse;width:100%;}
.reveal th,.reveal td{padding:0.6em 1em;border:1px solid #cbd5e1;text-align:left;}
.reveal th{background:#f1f5f9;color:var(--accent);font-weight:600;}
.reveal .title-slide h1{font-size:2.2em;}
.reveal .title-slide .subtitle{font-size:1em;color:var(--muted);}
.reveal .title-slide .meta{font-size:0.75em;color:var(--muted);margin-top:1.5em;}
.reveal .closing-slide h2{font-size:1.8em;color:var(--accent);}
.reveal .two-col{display:flex;gap:2em;text-align:left;}
.reveal .two-col > div{flex:1;}
.reveal .slide-number{color:var(--muted);font-size:0.6em;}
""",
}

NOTO_FONTS = {
    "ko": "Noto+Sans+KR",
    "ja": "Noto+Sans+JP",
    "zh": "Noto+Sans+SC",
    "zh-tw": "Noto+Sans+TC",
}


def escape_html(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def md_to_html(text):
    text = escape_html(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def md_block_to_html(text):
    lines = text.strip().splitlines()
    html_parts = []
    in_list = False
    list_items = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith(("- ", "* ", "1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ")):
            if not in_list:
                in_list = True
                list_items = []
            content = re.sub(r"^(-|\*|\d+\.)\s+", "", stripped)
            list_items.append(f"<li>{md_to_html(content)}</li>")
        else:
            if in_list:
                html_parts.append("<ul>" + "\n".join(list_items) + "</ul>")
                in_list = False
                list_items = []
            if stripped:
                html_parts.append(f"<p>{md_to_html(stripped)}</p>")

    if in_list:
        html_parts.append("<ul>" + "\n".join(list_items) + "</ul>")

    return "\n".join(html_parts)


def render_slide(slide, idx):
    stype = slide.get("type", "bullet")
    notes = slide.get("speaker_notes", "")
    notes_html = f'\n    <aside class="notes">{escape_html(notes)}</aside>' if notes else ""

    if stype == "title":
        subtitle = slide.get("subtitle", "")
        author = slide.get("author", "")
        date = slide.get("date", "")
        meta_parts = [p for p in [author, date] if p]
        meta = " · ".join(meta_parts)
        subtitle_html = f'<p class="subtitle">{md_to_html(subtitle)}</p>' if subtitle else ""
        meta_html = f'<p class="meta">{md_to_html(meta)}</p>' if meta else ""
        return (
            f'<section class="title-slide">\n'
            f'    <h1>{md_to_html(slide.get("content", ""))}</h1>\n'
            f'    {subtitle_html}\n'
            f'    {meta_html}\n'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "heading":
        return (
            f'<section>\n'
            f'    <h2>{md_to_html(slide.get("content", ""))}</h2>\n'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "bullet":
        items = slide.get("items", [])
        lis = "\n".join(f"        <li>{md_to_html(item)}</li>" for item in items)
        return (
            f'<section>\n'
            f'    <ul>\n{lis}\n    </ul>\n'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "code":
        lang = slide.get("language", "")
        code = slide.get("code", "")
        code_escaped = escape_html(code)
        cls = f' class="language-{lang}"' if lang else ""
        return (
            f'<section>\n'
            f'    <pre><code{cls}>{code_escaped}</code></pre>\n'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "image":
        src = escape_html(slide.get("src", ""))
        caption = slide.get("caption", "")
        cap_html = f'    <p class="caption">{md_to_html(caption)}</p>\n' if caption else ""
        return (
            f'<section>\n'
            f'    <img src="{src}" style="max-height:70vh;max-width:90%;" />\n'
            f'{cap_html}'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "quote":
        text = md_to_html(slide.get("text", ""))
        author = md_to_html(slide.get("author", ""))
        author_html = f'<cite>— {author}</cite>' if author else ""
        return (
            f'<section>\n'
            f'    <blockquote>\n'
            f'        <p>{text}</p>\n'
            f'        {author_html}\n'
            f'    </blockquote>\n'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "two_col":
        left = md_block_to_html(slide.get("left", ""))
        right = md_block_to_html(slide.get("right", ""))
        return (
            f'<section>\n'
            f'    <div class="two-col">\n'
            f'        <div>{left}</div>\n'
            f'        <div>{right}</div>\n'
            f'    </div>\n'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "table":
        headers = slide.get("headers", [])
        rows = slide.get("rows", [])
        ths = "\n".join(f"            <th>{escape_html(h)}</th>" for h in headers)
        trs = []
        for row in rows:
            tds = "\n".join(f"            <td>{escape_html(str(c))}</td>" for c in row)
            trs.append(f"        <tr>\n{tds}\n        </tr>")
        body = "\n".join(trs)
        return (
            f'<section>\n'
            f'    <table>\n'
            f'        <thead>\n'
            f'            <tr>\n{ths}\n            </tr>\n'
            f'        </thead>\n'
            f'        <tbody>\n'
            f'{body}\n'
            f'        </tbody>\n'
            f'    </table>\n'
            f'{notes_html}\n'
            f'</section>'
        )

    elif stype == "closing":
        content = md_to_html(slide.get("content", ""))
        subtitle = slide.get("subtitle", "")
        sub_html = f'    <p class="subtitle">{md_to_html(subtitle)}</p>\n' if subtitle else ""
        return (
            f'<section class="closing-slide">\n'
            f'    <h2>{content}</h2>\n'
            f'{sub_html}'
            f'{notes_html}\n'
            f'</section>'
        )

    else:
        return (
            f'<section>\n'
            f'    <p>{md_to_html(str(slide))}</p>\n'
            f'{notes_html}\n'
            f'</section>'
        )


def build_html(data):
    title = data.get("title", "Presentation")
    style_name = data.get("style", "modern")
    lang = data.get("lang", "en")
    slides = data.get("slides", [])

    theme_css = THEMES.get(style_name, THEMES["modern"])

    font_families = ["Inter", "Fira Code"]
    noto = NOTO_FONTS.get(lang)
    if noto:
        font_families.append(noto)
    fonts_url = "https://fonts.googleapis.com/css2?family=" + "&family=".join(
        f.replace(" ", "+") for f in font_families
    ) + "&display=swap"

    sections = "\n".join(render_slide(s, i) for i, s in enumerate(slides))

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape_html(title)}</title>
<link rel="stylesheet" href="{fonts_url}">
<link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reveal.css">
<style>
{theme_css}
</style>
</head>
<body>
<div class="reveal">
<div class="slides">
{sections}
</div>
</div>
<script src="https://unpkg.com/reveal.js@4.5.0/dist/reveal.js"></script>
<script>
    Reveal.initialize({{
        hash: true,
        slideNumber: 'c/t',
        transition: 'slide',
        width: 1280,
        height: 720,
        margin: 0.04
    }});
</script>
</body>
</html>"""
    return html


def write_notes(data, output_path):
    lines = [f"Speaker Notes: {data.get('title', 'Presentation')}", "=" * 50, ""]
    for i, slide in enumerate(data.get("slides", []), 1):
        stype = slide.get("type", "")
        if stype == "title":
            lines.append(f"Slide {i}: TITLE — {slide.get('content', '')}")
        elif stype == "heading":
            lines.append(f"Slide {i}: SECTION — {slide.get('content', '')}")
        elif stype == "bullet":
            lines.append(f"Slide {i}: BULLETS")
        elif stype == "code":
            lines.append(f"Slide {i}: CODE — {slide.get('language', '')}")
        elif stype == "image":
            lines.append(f"Slide {i}: IMAGE — {slide.get('src', '')}")
        elif stype == "quote":
            lines.append(f"Slide {i}: QUOTE")
        elif stype == "two_col":
            lines.append(f"Slide {i}: TWO-COLUMN")
        elif stype == "table":
            lines.append(f"Slide {i}: TABLE")
        elif stype == "closing":
            lines.append(f"Slide {i}: CLOSING — {slide.get('content', '')}")
        else:
            lines.append(f"Slide {i}: {stype.upper()}")

        notes = slide.get("speaker_notes", "")
        if notes:
            lines.append(f"  Notes: {notes}")
        else:
            lines.append("  (no notes)")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate HTML slides from JSON.")
    parser.add_argument("--input", "-i", help="Path to JSON input file. If omitted, reads from stdin.")
    parser.add_argument("--output", "-o", required=True, help="Path for output HTML file.")
    args = parser.parse_args()

    if args.input:
        input_text = Path(args.input).read_text(encoding="utf-8")
    else:
        input_text = sys.stdin.read()

    data = json.loads(input_text)
    html = build_html(data)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")

    notes_path = out_path.with_suffix("").with_suffix(out_path.suffix + ".notes.txt")
    write_notes(data, notes_path)

    print(f"Created: {out_path}")
    print(f"Notes:   {notes_path}")


if __name__ == "__main__":
    main()
