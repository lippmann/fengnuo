#!/usr/bin/env python3
"""
Fetches the latest Douban broadcasts (广播) for L.Revolution
and updates the fn-feed section in content/index.md.
"""

import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

DOUBAN_RSS = "https://www.douban.com/feed/people/L.Revolution/miniblog"
INDEX_MD = "content/index.md"
MAX_ENTRIES = 3

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml, text/xml",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def fetch_rss(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()


def parse_entries(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    entries = []

    # Try Atom format first (豆瓣通常返回 Atom)
    for entry in root.findall("atom:entry", ns)[:MAX_ENTRIES]:
        title_el = entry.find("atom:title", ns)
        published_el = entry.find("atom:published", ns)
        summary_el = entry.find("atom:summary", ns)
        content_el = entry.find("atom:content", ns)

        text = ""
        if content_el is not None and content_el.text:
            # Strip any HTML tags from content
            text = re.sub(r"<[^>]+>", "", content_el.text).strip()
        elif summary_el is not None and summary_el.text:
            text = re.sub(r"<[^>]+>", "", summary_el.text).strip()
        elif title_el is not None and title_el.text:
            text = title_el.text.strip()

        if not text:
            continue

        date_str = ""
        if published_el is not None and published_el.text:
            try:
                dt = datetime.fromisoformat(
                    published_el.text.replace("Z", "+00:00")
                )
                date_str = dt.strftime("%Y · %m · %d")
            except ValueError:
                date_str = published_el.text[:10]

        entries.append({"text": text, "date": date_str})

    if entries:
        return entries

    # Fallback: RSS 2.0 format
    channel = root.find("channel")
    if channel is None:
        return entries

    for item in channel.findall("item")[:MAX_ENTRIES]:
        title_el = item.find("title")
        desc_el = item.find("description")
        pubdate_el = item.find("pubDate")

        text = ""
        if desc_el is not None and desc_el.text:
            text = re.sub(r"<[^>]+>", "", desc_el.text).strip()
        elif title_el is not None and title_el.text:
            text = title_el.text.strip()

        if not text:
            continue

        date_str = ""
        if pubdate_el is not None and pubdate_el.text:
            try:
                from email.utils import parsedate_to_datetime
                dt = parsedate_to_datetime(pubdate_el.text)
                date_str = dt.strftime("%Y · %m · %d")
            except Exception:
                date_str = pubdate_el.text[:10]

        entries.append({"text": text, "date": date_str})

    return entries


def build_feed_html(entries: list[dict]) -> str:
    parts = []
    for i, entry in enumerate(entries):
        text = entry["text"].replace("<", "&lt;").replace(">", "&gt;")
        date = entry["date"]
        padding_top = "" if i == 0 else ""
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

    # Replace everything between <div class="fn-feed"> and </div> (the feed container)
    pattern = r'(<div class="fn-feed">)\n.*?(</div>\n</div>\n<!-- Hand-drawn tail)'
    replacement = r'\1\n' + new_feed + r'\n\2'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        print("ERROR: Could not find fn-feed section in index.md", file=sys.stderr)
        return False

    if new_content == content:
        print("No changes — feed is already up to date.")
        return True

    with open(INDEX_MD, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated {len(entries)} entries in {INDEX_MD}")
    return True


def main():
    print(f"Fetching {DOUBAN_RSS} ...")
    try:
        xml_bytes = fetch_rss(DOUBAN_RSS)
    except Exception as e:
        print(f"ERROR fetching RSS: {e}", file=sys.stderr)
        sys.exit(1)

    entries = parse_entries(xml_bytes)
    if not entries:
        print("No entries found in RSS feed.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(entries)} entries.")
    for e in entries:
        print(f"  [{e['date']}] {e['text'][:60]}...")

    if not update_index(entries):
        sys.exit(1)


if __name__ == "__main__":
    main()
