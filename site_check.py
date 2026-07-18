#!/usr/bin/env python3
"""
三站自动排查脚本 — 供 GitHub Actions 定时调用
检查 aitool-picks、MintShovels、makerearn.com 三个网站
结果写入 COLLAB.md
"""

import urllib.request
import urllib.error
import re
import json
import os
from datetime import datetime, timezone, timedelta

# ============ 配置 ============
COLLAB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "COLLAB.md")

SITES = {
    "AITool Picks": {
        "url": "https://sun490619.github.io/aitool-picks/",
        "expected": ["AI", "tool", "picks"],
    },
    "MintShovels": {
        "url": "https://mintshovels.com/",
        "expected": ["seo", "audit", "mintshovels"],
    },
    "Maker Earn": {
        "url": "https://makerearn.com/",
        "expected": ["maker", "earn"],
    },
}

# ============ 工具函数 ============
def fetch_url(url, timeout=15):
    """获取网页内容"""
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "CodeBuddy-SiteCheck/1.0 (+https://github.com)",
                "Accept": "text/html,application/xhtml+xml",
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {
                "status": resp.status,
                "content": resp.read().decode("utf-8", errors="ignore"),
                "final_url": resp.url,
            }
    except urllib.error.HTTPError as e:
        return {"status": e.code, "content": "", "error": str(e)}
    except Exception as e:
        return {"status": 0, "content": "", "error": str(e)}


def check_site(name, config):
    """检查单个网站，返回问题列表"""
    issues = []
    result = fetch_url(config["url"])

    # 1. HTTP 状态码
    if result["status"] == 0:
        issues.append(("🔴", "无法访问", result.get("error", "未知错误")))
        return issues
    elif result["status"] >= 500:
        issues.append(("🔴", f"服务器错误 HTTP {result['status']}", ""))
        return issues
    elif result["status"] >= 400:
        issues.append(("🔴", f"客户端错误 HTTP {result['status']}", ""))
        return issues
    elif result["status"] >= 300:
        issues.append(("🟡", f"重定向 HTTP {result['status']} → {result.get('final_url', '')}", ""))

    content = result["content"].lower()

    # 2. 关键内容是否存在
    for keyword in config["expected"]:
        if keyword.lower() not in content:
            issues.append(("🟡", f"页面缺少关键词", f"'{keyword}' 未出现"))

    # 3. HTML 完整性
    if not content.strip().startswith("<!doctype") and not content.strip().startswith("<html"):
        issues.append(("🟠", "页面可能不是完整 HTML", "开头不符合 HTML 规范"))

    if "</html>" not in content[-200:]:
        issues.append(("🟡", "页面可能未完整闭合", "</html> 标签缺失或不在末尾"))

    # 4. 基本 SEO 元素
    if "<title>" not in content or "</title>" not in content:
        issues.append(("🟡", "缺少 <title> 标签", ""))
    if '<meta name="description"' not in content:
        issues.append(("🟡", "缺少 meta description", ""))

    # 5. 内容大小
    size_kb = len(content) / 1024
    if size_kb < 1:
        issues.append(("🔴", "页面内容极少", f"仅 {size_kb:.1f} KB"))
    elif size_kb < 5:
        issues.append(("🟡", "页面内容偏少", f"{size_kb:.1f} KB"))

    # 6. 常见错误
    if "404" in content[:500] and "not found" in content[:500]:
        issues.append(("🔴", "页面显示 404", ""))
    if "error establishing" in content:
        issues.append(("🔴", "数据库连接错误", ""))

    return issues


def update_collab(report_text):
    """将排查结果写入 COLLAB.md"""
    now_beijing = datetime.now(timezone.utc) + timedelta(hours=8)
    timestamp = now_beijing.strftime("%Y-%m-%d %H:%M")

    new_section = f"""### [{timestamp}] 自动排查

{report_text}

---

"""

    try:
        with open(COLLAB_PATH, "r", encoding="utf-8") as f:
            old_content = f.read()
    except FileNotFoundError:
        old_content = "# CodeBuddy ↔ Hermes 协作文件\n\n"

    # 找到"## 排查记录"后的第一个位置插入
    marker = "## 排查记录"
    if marker in old_content:
        insert_pos = old_content.index(marker) + len(marker) + 1
        # 找到下一行
        next_line = old_content.find("\n", insert_pos)
        new_content = old_content[:next_line + 1] + "\n" + new_section + old_content[next_line + 1:]
    else:
        # 如果没有排查记录section，在末尾添加
        new_content = old_content + "\n## 排查记录\n\n" + new_section

    with open(COLLAB_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    print("=" * 60)
    print("🔍 三站自动排查")
    print(f"⏰ 北京时间: {(datetime.now(timezone.utc) + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    all_ok = True
    report_lines = []

    for name, config in SITES.items():
        print(f"\n--- 检查 {name} ({config['url']}) ---")
        issues = check_site(name, config)

        if not issues:
            print(f"  🟢 {name}: 一切正常")
            report_lines.append(f"**🟢 {name}**：一切正常")
        else:
            all_ok = False
            for severity, title, detail in issues:
                line = f"{severity} {title}"
                if detail:
                    line += f" — {detail}"
                print(f"  {line}")
            report_lines.append(f"**{name}**：")
            for severity, title, detail in issues:
                line = f"- {severity} {title}"
                if detail:
                    line += f"：{detail}"
                report_lines.append(line)

    report_text = "\n".join(report_lines)

    if all_ok:
        report_text += "\n\n✅ 三站全部正常。"
    else:
        report_text += "\n\n⚠️ 存在问题，请 Hermes 查看处理。"

    # 写入 COLLAB.md
    update_collab(report_text)

    print("\n" + "=" * 60)
    print("✅ 排查完成，结果已写入 COLLAB.md")
    if not all_ok:
        print("⚠️  存在异常项，请 Hermes 查看")

    return 0 if all_ok else 1


if __name__ == "__main__":
    exit(main())
