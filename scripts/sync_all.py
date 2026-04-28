#!/usr/bin/env python3
"""
Master sync + render script.

Syncs Douban, X, Threads, Instagram → merges into content/says/feed.json
Then renders:
  • content/index.md        (latest 5 posts, fn-feed section)
  • content/says/index.md   (full archive)

Required env vars:
  DOUBAN_COOKIE    — full browser cookie string for douban.com
  THREADS_TOKEN    — (optional) Meta Threads API long-lived token
  INSTAGRAM_TOKEN  — (optional) Meta Instagram Graph API token
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT      = Path(__file__).parent.parent
FEED_FILE = ROOT / "content/says/feed.json"
INDEX_MD  = ROOT / "content/index.md"
SAYS_MD   = ROOT / "content/says/index.md"

HOME_MAX  = 5   # posts shown on homepage

# ── Platform logos (inline SVG) ────────────────────────────────────────────

LOGOS = {
    "douban": (
        '#07A761',
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<rect x="3" y="3" width="18" height="3" rx="1"/>'
        '<rect x="5" y="8" width="14" height="10" rx="1"/>'
        '<rect x="8" y="20" width="3" height="1" rx="0.5"/>'
        '<rect x="13" y="20" width="3" height="1" rx="0.5"/>'
        '<rect x="10" y="18" width="4" height="3" rx="0.5"/>'
        '</svg>'
    ),
    "twitter": (
        '#000000',
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231'
        '-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25z'
        'm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/>'
        '</svg>'
    ),
    "threads": (
        '#000000',
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<path d="M12.186 24h-.007c-3.581-.024-6.334-1.205-8.184-3.509C2.35 18.44'
        ' 1.5 15.586 1.5 12.068V12c0-3.368.829-6.108 2.465-8.14C5.684 1.707'
        ' 8.428.5 11.993.5h.014c2.955.02 5.338 1.053 6.885 2.994 1.495 1.878'
        ' 2.274 4.638 2.316 8.206l.002.3v.432c0 3.503-.765 6.15-2.273 7.871'
        '-1.446 1.651-3.645 2.632-6.751 2.697zM12 2.5c-3.09 0-5.386 1.007'
        '-6.819 2.993C4.047 6.975 3.5 9.215 3.5 12c0 3.103.757 5.68 2.25 7.547'
        ' 1.434 1.794 3.69 2.93 6.743 2.953 2.698-.055 4.5-.838 5.67-2.188'
        ' 1.234-1.41 1.837-3.668 1.837-6.812V13c-.04-3.17-.764-5.614-2.099'
        '-7.213C16.582 3.998 14.617 3.145 12 2.5z"/>'
        '</svg>'
    ),
    "instagram": (
        'url(#ig-grad)',
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<defs><linearGradient id="ig-grad" x1="0%" y1="100%" x2="100%" y2="0%">'
        '<stop offset="0%" style="stop-color:#f09433"/>'
        '<stop offset="25%" style="stop-color:#e6683c"/>'
        '<stop offset="50%" style="stop-color:#dc2743"/>'
        '<stop offset="75%" style="stop-color:#cc2366"/>'
        '<stop offset="100%" style="stop-color:#bc1888"/>'
        '</linearGradient></defs>'
        '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691'
        ' 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069'
        ' 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07'
        '-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058'
        '-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227'
        ' 1.664-4.771 4.919-4.919C8.333.014 8.741 0 12 0zm0 5.838a6.162 6.162'
        ' 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010'
        ' 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>'
        '</svg>'
    ),
    "weread": (
        '#1A7E4A',
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<path d="M17.5 6.5C17.5 4.57 15.93 3 14 3s-3.5 1.57-3.5 3.5c0 .88.32 1.68.85 2.3'
        'C9.91 9.38 9 10.84 9 12.5c0 2.49 2.01 4.5 4.5 4.5s4.5-2.01 4.5-4.5'
        'c0-1.66-.91-3.12-2.35-3.7.53-.62.85-1.42.85-2.3z'
        'M14 5c.83 0 1.5.67 1.5 1.5S14.83 8 14 8s-1.5-.67-1.5-1.5S13.17 5 14 5z'
        'M13.5 15c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>'
        '<path d="M6.5 8C5.12 8 4 9.12 4 10.5S5.12 13 6.5 13 9 11.88 9 10.5 7.88 8 6.5 8z'
        'M6.5 11C6.22 11 6 10.78 6 10.5S6.22 10 6.5 10s.5.22.5.5-.22.5-.5.5z"/>'
        '</svg>'
    ),
}


# ── Feed data helpers ───────────────────────────────────────────────────────

def load_feed() -> list[dict]:
    if FEED_FILE.exists():
        return json.loads(FEED_FILE.read_text())
    return []


def save_feed(posts: list[dict]):
    FEED_FILE.parent.mkdir(parents=True, exist_ok=True)
    FEED_FILE.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def merge(existing: list[dict], new_posts: list[dict]) -> list[dict]:
    by_id = {p["id"]: p for p in existing}
    for p in new_posts:
        by_id[p["id"]] = p   # overwrite with fresh data
    all_posts = list(by_id.values())
    all_posts.sort(key=lambda p: p.get("timestamp", 0), reverse=True)
    return all_posts


# ── HTML rendering ──────────────────────────────────────────────────────────

def _fmt_date(date_str: str) -> str:
    """'2026-04-10' → '2026 · 04 · 10'"""
    parts = date_str.split("-")
    return " · ".join(parts) if len(parts) == 3 else date_str


def _logo_html(platform: str, url: str) -> str:
    color, svg = LOGOS.get(platform, ('#888', '<svg viewBox="0 0 24 24" width="12" height="12"></svg>'))
    is_grad = color.startswith("url(")
    bg = f'background:{color}' if not is_grad else 'background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)'
    return (
        f'<a class="fn-logo fn-logo-{platform}" href="{url}" '
        f'target="_blank" title="{platform}" style="{bg}">{svg}</a>'
    )


def _images_html(images: list[str]) -> str:
    if not images:
        return ""
    imgs = "".join(
        f'<img src="{img}" loading="lazy" alt="">'
        for img in images
    )
    return f'<div class="fn-entry-images">{imgs}</div>'


def _dot_svg(platform: str, size: int = 10) -> str:
    """Return the inner SVG for a platform's timeline dot."""
    svgs = {
        "twitter": (
            f'<svg viewBox="0 0 24 24" fill="currentColor" width="{size}" height="{size}">'
            '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231'
            '-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25z'
            'm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg>'
        ),
        "douban": (
            f'<svg viewBox="0 0 24 24" fill="currentColor" width="{size}" height="{size}">'
            '<rect x="3" y="3" width="18" height="3" rx="1"/>'
            '<rect x="5" y="8" width="14" height="10" rx="1"/>'
            '<rect x="8" y="20" width="3" height="1" rx="0.5"/>'
            '<rect x="13" y="20" width="3" height="1" rx="0.5"/>'
            '<rect x="10" y="18" width="4" height="3" rx="0.5"/></svg>'
        ),
        "threads": (
            f'<svg viewBox="0 0 24 24" fill="currentColor" width="{size}" height="{size}">'
            '<path d="M12.186 24h-.007c-3.581-.024-6.334-1.205-8.184-3.509C2.35 18.44'
            ' 1.5 15.586 1.5 12.068V12c0-3.368.829-6.108 2.465-8.14C5.684 1.707'
            ' 8.428.5 11.993.5h.014c2.955.02 5.338 1.053 6.885 2.994 1.495 1.878'
            ' 2.274 4.638 2.316 8.206l.002.3v.432c0 3.503-.765 6.15-2.273 7.871'
            '-1.446 1.651-3.645 2.632-6.751 2.697z"/></svg>'
        ),
        "instagram": (
            f'<svg viewBox="0 0 24 24" fill="currentColor" width="{size}" height="{size}">'
            '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691'
            ' 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069'
            ' 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07'
            '-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058'
            '-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227'
            ' 1.664-4.771 4.919-4.919C8.333.014 8.741 0 12 0zm0 5.838a6.162 6.162'
            ' 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010'
            ' 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>'
        ),
        "weread": (
            f'<svg viewBox="0 0 24 24" fill="currentColor" width="{size}" height="{size}">'
            '<path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h10v2H4z"/></svg>'
        ),
    }
    return svgs.get(platform, svgs["twitter"])


def _vb_entry_html(post: dict, truncate: int = 0) -> str:
    """Render a single post as a .vb-entry (timeline style)."""
    platform = post.get("platform", "twitter")
    url      = post.get("url", "#")
    date     = _fmt_date(post.get("date", ""))
    text     = post.get("text", "")
    if truncate and len(text) > truncate:
        text = text[:truncate] + "…"
    text_esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    svg = _dot_svg(platform, size=10)
    max_imgs = 2 if truncate else 4
    imgs = "".join(
        f'<img src="{img}" loading="lazy" alt="">'
        for img in post.get("images", [])[:max_imgs]
    )
    images_html = f'<div class="vb-images">{imgs}</div>' if imgs else ""

    return (
        f'<div class="vb-entry">'
        f'<div class="vb-spine">'
        f'<a class="vb-dot vb-dot-{platform}" href="{url}" target="_blank" title="{platform}">{svg}</a>'
        f'<div class="vb-line"></div>'
        f'</div>'
        f'<div class="vb-content">'
        f'<p class="vb-date">{date}</p>'
        f'<p class="vb-text">{text_esc}</p>'
        f'{images_html}'
        f'</div>'
        f'</div>'
    )


def _home_entry_html(post: dict) -> str:
    return _vb_entry_html(post, truncate=200)


def _entry_html(post: dict, show_full: bool = False) -> str:
    return _vb_entry_html(post, truncate=0 if show_full else 200)


# ── Index.md update ─────────────────────────────────────────────────────────

def update_index(posts: list[dict]):
    content = INDEX_MD.read_text(encoding="utf-8")
    top = posts[:HOME_MAX]
    entries_html = "\n".join(_home_entry_html(p) for p in top)
    feed_block = f'<div class="vb-feed">\n{entries_html}\n</div>'

    new_content, n = re.subn(
        r'<!-- SAYS_START -->.*?<!-- SAYS_END -->',
        f'<!-- SAYS_START -->\n{feed_block}\n<!-- SAYS_END -->',
        content,
        flags=re.DOTALL,
    )
    if n == 0:
        print("WARNING: could not find <!-- SAYS_START/END --> markers in index.md")
        return

    INDEX_MD.write_text(new_content, encoding="utf-8")
    print(f"[render] index.md updated with {len(top)} posts")


# ── Says/index.md generation ────────────────────────────────────────────────

SAYS_TEMPLATE = """\
---
title: 碎的念
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;900&family=IBM+Plex+Mono:ital,wght@0,300;0,400&display=swap" rel="stylesheet">

<style>
:root {{
  --c-text:#09090b; --c-muted:#71717a; --c-border:#e4e4e7; --c-hover:#f4f4f5;
}}
.sy-wrap {{ font-family:'IBM Plex Mono',monospace; color:var(--c-text); padding:0 0 80px; max-width:640px; }}
.sy-header {{ margin-bottom:48px; padding-bottom:20px; border-bottom:1px solid var(--c-border); }}
.sy-eyebrow {{ font-size:10px; letter-spacing:0.2em; color:var(--c-muted); font-weight:300; margin:0 0 10px; }}
.sy-eyebrow em {{ font-style:normal; }}
.sy-title {{ font-family:'Noto Serif SC',serif; font-size:26px; font-weight:900; color:var(--c-text); margin:0; }}
.sy-count {{ font-size:10px; letter-spacing:0.14em; color:var(--c-muted); font-weight:300; margin-bottom:32px; }}
.vb-feed {{ display:flex; flex-direction:column; }}
.vb-entry {{ display:grid; grid-template-columns:28px 1fr; gap:0 12px; padding:0 0 22px; }}
.vb-entry:last-child {{ padding-bottom:0; }}
.vb-spine {{ display:flex; flex-direction:column; align-items:center; }}
.vb-dot {{ width:26px; height:26px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex-shrink:0; text-decoration:none; color:#fff; margin-top:2px; transition:opacity 0.15s,transform 0.15s; }}
.vb-dot:hover {{ opacity:0.8; transform:scale(1.08); }}
.vb-dot-twitter  {{ background:#09090b; }}
.vb-dot-douban   {{ background:#07A761; }}
.vb-dot-threads  {{ background:#09090b; }}
.vb-dot-weread   {{ background:#1A7E4A; }}
.vb-dot-instagram {{ background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888); }}
.vb-line {{ width:1px; background:var(--c-border); flex:1; margin-top:6px; min-height:10px; }}
.vb-entry:last-child .vb-line {{ display:none; }}
.vb-content {{ padding-top:3px; }}
.vb-date {{ font-size:9px; color:var(--c-muted); letter-spacing:0.06em; font-weight:300; margin-bottom:7px; }}
.vb-text {{ font-family:'Noto Serif SC',serif; font-size:14px; font-weight:300; line-height:2; color:var(--c-text); white-space:pre-wrap; }}
.vb-images {{ display:flex; flex-wrap:wrap; gap:7px; margin-top:10px; }}
.vb-images img {{ width:120px; height:120px; object-fit:cover; border-radius:2px; }}
</style>

<div class="sy-wrap">
<div class="sy-header">
<p class="sy-eyebrow"><em>~/</em>says</p>
<h1 class="sy-title">碎的念</h1>
</div>
<p class="sy-count">{post_count} 条记录</p>
<div class="vb-feed">
{entries}
</div>
</div>
"""


def update_says(posts: list[dict]):
    entries = "\n".join(_entry_html(p, show_full=True) for p in posts)
    content = SAYS_TEMPLATE.format(
        post_count=len(posts),
        entries=entries,
    )
    SAYS_MD.parent.mkdir(parents=True, exist_ok=True)
    SAYS_MD.write_text(content, encoding="utf-8")
    print(f"[render] says/index.md updated with {len(posts)} posts")


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    feed = load_feed()
    new_posts: list[dict] = []

    # Douban
    douban_cookie = os.environ.get("DOUBAN_COOKIE", "")
    if douban_cookie:
        from sync_douban import fetch_posts as fetch_douban
        new_posts.extend(fetch_douban(douban_cookie))
    else:
        print("[douban] DOUBAN_COOKIE not set — skipping")

    # X / Twitter
    from sync_twitter import fetch_posts as fetch_twitter
    new_posts.extend(fetch_twitter())

    # Threads
    from sync_threads import fetch_posts as fetch_threads
    new_posts.extend(fetch_threads())

    # Instagram
    from sync_instagram import fetch_posts as fetch_instagram
    new_posts.extend(fetch_instagram())

    # WeChat Reading (微信读书) highlights
    weread_cookie = os.environ.get("WEREAD_COOKIE", "")
    if weread_cookie:
        from weread_sync import fetch_posts as fetch_weread
        new_posts.extend(fetch_weread(weread_cookie))
    else:
        print("[weread] WEREAD_COOKIE not set — skipping")

    if new_posts:
        feed = merge(feed, new_posts)
        save_feed(feed)
        print(f"[feed] total {len(feed)} posts saved")
    else:
        print("[feed] no new posts, using existing feed")

    if not feed:
        print("ERROR: feed is empty", file=sys.stderr)
        sys.exit(1)

    update_index(feed)
    update_says(feed)


if __name__ == "__main__":
    main()
