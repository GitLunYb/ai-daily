# 航天日报 · 2026-11-27

> 数据采集窗口：2026-11-24 至 2026-11-27。本期数据以 Hacker News 与 arXiv 为主，航天实体标签（SpaceX、NASA、ESA 等）与条目内容存在较多错配，以下仅对**内容确属航天/空间领域**的条目做正式归类；标签与内容不符者不纳入航天条目，避免误导。星数字段本期全部为空，故不显示 ⭐。

---

## TL;DR

1. **SpaceX 获 FCC 批准部署 100 万颗轨道数据中心卫星**，多源报道（CNBC、Reuters、BBC、NPR、Ars Technica），为本周最大航天事件。
2. **ESO 就"百万级太空数据中心"发表官方声明**，欧洲天文学界对轨道光污染与射电干扰表达关切。
3. **欧洲最大卫星工厂在比利时开业**，明确以对标 Starlink 为目标（Aerospacelab）。
4. **NASA 火星舰队约半数因技术问题离线**，老龄化深空资产风险显性化。
5. **NASA 开源工具 ziggy 发布 v1.0.2**，修复由 NASA 安全团队识别的日志消息漏洞。

---

## 卫星与星座

### SpaceX 获 FCC 批准部署 100 万颗轨道数据中心卫星 🆕
多源报道确认美国监管机构批准 SpaceX 部署规模达百万颗的"太空数据中心"卫星星座。评分 9.2 / 8.8 / 4.1 / 3.4 / 3.2（多源）。
[CNBC](https://www.cnbc.com/2026/11/25/spacex-fcc-satellite-approval.html) · [Reuters](https://www.reuters.com/business/media-telecom/us-authorizes-spacex-deploy-1-million-satellites-data-centers-space-2026-11-25/) · [BBC](https://www.bbc.co.uk/news/articles/cwp836l8n1jgo) · [NPR](https://www.npr.org/2026/11/26/g-s1-155940/fcc-spacex-satellites-data-centers-in-space) · [Ars Technica](https://arstechnica.com/space/2026/11/the-fcc-has-authorized-spacex-to-deploy-1-million-satellites/)

**简评**：本周最具分量的航天监管事件。百万颗量级远超现有任何星座规划，其轨道密度、频率协调与再入管理问题均无先例。多源交叉印证，可信度高；但条目本身为新闻转述，技术细节（单星功率、星间链路、散热方案）未在数据中展开，不宜臆测。

**深入**：该批准若落地，意味着"轨道算力"从概念走向监管许可阶段——把数据中心负载迁移至低轨，理论上可利用连续太阳能与真空辐射散热。但百万颗规模对轨道碎片管理、天文观测（见下条 ESO 声明）与频率资源构成系统性挑战，监管批准与实际部署之间仍有巨大工程与生态鸿沟。

### ESO 就百万级太空数据中心获批发表声明 🆕
欧洲南天天文台就"一百万颗太空数据中心"发射获批发布官方声明。评分 8.5。
[eso.org](https://www.eso.org/public/news/eso2614/)

**简评**：天文界对轨道巨型星座光污染与射电干扰的正式表态，与上条形成"产业—科学"张力。声明具体内容数据未给出，仅据标题与来源判断其立场为关切。

### 欧洲最大卫星工厂开业，剑指 Starlink 🆕
Aerospacelab 在比利时开设欧洲最大卫星工厂，定位为对 Starlink 的竞争性产能。评分 3.7。
[CNBC](https://www.cnbc.com/2026/11/26/starlink-satellites-aerospacelab-factory-belgium.html)

**简评**：欧洲卫星制造产能扩张的信号，但条目信息量有限，量产节拍与成本目标未披露。

### NASA 火星舰队约半数因技术问题离线
Ars Technica 报道 NASA 老龄化火星探测舰队中约一半因技术故障失联/离线。评分 3.2。
[Ars Technica](https://arstechnica.com/space/2026/11/half-of-nasas-aging-mars-fleet-knocked-offline-by-technical-issues/)

**简评**：深空资产老龄化与单点故障风险的现实案例，具体受影响探测器数据未列出，不展开。

---

## 空间攻防

> 本期该分类下多数条目（AI 模型计费、文明史、域名接管等）与空间攻防无关，仅保留技术相关内容。

### 燃料即身份：全密钥失陷后星间激光链路的认证
arXiv 论文提出在攻击者获取卫星全部密钥后，利用"燃料"作为物理身份凭证对星间激光链路进行认证。评分 4.6。
[arXiv:2611.34470](https://arxiv.org/abs/2611.34470v1)

**简评**：思路有创新性——把推进剂余量当作不可伪造的物理指纹，绕开纯密钥体系的单点失效。但"燃料即身份"的可观测性、精度与对抗条件下的稳定性均需验证，属概念探索阶段。

### 俄罗斯准备发射搭载核武器的卫星（政策动向）
有报道称北约认为俄罗斯正筹备发射搭载核武器的卫星。评分 2.8。
[bnn-news](https://bnn-news.com/world/nato-believes-russia-is-preparing-to-launch-a-satellite-equipped-with-nuclear-weapons-jqvj38x)

**简评**：军备动向类消息，单一来源、未证实，仅作态势提示，不作技术展开。

---

## 控制与分系统（仅卫星）

> 本期该分类下绝大多数 arXiv 条目为机器人/视觉/强化学习，与卫星姿轨控无关。仅一条与空间指向/动量管理相关。

### 轻量高空气球载荷的方位指向与动量管理
arXiv 论文针对 ALTAIR 项目（以平流层气球搭载积分球作为人造星进行光度定标）研究方位指向与角动量管理。评分 4.6。
[arXiv:2611.34817](https://arxiv.org/abs/2611.34817v1)

**简评**：属"指向控制+动量管理"的空间工程问题，虽载体为气球而非卫星，但控制方法论（指向精度、角动量卸载）与卫星姿控同源，可作为分系统设计的参考案例。数据未给出具体指标，不展开。

---

## 航天前沿与新方法

### NASA ziggy v1.0.2：修复 NASA 安全团队识别的漏洞
NASA 开源项目 ziggy 发布 v1.0.2（含 v1.0.1），修复日志消息中的安全漏洞（ZIGGY-687），并修复 `ziggy export-pipelines` 命令。评分 8.7。
[GitHub](https://github.com/nasa/ziggy/releases/tag/v1.0.2)

**简评**：航天机构开源工具链的安全维护实践，版本说明清晰、可追溯，是"敏捷研制+安全左移"的正面样例。功能范围数据未详述，仅据 release note 描述。

### 面向 AI 智能体的科研入学考试（REE）
arXiv 提出 REE 基准，用于评估自主科研智能体通过重复实验改进解的能力。评分 4.6。
[arXiv:2611.34646](https://arxiv.org/abs/2611.34646v1)

**简评**：AI for Science 评测方法学的新尝试，对航天领域"AI 辅助设计/实验"的评估体系有借鉴意义，但尚未针对航天任务定制。

### AI 原生自编码器通信的频谱自适应（迁移学习）
arXiv 研究端到端物理层学习中自编码器在频谱变化下的迁移适配。评分 4.6。
[arXiv:2611.34942](https://arxiv.org/abs/2611.34942v1)

**简评**：AI 原生空口技术与卫星通信频谱灵活使用方向相关，属方法探索，工程成熟度尚早。

---

## 商业与融资

### SpaceX 拟向每名美国儿童赠予公司股票
多条报道称 SpaceX/马斯克宣布向每名美国儿童赠予 SpaceX A 类普通股（股数报道不一：1 股 vs 2 股）。评分 3.7 / 3.5 / 3.4。
[SpaceX IR](https://ir.spacex.com/updates/releases-details/2026/SpaceX-to-Invest-in-the-Next-Generation-of-Americans-2026-r_LYQ5cH94/default.aspx) · [Reuters](https://www.reuters.com/business/media-telecom/musk-says-every-child-us-will-get-two-spacex-shares-2026-11-26/) · [Twitter](https://twitter.com/elonmusk/status/2125797463047258119)

**简评**：非常规的公众关系/股权安排，股数在不同来源间存在矛盾（1 股 vs 2 股），以官方 IR 为准更稳妥。属商业与舆情事件，非技术议题。

### 马斯克称 SpaceX 与 Tesla 探索史上最大合并
有报道称马斯克表示 SpaceX 与 Tesla 正探索合并。评分 2.6。
[Al Jazeera](https://www.aljazeera.com/economy/2026/10/21/elon-musk-says-spacex-and-tesla-exploring-largest-merger-in)

**简评**：单一来源、日期偏早（10 月），可信度与时效性均弱，仅作线索记录。

---

## 今日精讲：燃料即身份——全密钥失陷下的星间激光链路认证

**是什么**：arXiv 论文《Fuel as Identity: Authenticating Inter-Satellite Laser Links after Total Key Compromise》提出，在攻击者已获取某卫星**全部密钥**的极端假设下，仍能对星间光链路进行身份认证——把卫星的推进剂余量作为物理层身份凭证。

**技术亮点**：传统星间链路安全完全建立在密钥之上，"全密钥失陷"即意味着认证体系归零。该工作转向**物理不可克隆/难以伪造的系统状态**（燃料量）作为第二因子，思路接近"物理层指纹"与"状态即身份"，把安全根从密码学迁移到航天器自身的可观测物理量。

**解决什么问题**：星间激光链路是低轨巨型星座的骨干，一旦单星密钥被攻破，攻击者可注入伪造节点、劫持路由。该方案试图在密码学失效后仍保留一道认证屏障。

**未来潜力**：若百万级星座（见本期 SpaceX 条目）成为现实，星间链路的密钥管理规模将空前庞大，"全密钥失陷"不再是理论假设。物理层身份认证可能成为星座安全的必要补充层。

**潜在风险**：燃料余量的可观测精度、在轨测量误差、对抗条件下的可欺骗性均未在数据中给出验证；且燃料随任务消耗而变，"身份"是动态量，认证协议设计复杂。当前属概念阶段，工程可行性待证。

**与同类对比**：相较纯密码学方案（抗量子密钥分发、密钥轮换），该工作走的是"非密码学冗余"路线，二者互补而非替代。本期另有多篇 AI 安全/对抗论文（如监控评估误导、对抗补丁），但均不针对空间链路，可比性有限。

---

*说明：本期数据中大量条目的 entity 标签（SpaceX/NASA/ESA/CASC 等）与标题内容明显不符（如 AI 模型计费、Vim 手册、Waymo 扔鸡蛋等），已按"严格基于内容"原则剔除，未纳入航天日报正文。星数字段全为空，故全文未显示 ⭐。*