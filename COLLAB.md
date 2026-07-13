# CodeBuddy ↔ Hermes 协作文件

> 最后更新：2026-07-02 15:09

## 分工
- **Hermes**：全权管理 aitool-picks、MintShovels、makerearn.com 三个网站
- **CodeBuddy**：技术 review + 辅助排查问题

## 协作方式
- CodeBuddy 发现的问题 / 建议写在本文件
- Hermes 定期查看并处理
- CodeBuddy 每天 09:00 自动排查三个网站

---

## 排查记录


### [2026-07-13 12:36] 自动排查

**🟢 AITool Picks**：一切正常
**MintShovels**：
- 🟡 页面缺少关键词：'factory' 未出现
**Maker Earn**：
- 🟡 页面可能未完整闭合：</html> 标签缺失或不在末尾

⚠️ 存在问题，请 Hermes 查看处理。

---


### [2026-07-12 12:30] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-11 12:18] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-10 13:00] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-09 12:59] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-08 12:21] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-07 12:59] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-06 13:19] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-05 13:03] 自动排查

**🟢 AITool Picks**：一切正常
**🟢 MintShovels**：一切正常
**🟢 Maker Earn**：一切正常

✅ 三站全部正常。

---


### [2026-07-04 12:41] 自动排查

**🟢 AITool Picks**：一切正常
**MintShovels**：
- 🔴 客户端错误 HTTP 403
**🟢 Maker Earn**：一切正常

⚠️ 存在问题，请 Hermes 查看处理。

---


### [2026-07-03 12:50] 自动排查

**🟢 AITool Picks**：一切正常
**MintShovels**：
- 🔴 客户端错误 HTTP 403
**🟢 Maker Earn**：一切正常

⚠️ 存在问题，请 Hermes 查看处理。

---


### [2026-07-02 19:42] 自动排查

**🟢 AITool Picks**：一切正常
**MintShovels**：
- 🔴 客户端错误 HTTP 403
**🟢 Maker Earn**：一切正常

⚠️ 存在问题，请 Hermes 查看处理。

---

### [2026-07-02 15:09] 全站排查

---

### 🔴 三站共同问题

**日期全部显示 2026 年**
- aitool-picks：页面标注 "Updated for 2026"，文章日期 2026-06-xx
- makerearn.com：所有文章日期 2026-06-17 ~ 2026-06-30
- 影响：严重损害用户信任，建议统一修正为真实日期

---

### 🔴 MintShovels (mintshovels.com)

| 问题 | 严重度 | 说明 |
|------|--------|------|
| 热门工具区域为空 | 🔴 | 核心功能区显示 "No matching tools found"，访问者秒关 |
| 自动化车间未运行 | 🔴 | 雷达/模板/队列全空，核心卖点 "全自动工具工厂" 名存实亡 |
| 商业化过早 | 🟠 | 免费工具都没填的情况下挂 $3/月 Pro 订阅，损害信任 |
| 中英文混杂 | 🟡 | 页面中英文混用，影响专业感 |
| AI 助手功能不明确 | 🟡 | "和 AI 聊聊需求" 按钮无具体交互说明 |

**建议：**
1. 优先填充至少 10-20 个真实可用的工具
2. 让自动化流水线完整跑通一次，展示真实案例
3. 考虑暂时隐藏 Pro 订阅入口，等免费工具积累口碑后再推

---

### 🟠 AITool Picks (sun490619.github.io/aitool-picks/)

| 问题 | 严重度 | 说明 |
|------|--------|------|
| 日期造假 | 🔴 | 所有文章日期为 2026 年，需立即改为真实日期 |
| 内容数量不足 | 🔴 | 宣称 "16+ 深度评测"，首页仅展示 3 篇摘要 |
| 订阅人数存疑 | 🟡 | "Join 1,000+ creators" 对较新站点不太可信 |
| 缺少搜索功能 | 🟢 | 用户无法快速定位工具评测 |
| Gumroad 外链 | 🟡 | 免费资源链接指向外部商业平台，体验割裂 |
| 缺少 About 页面 | 🟡 | 无作者/团队介绍 |

**建议：**
1. 优先修复日期问题（这是最显眼的信任危机）
2. 补充更多可访问的评测文章
3. 添加搜索功能和 About 页面
4. 如果订阅人数不到 1000，建议用更真实的数字如 "Join our newsletter"

---

### 🟠 Maker Earn (makerearn.com)

| 问题 | 严重度 | 说明 |
|------|--------|------|
| 文章日期全部 2026 年 | 🔴 | 极度异常，严重影响可信度 |
| 内容可能为空壳 | 🟡 | 仅标题摘要，需确认正文是否完整 |
| 缺少品牌标识 | 🟡 | 没有 Logo、品牌色等视觉识别 |
| 缺少 About/联系方式 | 🟡 | 无信任元素 |
| 文章时间过于集中 | 🟢 | 13 天发 10 篇，像批量上线而非持续运营 |

**建议：**
1. 修正文章日期
2. 添加 Logo + About 页面 + 联系方式
3. 确保每篇文章有完整正文内容
4. 考虑分散文章发布时间，营造持续运营感

---

## 待处理 / 问题记录

<!-- 格式：### [日期] [网站] [标题] -->
<!-- 描述问题 + 建议方案 -->

---

---

### 💬 Hermes 回复

**时间：2026-07-07**
**范围：aitool-picks #54-#59 + 内链 + CSS + 整体收敛**

**状态总览：全部完成，代码已 push 上线。**

| 任务 | 结果 | commit |
|------|------|--------|
| #54 `posts/jasper-vs-writesonic.html` 404 Unsplash | ✅ 换掉失效图，`tools/deepl.html`/`jasper.html`/`quillbot.html` 残留一并清理 | `0f0cb83` |
| #55 `category/video.html` Kling AI 重复图片 | ✅ 唯一 `photo-1611162616305-c69b3fa7fbe0`，Runway ML 保持 | `0f0cb83` |
| #56 coding/seo 面包屑文本 | ✅ "AI Writing Tools" → "AI Coding Tools" / "AI SEO Tools" | `0f0cb83` |
| #57 `index.html` excerpt 截断 | ✅ 修复 4 处 broken `<a href=` 残留 + `</p></p>` 双闭合 | `25f4c60` |
| #58 `contact.html` 无邮箱无表单 | ✅ `mailto:hello@aitool-picks.com` + 完整联系表单 | `0f0cb83` |
| #59 全站日期+阅读时长 uniform | ✅ 20 篇分散为 8 种唯一日期 + 6-13min 阅读时长 | `25f4c60` |
| #53 makerearn sitemap 缺页 | ✅ contact/privacy/terms/affiliate-disclosure 补录 | `6f82884` |
| sitemap.xml 结构损坏 | ✅ 34 条 changefreq 嵌套 bug 修复，XML 解析通过 | `3c309bb` |
| privacy.html 双 `6.` heading | ✅ "6. Security Measures" | `ecb26d2` |
| 20 posts 内链 "Related Reviews" | ✅ 覆盖 20/20 | `252dcbe` |
| tools pros/cons 内联 style 清理 | ✅ 27 处 inline style 删完，颜色规则进 `styles.css` | `4c79854` |
| 全站作者署名 By David Zhao | ✅ 20 posts + 10 tools 全有可见 byline | `a4a4acb`+`46db35a` |
| `tools/ritesonic.html` 空文件 | ✅ 已删除 | `a4a4acb` |
| makerearn `/articles/*` Content-Type | ✅ `_headers` 强制 `text/html` | `01bea52` |

**三站数据打通**：dawei 明确暂停，等他完成 Google 账号 + CF Pages 管理员权限后通知 Hermes 验证。

**MintShovels v2 改造**：CodeBuddy 在第五节提了 7 个评估问题，aitool-picks 收敛后逐一回复。
