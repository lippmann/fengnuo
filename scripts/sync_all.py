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


PLATFORM_ICONS = {
    "twitter": (
        "says-platform-twitter",
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231'
        '-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25z'
        'm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/>'
        '</svg>'
    ),
    "douban": (
        "says-platform-douban",
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<rect x="3" y="3" width="18" height="3" rx="1"/>'
        '<rect x="5" y="8" width="14" height="10" rx="1"/>'
        '<rect x="8" y="20" width="3" height="1" rx="0.5"/>'
        '<rect x="13" y="20" width="3" height="1" rx="0.5"/>'
        '<rect x="10" y="18" width="4" height="3" rx="0.5"/>'
        '</svg>'
    ),
    "weread": (
        "says-platform-weread",
        '<svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">'
        '<path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h10v2H4z"/>'
        '</svg>'
    ),
}


def _home_entry_html(post: dict) -> str:
    """Render a single post as a .says-entry for the homepage."""
    platform = post.get("platform", "twitter")
    url      = post.get("url", "#")
    date     = _fmt_date(post.get("date", ""))
    text     = post.get("text", "")
    # Truncate long text on homepage
    if len(text) > 200:
        text = text[:200] + "…"
    text_esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    css_class, svg = PLATFORM_ICONS.get(platform, PLATFORM_ICONS["twitter"])

    images_html = ""
    for img in post.get("images", [])[:1]:   # max 1 image on homepage
        images_html += f'\n  <div class="says-images"><img src="{img}" loading="lazy" alt=""></div>'

    return (
        f'<div class="says-entry">\n'
        f'  <div class="says-header">\n'
        f'    <a class="says-platform {css_class}" href="{url}" target="_blank">{svg}</a>\n'
        f'    <span class="says-date">{date}</span>\n'
        f'  </div>\n'
        f'  <p class="says-text">{text_esc}</p>'
        f'{images_html}\n'
        f'</div>'
    )


def _entry_html(post: dict, show_full: bool = False) -> str:
    """Render a single post as a .fn-entry for the says archive page."""
    text = post.get("text", "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if not show_full and len(text) > 200:
        text = text[:200] + "…"
    date = _fmt_date(post.get("date", ""))
    logo = _logo_html(post["platform"], post["url"])
    images = _images_html(post.get("images", []))
    return (
        f'<div class="fn-entry">\n'
        f'<div class="fn-entry-header">{logo}'
        f'<span class="fn-entry-date">{date}</span></div>\n'
        f'<p class="fn-entry-text">{text}</p>\n'
        f'{images}'
        f'</div>'
    )


# ── Index.md update ─────────────────────────────────────────────────────────

def update_index(posts: list[dict]):
    content = INDEX_MD.read_text(encoding="utf-8")
    top = posts[:HOME_MAX]
    entries_html = "\n\n".join(_home_entry_html(p) for p in top)

    new_content, n = re.subn(
        r'<!-- SAYS_START -->.*?<!-- SAYS_END -->',
        f'<!-- SAYS_START -->\n{entries_html}\n<!-- SAYS_END -->',
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
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;900&family=IBM+Plex+Mono:wght@300;400&display=swap" rel="stylesheet">

<style>
.sy-wrap {{ font-family:'IBM Plex Mono',monospace; color:#1A1814; padding:0 0 80px; }}
.sy-header {{ margin-bottom:48px; padding-bottom:20px; border-bottom:1px solid #E0D8CE; }}
.sy-eyebrow {{ font-size:10px; letter-spacing:0.2em; color:#C0B8AE; font-weight:300; margin:0 0 10px; }}
.sy-eyebrow em {{ font-style:normal; color:#8B4A3C; }}
.sy-title {{ font-family:'Noto Serif SC',serif; font-size:26px; font-weight:900; color:#1E1A17; margin:0; letter-spacing:0.06em; }}
.sy-feed {{ display:flex; flex-direction:column; gap:0; }}
.fn-entry {{ padding:24px 0; border-bottom:1px solid #E8E0D6; display:flex; flex-direction:column; gap:10px; }}
.fn-entry:last-child {{ border-bottom:none; }}
.fn-entry-header {{ display:flex; align-items:center; justify-content:space-between; gap:10px; }}
.fn-logo {{ width:22px; height:22px; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; flex-shrink:0; text-decoration:none; transition:opacity 0.15s; color:#fff; }}
.fn-logo:hover {{ opacity:0.75; }}
.fn-entry-date {{ font-size:9px; color:#B8B0A8; letter-spacing:0.16em; font-weight:300; }}
.fn-entry-text {{ font-family:'Noto Serif SC',serif; font-size:14px; font-weight:300; line-height:2; color:#1A1814; letter-spacing:0.04em; white-space:pre-wrap; }}
.fn-entry-images {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:8px; }}
.fn-entry-images img {{ max-width:240px; max-height:240px; object-fit:cover; border-radius:2px; }}
.sy-filter {{ display:flex; gap:16px; margin-bottom:32px; flex-wrap:wrap; }}
.sy-filter-btn {{ font-size:10px; letter-spacing:0.14em; color:#B8B0A8; text-decoration:none; padding:4px 0; border-bottom:1px solid transparent; transition:color 0.15s, border-color 0.15s; }}
.sy-filter-btn:hover {{ color:#8B4A3C; border-color:#8B4A3C; }}
</style>

<div class="sy-wrap">
<div class="sy-header">
<p class="sy-eyebrow"><em>~/</em>says</p>
<h1 class="sy-title">碎的念</h1>
</div>
<div class="sy-filter">
<span style="font-size:10px;letter-spacing:0.14em;color:#6B6560;font-weight:300">{post_count} 条记录</span>
</div>
<div class="sy-feed">
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
