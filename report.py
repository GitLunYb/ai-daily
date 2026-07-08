#!/usr/bin/env python3
"""把 collect.py 的 JSON 数据用 DeepSeek 生成中文 Markdown 日报。

用法: python report.py [data.json]
- 优先调 DeepSeek API 生成智能报告
- API 不可用 / 失败则规则化兜底
- 输出到 reports/report_YYYY-MM-DD.md
"""
import json
import os
import sys
import datetime
from pathlib import Path


def rule_based_report(data, date_str):
    items = data.get("items", [])
    stats = data.get("stats", {})
    by_source = stats.get("by_source", {})
    src_summary = "、".join(f"{k}:{v.get('items', 0)}" for k, v in by_source.items())
    lines = [
        f"# AI 日报 — {date_str}",
        "",
        f"> 共 {len(items)} 条 · 来源 {src_summary}",
        "",
    ]

    def imp(it):
        return it.get("importance") or 0

    high = sorted([it for it in items if imp(it) >= 7], key=lambda x: -imp(x))
    mid = sorted([it for it in items if 5 <= imp(it) < 7], key=lambda x: -imp(x))
    low = sorted([it for it in items if imp(it) < 5], key=lambda x: -imp(x))

    def fmt(it):
        title = it.get("title") or it.get("entity") or "无标题"
        url = it.get("source_url") or it.get("url") or ""
        link = f"[{title}]({url})" if url else title
        sm = it.get("summary") or ""
        sm = f" — {sm[:60]}" if sm else ""
        return f"- **[{imp(it)}]** {link} `{it.get('source', '')}`{sm}"

    for title, group in [("重点(7+)", high), ("重要(5-7)", mid), ("常规(<5)", low)]:
        if group:
            lines.append(f"## {title}")
            lines += [fmt(it) for it in group]
            lines.append("")
    lines.append("---")
    lines.append("*规则化兜底生成(LLM 未调用或失败)*")
    return "\n".join(lines)


def llm_report(data, date_str):
    try:
        from openai import OpenAI
    except ImportError:
        return None
    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        return None
    items = data.get("items", [])
    today = date_str
    brief = []
    for it in items:
        eng = it.get("engagement") or {}
        brief.append({
            "id": it.get("id"),
            "title": it.get("title"),
            "summary": it.get("summary"),
            "source": it.get("source"),
            "entity": it.get("entity"),
            "type": it.get("content_type"),
            "score": it.get("importance"),
            "stars": eng.get("stars"),
            "date": it.get("date"),
            "url": it.get("source_url") or it.get("url"),
            "verified": it.get("verified"),
        })
    prompt = (
        f"你是资深 AI 技术编辑。根据下面 {date_str} 收集的 AI 动态数据(JSON)写一份中文 Markdown 日报。\n"
        f"今天日期是 {today},数据里每条有 date、stars 等字段。\n"
        "写作要求:\n"
        "1. **TL;DR**:5 条今日重点,每条一句话点出最值得关注的事。\n"
        "2. **每个项目**:名称 + 一句话简介(基于 summary;**summary 为空时只基于标题写一句并标「(信息有限)」,绝不编造细节**)+ 评分 + 简评。\n"
        "3. **星数显示**:项目标题后用 `⭐数字` 标出 stars(有就标,没有不标)。高星(>1000)或高分(≥8)的项目在简介后加一段深入讲(技术亮点、意义)。\n"
        "4. **今日精讲**:综合【评分+星数+创新性+实用性】选 1 个最有未来潜力的(不必最高分,而是最有潜力),单独一节深入分析:是什么、技术亮点、解决什么问题、未来潜力、潜在风险、与同类对比。\n"
        "5. **日期标注**:date 等于今天标 🆕;不是今天标实际日期,区分今日新增 vs 近几天累积。\n"
        "6. 按 Product / Model / Benchmark / Funding 分类组织(没内容的分类省略)。\n"
        "7. 语言专业简洁,严格基于数据,不编造。每条附链接。\n"
        "数据:\n" + json.dumps(brief, ensure_ascii=False)
    )
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000,
        timeout=180,
    )
    return resp.choices[0].message.content


def main():
    data_path = sys.argv[1] if len(sys.argv) > 1 else "data.json"
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    date_str = data.get("date") or datetime.date.today().isoformat()

    report = None
    try:
        report = llm_report(data, date_str)
    except Exception as e:
        print(f"[report] LLM 调用失败,规则化兜底: {e}", file=sys.stderr)
    if not report:
        report = rule_based_report(data, date_str)

    out_dir = Path("reports")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"report_{date_str}.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"[report] 报告已生成: {out_path}")


if __name__ == "__main__":
    main()
