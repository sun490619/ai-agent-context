# Key Decisions Log

## Business Model Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-06 | aitool-picks 导流至用户自有 Gumroad 店铺主页，非平台佣金 | 100%收入归用户 |
| 2026-06 | aitool-picks Gumroad 导流目标改为店铺主页 https://sunshine4255.gumroad.com | 提高转化 |
| 2026-06 | aitool-picks 方案从 B 调整为 A（Redbubble 优先取消） | 用户明确要求 |
| 2026-06 | aitool-picks 初始方案原定选 B（Redbubble 优先），后按用户要求切换为 A | 用户明确要求 |

## Content Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-06 | Gumroad 产品格式标准化：listing.md + 内容文件 + cover.png | 统一规范 |
| 2026-06 | Gumroad 封面图用 Pillow 简单文字风格（深色背景+白色标题），不再调用 FAL | 用户明确要求 |
| 2026-06 | 47个免费产品，2个$5（#30 Dropshipping、#43 Python Scripts），1个$7（#35 React Components） | 用户决定 |
| 2026-06 | "100 Excel Formulas" 和 "50 ChatGPT Prompts for Content Creators" 定价用户未定 | 待确认 |
| 2026-06 | KDP 选题方向：细分软件速查指南（40%，Notion/Figma/Midjourney）、AI+转型手册（30%）、标准化职场模板库（30%） | 用户提供 |
| 2026-06 | aitool-picks 每 2-3 天发一篇新文章，先追到 15 篇 SEO 文章 | 用户要求 |

## Technical Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-06 | sing-box 配置未修改 | 用户恐惧，手动 VPN 切换更安全 |
| 2026-06 | KDP/Payoneer/Wise 必须使用中国真实 IP（手动切换） | 国际平台封号风险 |
| 2026-06 | 所有新增被动收入项目必须无 upfront 费用、无需信用卡 | 用户无信用卡 |
| 2026-06 | #10 Chrome Extension 铺货永久搁置（Chrome Web Store 需 5美元信用卡） | 用户无信用卡 |
| 2026-06 | aitool-picks HTML 变更通过助手执行 git push（用户不会 Git） | 用户不会操作 |
| 2026-06 | #13 Niche Newsletter：Substack 免费注册，内容由助手生成 | 无需信用卡 |
| 2026-06 | 用户使用多 agent 协作模式：当前 agent + "Aged" agent | 用户明确要求 |
| 2026-06 | aitool-picks 渲染问题（强制刷新）用户明确要求当前不做，等待 Aged agent 处理 | 避免多 agent 冲突 |

## Tool & Service Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-06 | 4 个平台已注册并绑定 PayPal：Shutterstock、Adobe Stock、Freepik、Teespring | 用户注册 |
| 2026-06 | Redbubble deferred（封号风险）、Etsy deferred（门槛） | 用户决定 |
| 2026-06 | AI Stock/POD 项目正式搁置（19/20 图像无效，FAL 余额耗尽） | 无替代方案 |
| 2026-06 | Amazon Affiliate 链接后台自动对相关产品加追踪码 | 用户要求 |
| 2026-06 | aitool-picks Amazon Associates 追踪 ID sun490619-20 | 用户申请成功 |
| 2026-06 | 工具评测文章底部只留 Related Reviews，不加 Amazon 推荐 | 用户反馈太乱 |
| 2026-06 | Best-of 文章保留 Amazon 推荐区块 | 不冲突 |
| 2026-06 | Amazon 推荐商品按销量/佣金定期轮换 | 用户要求 |
| 2026-06 | MintShovels Amazon 推荐卡片：3 个，后期可替换 | 用户批准 |
