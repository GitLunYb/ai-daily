"""微信公众号 collector (RSS,从 wechat2rss 或自建 RSSHub 获取 RSS URL)。

从 ENTITIES_DIR/wechat_accounts.md 读取公众号 RSS URL 列表,抓取全部
(用户配的公众号都是航天相关,不过滤)。公众号 RSS 需自建或第三方服务,
公共 rsshub.app 不支持。
"""

import html
import os
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List

from . import http
from .schema import TrackerItem, Engagement, CollectionResult
from .util import log

SOURCE_WECHAT = "wechat"
_log = lambda msg: log("WeChat", msg, tty_only=True)

DEPTH_LIMITS = {"quick": 10, "default": 25, "deep": 50}
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def _load_rss_urls() -> List[str]:
    d = os.environ.get("ENTITIES_DIR")
    if not d:
        return []
    p = Path(d) / "wechat_accounts.md"
    if not p.exists():
        return []
    urls = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("http"):
            urls.append(line)
    return urls


def _strip_html(text: str) -> str:
    text = html.unescape(text or "")
    return re.sub(r"<[^>]+>", " ", text).strip()


def _parse_date(s: str) -> str:
    if not s:
        return ""
    import datetime
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.datetime.strptime(s[:26], fmt).strftime("%Y-%m-%d")
        except Exception:
            pass
    return s[:10] if len(s) >= 10 else ""


def _parse_rss(xml_text: str) -> List[Dict[str, str]]:
    if not xml_text:
        return []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        _log(f"RSS parse error: {e}")
        return []
    out: List[Dict[str, str]] = []
    for item in root.iter("item"):
        out.append({
            "title": (item.findtext("title") or "").strip(),
            "url": (item.findtext("link") or "").strip(),
            "date": _parse_date((item.findtext("pubDate") or "").strip()),
            "summary": _strip_html((item.findtext("description") or ""))[:300],
            "author": (item.findtext("author") or "").strip(),
        })
    for entry in root.findall("atom:entry", ATOM_NS):
        link_el = entry.find("atom:link", ATOM_NS)
        out.append({
            "title": (entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip(),
            "url": link_el.get("href", "") if link_el is not None else "",
            "date": _parse_date((entry.findtext("atom:published", default="", namespaces=ATOM_NS) or "").strip()),
            "summary": _strip_html(entry.findtext("atom:content", default="", namespaces=ATOM_NS) or "")[:300],
            "author": "",
        })
    return out


def _fetch(url: str) -> List[Dict[str, str]]:
    try:
        body = http.get_text(
            url,
            headers={"Accept": "application/rss+xml, application/xml, text/xml"},
            timeout=20,
            retries=2,
        )
        return _parse_rss(body)
    except Exception as e:
        _log(f"fetch failed {url}: {e}")
        return []


def collect(config, from_date, to_date, depth="default") -> CollectionResult:
    """从 wechat_accounts.md 的 RSS URL 抓公众号文章(不过滤,都是航天相关)。"""
    result = CollectionResult(source=SOURCE_WECHAT)
    urls = _load_rss_urls()
    if not urls:
        _log("无 wechat_accounts.md 或为空,跳过(公众号 RSS 需自建/第三方配置)")
        return result
    limit = DEPTH_LIMITS.get(depth, DEPTH_LIMITS["default"])
    all_items: List[TrackerItem] = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(_fetch, u): u for u in urls}
        for fut in as_completed(futures):
            for i, e in enumerate(fut.result()[:limit]):
                date = e["date"] or None
                if date and (date < from_date or date > to_date):
                    continue
                author = e.get("author") or "微信公众号"
                all_items.append(TrackerItem(
                    id=f"WC-{abs(hash(e['url'])) % 0xffff}-{i}",
                    title=e["title"],
                    summary=e["summary"],
                    entity=author,
                    source=SOURCE_WECHAT,
                    source_url=e["url"],
                    source_label=author,
                    date=date,
                    date_confidence="high" if date else "low",
                    raw_text=e["title"],
                    engagement=Engagement(),
                    relevance=0.7,  # 公众号质量高,给最高权重
                ))
    result.items = all_items
    result.entities_checked = len(urls)
    result.entities_with_updates = 1 if all_items else 0
    _log(f"Collected {len(all_items)} wechat items")
    return result
