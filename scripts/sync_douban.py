#!/usr/bin/env python3
"""
Fetches the latest Douban broadcasts (广播) for L.Revolution
and updates the fn-feed section in content/index.md.

Requires DOUBAN_COOKIE env var (full cookie string from browser devtools).
"""

import os
import re
import ssl
import sys
import time
import urllib.request
from datetime import datetime

# Allow unverified SSL on macOS (system cert store issue)
_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

STATUSES_URL = "https://www.douban.com/people/L.Revolution/statuses"
TOPIC_URL    = "https://www.douban.com/topic/{}/"
INDEX_MD     = "content/index.md"
MAX_ENTRIES  = 3

COOKIE = os.environ.get("DOUBAN_COOKIE", "")
if not COOKIE:
    print("ERROR: DOUBAN_COOKIE env var not set", file=sys.stderr)
    sys.exit(1)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "Cookie": COOKIE,
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.douban.com",
        "Accept-Language": "zh-CN,zh;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as resp:
        return resp.read().decode("utf-8", errors="replace")


def get_topic_ids(html: str) -> list[str]:
    """Extract topic IDs (text broadcasts) from the statuses page."""
    seen = set()
    ids = []
    for m in re.finditer(r'douban\.com/topic/(\d+)', html):
        tid = m.group(1)
        if tid not in seen:
            seen.add(tid)
            ids.append(tid)
    return ids[:MAX_ENTRIES]


def get_topic_content(topic_id: str) -> dict | None:
    try:
        html = fetch(TOPIC_URL.format(topic_id))
    except Exception as e:
        print(f"  WARNING: failed to fetch topic {topic_id}: {e}", file=sys.stderr)
        return None

    date_m = re.search(r'<span class="create-time">([^<]+)</span>', html)
    # Grab ALL paragraphs from the broadcast content
    texts = re.findall(r'<p data-align[^>]*>(.*?)</p>', html, re.DOTALL)

    if not texts:
        return None

    full_text = "\n".join(
        re.sub(r'<[^>]+>', '', t).strip()
        for t in texts
        if re.sub(r'<[^>]+>', '', t).strip()
    )

    date_str = ""
    if date_m:
        try:
            dt = datetime.strptime(date_m.group(1).strip(), "%Y-%m-%d %H:%M:%S")
            date_str = dt.strftime("%Y · %m · %d")
        except ValueError:
            date_str = date_m.group(1).strip()[:10]

    return {"text": full_text, "date": date_str}


def build_feed_html(entries: list[dict]) -> str:
    parts = []
    for entry in entries:
        text = entry["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        date = entry["date"]
        parts.append(
            f'<div class="fn-entry">\n'
            f'<p class="fn-entry-text">{text}</p>\n'
            f'<span class="fn-entry-date">{date}</span>\n'
            f'</div>'
        )
    return "\n".join(parts)


def update_index(entries: list[dict]) -> bool:
    with open(INDEX_MD, "r", encoding="utf-8") as f:
        content = f.read()

    new_feed = build_feed_html(entries)

    pattern = r'(<div class="fn-feed">)\n.*?(</div>\n</div>\n<!-- Hand-drawn tail)'
    replacement = r'\1\n' + new_feed + r'\n\2'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        print("ERROR: could not find fn-feed section in index.md", file=sys.stderr)
        return False

    if new_content == content:
        print("No changes — feed already up to date.")
        return True

    with open(INDEX_MD, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated {len(entries)} entries in {INDEX_MD}")
    return True


def main():
    print(f"Fetching statuses page …")
    try:
        statuses_html = fetch(STATUSES_URL)
    except Exception as e:
        print(f"ERROR fetching statuses page: {e}", file=sys.stderr)
        sys.exit(1)

    topic_ids = get_topic_ids(statuses_html)
    if not topic_ids:
        print("No broadcast topics found on statuses page.", file=sys.stderr)
        sys.exit(1)

    print(f"Found topic IDs: {topic_ids}")

    entries = []
    for tid in topic_ids:
        print(f"  Fetching topic {tid} …")
        entry = get_topic_content(tid)
        if entry:
            print(f"    [{entry['date']}] {entry['text'][:60]} …")
            entries.append(entry)
        time.sleep(0.8)   # be polite

    if not entries:
        print("ERROR: no entries extracted.", file=sys.stderr)
        sys.exit(1)

    if not update_index(entries):
        sys.exit(1)


if __name__ == "__main__":
    main()
