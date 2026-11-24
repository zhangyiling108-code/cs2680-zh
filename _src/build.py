"""把 _src/*.md 的逐页中文翻译 + assets/slides 的原版页面图片，生成静态网页课件。

用法：python3 -I _src/build.py   （在 中文课件网页/ 的上级或任意目录运行均可）
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src")
sys.path.insert(0, SRC)
from catalog import LECTURES, COURSE  # noqa: E402

INLINE_PATTERNS = [
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\"=>])(https?://[^\s<）)，。]+)"), r'<a href="\1" target="_blank" rel="noopener">\1</a>'),
]


def inline(text):
    out = html.escape(text, quote=False)
    for pat, rep in INLINE_PATTERNS:
        out = pat.sub(rep, out)
    return out


def render_list(lines):
    """lines: [(indent, ordered, text)] -> nested html list"""
    out, stack = [], []
    for indent, ordered, text in lines:
        level = indent // 2
        tag = "ol" if ordered else "ul"
        while len(stack) > level + 1:
            out.append(f"</li></{stack.pop()}>")
        if len(stack) == level + 1:
            out.append("</li>")
        while len(stack) < level + 1:
            stack.append(tag)
            out.append(f"<{tag}>")
        out.append(f"<li>{inline(text)}")
    while stack:
        out.append(f"</li></{stack.pop()}>")
    return "".join(out)


def render_table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    head, body = cells[0], cells[1:]
    h = "".join(f"<th>{inline(c)}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
    return f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


LIST_RE = re.compile(r"^( *)(?:([-*])|(\d+)[.、]) (.*)$")


def render_body(text):
    blocks, i = [], 0
    lines = text.split("\n")
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            blocks.append("<pre><code>" + html.escape("\n".join(lines[i + 1:j])) + "</code></pre>")
            i = j + 1
            continue
        if LIST_RE.match(line):
            items = []
            while i < len(lines) and (m := LIST_RE.match(lines[i])):
                items.append((len(m.group(1)), m.group(3) is not None, m.group(4)))
                i += 1
            blocks.append(render_list(items))
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[\s\-:|]+\|$", lines[i]):
                    rows.append(lines[i])
                i += 1
            blocks.append(render_table(rows))
            continue
        if line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(inline(lines[i][1:].strip()))
                i += 1
            blocks.append('<div class="callout">' + "<br>".join(quote) + "</div>")
            continue
        if line.startswith("（图") or line.startswith("（来源") or line.startswith("(图"):
            blocks.append(f'<p class="note">{inline(line)}</p>')
            i += 1
            continue
        blocks.append(f"<p>{inline(line)}</p>")
        i += 1
    return "\n".join(blocks)


HEAD_RE = re.compile(r"^## (\d+) \| (.*)$", re.M)


def parse_md(path):
    text = open(path, encoding="utf-8").read()
    parts = HEAD_RE.split(text)
    slides = {}
    for k in range(1, len(parts), 3):
        slides[int(parts[k])] = (parts[k + 1].strip(), parts[k + 2].strip())
    return slides


def page(title, body, rel="", extra_head=""):
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{rel}assets/style.css">
{extra_head}
</head>
<body>
{body}
<script src="{rel}assets/app.js"></script>
</body>
</html>
"""


def topbar(rel, current=None):
    links = []
    for lec in LECTURES:
        cls = ' class="on"' if current == lec["id"] else ""
        links.append(f'<a{cls} href="{rel}lectures/{lec["id"]}.html">{lec["no"]}</a>')
    return f"""<header class="topbar">
  <a class="brand" href="{rel}index.html">CS2680 <span>现代 AI 系统</span></a>
  <nav class="lecnav">{''.join(links)}</nav>
  <div class="tools">
    <div class="seg" role="group" aria-label="显示模式">
      <button data-mode="both" title="原图 + 中文">对照</button>
      <button data-mode="zh" title="只看中文">中文</button>
      <button data-mode="img" title="只看原版">原版</button>
    </div>
    <button class="theme" title="切换深浅色" aria-label="切换深浅色">◐</button>
  </div>
</header>"""


def build_lecture(idx, lec):
    md = os.path.join(SRC, lec["id"] + ".md")
    slides = parse_md(md)
    img_dir = os.path.join(ROOT, "assets", "slides", lec["id"])
    n_imgs = len([f for f in os.listdir(img_dir) if f.endswith(".jpg")])
    missing = [p for p in range(1, n_imgs + 1) if p not in slides]
    if missing:
        print(f"  ! {lec['id']} 缺少翻译页：{missing}")
    toc, cards = [], []
    for p in range(1, n_imgs + 1):
        title, body = slides.get(p, ("（未翻译）", ""))
        toc.append(f'<li><a href="#s{p}"><b>{p}</b>{inline(title)}</a></li>')
        cards.append(f"""<section class="slide" id="s{p}">
  <figure class="orig"><img loading="lazy" src="../assets/slides/{lec['id']}/p{p:02d}.jpg" alt="原版第 {p} 页" width="1280" height="720"></figure>
  <div class="zh">
    <div class="pno">{p} / {n_imgs}</div>
    <h2>{inline(title)}</h2>
    {render_body(body)}
  </div>
</section>""")
    prev_l = LECTURES[idx - 1] if idx > 0 else None
    next_l = LECTURES[idx + 1] if idx + 1 < len(LECTURES) else None
    pager = '<nav class="pager">'
    pager += f'<a href="{prev_l["id"]}.html">← {prev_l["no"]} {html.escape(prev_l["zh"])}</a>' if prev_l else "<span></span>"
    pager += f'<a href="{next_l["id"]}.html">{next_l["no"]} {html.escape(next_l["zh"])} →</a>' if next_l else "<span></span>"
    pager += "</nav>"
    readings = ""
    if lec.get("readings"):
        readings = '<div class="readings"><b>推荐阅读</b>' + "".join(
            f'<a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a>' for t, u in lec["readings"]
        ) + "</div>"
    hero = f"""<div class="hero">
  <div class="kicker">{html.escape(lec['part'])} · {html.escape(lec['when'])}</div>
  <h1>{html.escape(lec['zh'])}</h1>
  <div class="en">{html.escape(lec['en'])}</div>
  <p class="lead">{html.escape(lec['summary'])}</p>
  {readings}
  <div class="meta">共 {n_imgs} 页 · 原版 PDF：<a href="../../{lec['id']}.pdf">{lec['id']}.pdf</a> · 键盘 ←/→ 或 J/K 翻页</div>
</div>"""
    body = f"""{topbar('../', lec['id'])}
<div class="layout">
  <aside class="toc"><div class="toc-h">本讲目录</div><ol>{''.join(toc)}</ol></aside>
  <main>{hero}{''.join(cards)}{pager}</main>
</div>
<div class="lightbox" hidden><img alt=""></div>"""
    out = os.path.join(ROOT, "lectures", lec["id"] + ".html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page(f"{lec['no']} {lec['zh']} · CS2680", body, "../"))
    return n_imgs, len(missing)


def build_index():
    rows = []
    for lec in LECTURES:
        rows.append(f"""<a class="lec" href="lectures/{lec['id']}.html">
  <div class="no">{lec['no']}</div>
  <div class="info"><div class="t">{html.escape(lec['zh'])}</div><div class="e">{html.escape(lec['en'])}</div>
  <div class="s">{html.escape(lec['summary'])}</div></div>
  <div class="when">{html.escape(lec['when'])}</div>
</a>""")
    part1 = "".join(r for r, l in zip(rows, LECTURES) if l["part"].startswith("第一部分"))
    part2 = "".join(r for r, l in zip(rows, LECTURES) if l["part"].startswith("第二部分"))
    other = "".join(r for r, l in zip(rows, LECTURES) if l["part"].startswith("附"))
    body = f"""{topbar('')}
<main class="home">
{COURSE['intro_html']}
<h2 class="sec">第一部分 · LLM 与智能体入门</h2><div class="lecs">{part1}</div>
<h2 class="sec">第二部分 · 面向 LLM 与智能体的系统</h2><div class="lecs">{part2}</div>
<h2 class="sec">作业讲义</h2><div class="lecs">{other}</div>
{COURSE['tail_html']}
</main>"""
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page("CS2680 现代 AI 系统 · 中文课件", body, ""))


def main():
    total = gaps = 0
    for i, lec in enumerate(LECTURES):
        if not os.path.exists(os.path.join(SRC, lec["id"] + ".md")):
            print(f"  - 跳过 {lec['id']}（尚无翻译）")
            continue
        n, m = build_lecture(i, lec)
        total += n
        gaps += m
        print(f"  ✓ {lec['id']}: {n} 页")
    build_index()
    print(f"完成：{total} 页，缺译 {gaps} 页")


if __name__ == "__main__":
    main()
