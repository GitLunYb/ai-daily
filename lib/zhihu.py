"""知乎 collector for morning-ai (RSSHub RSS, public instance).

从 ENTITIES_DIR/zhihu_topics.md 读取 RSS URL 列表,抓取后用航天关键词
过滤,只保留航天相关条目。
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

SOURCE_ZHIHU = "zhihu"
_log = lambda msg: log("Zhihu", msg, tty_only=True)

# 航天关键词过滤(标题/摘要含任一即保留)
SPACE_KEYWORDS = [
    "航天", "火箭", "卫星", "星座", "发射", "空间站", "探月", "探火", "深空",
    "星链", "SpaceX", "蓝箭", "星际荣耀", "星河动力", "天兵", "银河航天",
    "长光卫星", "反卫星", "空间对抗", "空间态势", "太空军", "太空安全",
    "姿态控制", "轨道控制", "GNC", "轨道", "航天器", "载人航天", "导航",
    "moon", "mars", "rocket", "satellite", "constellation", "launch",
    "aerospace", "starlink", "space force", "space domain",
]

DEPTH_LIMITS = {"quick": 10, "default": 25, "deep": 50}
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def _is_space_related(text: str) -> bool:
    if not text:
        return False
    low = text.lower()
    return any(kw.lower() in low for kw in SPACE_KEYWORDS)


def _load_rss_urls() -> List[str]:
    """从 ENTITIES_DIR/zhihu_topics.md 读取 RSS URL 列表。"""
    d = os.environ.get("ENTITIES_DIR")
    if not d:
        return []
    p = Path(d) / "zhihu_topics.md"
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
    """RFC822 / ISO 日期 -> YYYY-MM-DD。"""
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
    """解析 RSS 2.0 / Atom,返回 [{title, url, date, summary}]。"""
    if not xml_text:
        return []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        _log(f"RSS parse error: {e}")
        return []
    out: List[Dict[str, str]] = []
    # RSS 2.0: channel/item
    for item in root.iter("item"):
        out.append({
            "title": (item.findtext("title") or "").strip(),
            "url": (item.findtext("link") or "").strip(),
            "date": _parse_date((item.findtext("pubDate") or "").strip()),
            "summary": _strip_html((item.findtext("description") or ""))[:300],
        })
    # Atom: entry
    for entry in root.findall("atom:entry", ATOM_NS):
        link_el = entry.find("atom:link", ATOM_NS)
        out.append({
            "title": (entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip(),
            "url": link_el.get("href", "") if link_el is not None else "",
            "date": _parse_date((entry.findtext("atom:published", default="", namespaces=ATOM_NS) or "").strip()),
            "summary": _strip_html(entry.findtext("atom:content", default="", namespaces=ATOM_NS) or "")[:300],
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
    """从 zhihu_topics.md 的 RSS URL 抓知乎内容,过滤航天相关。"""
    result = CollectionResult(source=SOURCE_ZHIHU)
    urls = _load_rss_urls()
    if not urls:
        _log("无 zhihu_topics.md 或为空,跳过")
        return result
    limit = DEPTH_LIMITS.get(depth, DEPTH_LIMITS["default"])
    all_items: List[TrackerItem] = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(_fetch, u): u for u in urls}
        for fut in as_completed(futures):
            for i, e in enumerate(fut.result()[:limit]):
                if not _is_space_related(e["title"] + " " + e["summary"]):
                    continue
                date = e["date"] or None
                if date and (date < from_date or date > to_date):
                    continue
                all_items.append(TrackerItem(
                    id=f"ZH-{abs(hash(e['url'])) % 0xffff}-{i}",
                    title=e["title"],
                    summary=e["summary"],
                    entity="知乎",
                    source=SOURCE_ZHIHU,
                    source_url=e["url"],
                    source_label="知乎",
                    date=date,
                    date_confidence="high" if date else "low",
                    raw_text=e["title"],
                    engagement=Engagement(),
                    relevance=0.6,  # 知乎质量高,给较高权重
                ))
    result.items = all_items
    result.entities_checked = len(urls)
    result.entities_with_updates = 1 if all_items else 0
    _log(f"Collected {len(all_items)} zhihu items")
    return result
