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
        url = it.get("url") or ""
        link = f"[{title}]({url})" if url else title
        return f"- **[{imp(it)}]** {link} `{it.get('source', '')}`"

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
    brief = [
        {
            "id": it.get("id"),
            "title": it.get("title"),
            "source": it.get("source"),
            "entity": it.get("entity"),
            "score": it.get("importance"),
            "url": it.get("url"),
        }
        for it in items
    ]
    prompt = (
        f"你是 AI 资讯编辑。根据下面 {date_str} 收集的 AI 动态数据(JSON),"
        "生成一份中文 Markdown 日报:先 TLDR(分数 7+ 的重点 3-5 条),"
        "再按 Product/Model/Benchmark/Funding 分类列出其余,每条带分数和链接。语言简洁。\n"
        "数据:\n" + json.dumps(brief, ensure_ascii=False)
    )
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=2500,
        timeout=120,
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
