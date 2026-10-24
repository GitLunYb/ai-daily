# 航天日报 · 2026-10-24

> 数据采集窗口：2026-10-21 至 2026-10-24。本期数据源以 Hacker News / Reddit / arXiv / GitHub 为主，**绝大多数条目与航天无直接技术关联**（大量为 AI、软件、社会话题），且 `entity` 字段存在明显错配（如游戏公司关闭被归入 ESA、PHP 漏洞被归入 ESA）。本日报严格按数据实际内容筛选，仅保留可确认为航天/空间相关或对航天工程方法有直接借鉴价值的条目，其余不编造、不强行归类。所有条目 `stars` 字段均为 `null`，故不显示星标。

---

## TL;DR

1. **NASA 公布 Artemis 加速计划**，并同步释出 Artemis III（LEO 风险降低任务）与 Artemis IV 登月概念运行方案，Starship HLS 与 Blue Moon 双着陆器并行推进。
2. **Starship HLS「Cabin 1」在 Starfactory 建造画面公开**，NASA 估算单次登月仍需约 22 次 Starship 发射。
3. **日本发射火卫一采样返回任务**（MMX），目标带回火星卫星 Phobos 样品。
4. **Iceye 与 Nokia 联手乌克兰国防部**，共建主权级卫星通信能力，SAR+通信融合的国防航天模式进一步成型。
5. **在轨大型刚性载荷协同运输**出现去中心化双层优化新方法（arXiv），面向空间经济与轨道碎片治理需求。

---

## 发射任务 Launch & Mission

### 日本发射火卫一采样返回任务 🆕（2026-10-21）
Ars Technica 报道日本启动火卫一（Phobos）采样返回任务，目标将火星卫星物质带回地球。**评分 3.2**。
简评：MMX 是继隼鸟系列后日本深空采样返回的又一次跃迁，火卫一物质被认为可能包含火星原始物质甚至太阳系早期信息。数据中仅有标题级信息，任务细节（发射窗口、采样方式、返回时间）未提供，不做展开。
链接：https://arstechnica.com/space/2026/10/japan-launches-mission-to-bring-home-a-piece-of-the-martian-moon-phobos/

### NASA 公布 Artemis 加速计划 🆕（2026-10-24）
NASA 分享月球任务加速方案，涉及 Artemis 系列节奏调整。**评分 2.5**。
简评：标题级信息，具体加速内容需结合同日 Reddit 多条 Artemis 相关帖交叉印证（见下）。
链接：https://www.reddit.com/r/nasa/comments/1xdvkdj/nasa_shares_artemis_acceleration_plans_for_moon/

### Artemis III 概念运行方案（LEO 风险降低任务）🆕（2026-10-23）
据 Reddit 摘要，Artemis III 基线为 14 天任务（可延至 17 天应对天气/延迟），逐日安排专项测试；Blue Origin 先发射 Blue Moon 测试着陆器。**评分 2.5**。
简评：将 Artemis III 重新定义为 LEO 风险降低任务，是 Artemis 架构在着陆器进度压力下的务实调整——先在近地验证对接、加注、着陆器操作链路，再执行月面着陆。这是典型的「分阶段降风险」系统工程思路。
链接：https://www.reddit.com/r/spacex/comments/1xdts0b/summary_of_nasas_artemis_acceleration_event_as/

### Artemis IV 登月概念运行方案（Starship 版）🆕（2026-10-23）
NASA 发布 Artemis IV 使用 Starship 着陆器的概念运行方案，同时亦发布 Blue Origin 着陆器版本，官方表示仍将采用先就绪者。**评分 2.5**。
简评：双着陆器并行、先就绪先用，是 NASA 在商业着陆器竞争格局下的风险对冲策略，也意味着任务设计需保持接口层面的着陆器无关性。
链接：https://www.reddit.com/r/spacex/comments/1xdqwr4/nasas_newly_released_concept_of_operations_for/

### Starship HLS「Cabin 1」建造画面公开 🆕（2026-10-23）
NASA 在 Artemis 加速活动直播中分享 Starfactory 内 Starship HLS 乘员舱 Cabin 1 的建造图像。**评分 2.5**。
简评：HLS 乘员舱从图纸进入实物建造阶段，是 Artemis 载人登月链条上关键硬件节点的可见进展。信息限于图像层面。
链接：https://www.reddit.com/r/spacex/comments/1xdrjnr/nasa_shares_new_images_of_starship_hls_cabin_1/

### Starship 单次登月发射需求估算：约 22 次（2026-10-22）
Reddit 讨论给出支持一次月面着陆所需 Starship 发射次数的最新估算为 22 次。**评分 2.5**。
简评：22 次发射对应的是轨道加注架构的规模代价。这一数字直接决定登月任务的节奏可行性与成本结构，也是「快速复用」能力能否兑现的试金石。数据为社区估算，非官方确认。
链接：https://www.reddit.com/r/spacex/comments/1xcy6ds/latest_estimate_for_starship_launches_required_to/

### SpaceX 下一次飞行将尝试 Starship 捕获（2026-10-21）
报道称 SpaceX 计划在下一次 Starship 飞行中尝试捕获，并着眼提升发射频率。**评分 2.5**。
简评：回收捕获是复用闭环的核心环节，与上条 22 次发射需求直接耦合——没有高频复用，轨道加注架构不成立。
链接：https://www.reddit.com/r/spacex/comments/1xbzhug/spacex_to_attempt_starship_catch_on_next_flight/

### CRS-35 货运龙 4K 回放（2026-10-23）
10 月 13 日发射的 CRS-35 货运龙任务 4K 回放。**评分 2.5**。
简评：常规国际空间站货运补给任务，信息有限。
链接：https://www.reddit.com/r/spacex/comments/1xd3rjz/4k_replay_of_crs35_cargo_dragon_mission_launched/

---

## 卫星与星座 Satellite & Constellation

### 多 LEO 卫星辅助通信的随机几何分析与优化（2026-10-22）
arXiv 论文，针对 LEO 卫星对地用户无缝连接中的复杂星地传播与不可忽略的卫星失效概率，建立随机几何分析框架并做优化。**评分 4.7**。
简评：把「卫星失效概率」显式纳入星座覆盖分析，比传统理想化几何模型更贴近真实星座运营。对大规模星座的容量规划与冗余设计有直接参考价值。
链接：https://arxiv.org/abs/2610.31373v1

### NASA 卫星追踪闪电留下的污染（2026-10-22）
马里兰大学牵头实验，利用 NASA 卫星研究闪电产生的氮氧化物及其对空气污染与大气自净能力的影响。**评分 2.5**。
简评：闪电生成 NOx 的星基观测，属于大气化学与卫星遥感的交叉应用。信息有限。
链接：https://www.reddit.com/r/nasa/comments/1xc4qxs/nasa_satellite_tracks_the_pollution_lightning/

---

## 空间攻防 Space Defense & Security

### Iceye 与 Nokia 联手乌克兰国防部共建主权卫星通信能力（2026-10-22）
Iceye 与 Nokia 同乌克兰国防部合作，开发主权级卫星通信能力。**评分 5.2**。
简评（技术层面）：这是 SAR 遥感厂商与通信设备商的能力拼接——Iceye 提供星载 SAR 与星座运营经验，Nokia 提供地面/星地通信网络设备，乌方获得的是「侦察—传输」一体的主权能力，而非单纯采购图像。其技术要点在于：SAR 数据量大、时效要求高，星上处理与高速星地链路成为瓶颈，通信侧能力直接决定遥感价值的兑现速度。此类「遥感+通信」捆绑模式正在成为国防航天采购的主流形态。
链接：https://www.iceye.com/newsroom/press-releases/iceye-and-nokia-partner-with-the-ministry-of-defence-of-ukraine-to-develop-sovereign-satcom-capability

### 政策动向简提（不展开）
- 乌克兰方面称 Starlink / Starshield 速度限制仍在（2026-10-23，评分 9.0）；另有报道称马斯克下令放缓乌克兰 Starlink 并归因于特朗普（2026-10-22，评分 4.4）、特朗普致电马斯克要求解除限制（2026-10-22，评分 4.9）、共和党议员威胁就 Starlink 准入追责（2026-10-21，评分 4.0）、乌克兰学习在无 Starlink 条件下作战（2026-10-23，评分 4.0）。
- 评论文章《是时候把 Starlink 从马斯克手中拿走》（2026-10-22，评分 9.2）、《马斯克对太空的危险掌控》（2026-10-23，评分 3.5）。
- 要点：商业星座作为战场关键基础设施，其控制权归属已成为军备与政策层面的实质议题。以上均为政策/舆论动向，技术内容有限。

---

## 控制与分系统 Control & GNC（只卫星）

> 本期数据中**无**符合「卫星姿轨控、GNC、星敏、反作用轮」定义的条目。`entity` 标注为「控制与分系统」的条目（T132–T145）实际内容为图像生成、视频扩散、LLM 评测、隐私审计等，与卫星控制无关，不予归类。

---

## 航天前沿与新方法 Frontier & Methods

### 在轨大型刚性载荷协同运输的去中心化双层优化（2026-10-22）
arXiv 论文，面向空间经济增长与轨道拥堵/碎片加剧的背景，研究大型、非合作目标的可靠在轨运输，提出去中心化双层优化方法实现多航天器协同搬运刚性载荷。**评分 5.2**。
简评：在轨搬运大型非合作物体是碎片清除与在轨服务（OOS）的共同底层能力。去中心化双层优化的价值在于：上层做协同任务分配、下层做各航天器本地轨迹优化，避免单点集中规划在通信延迟与失效下的脆弱性。这是把地面多机器人协同控制方法迁移到轨道动力学约束下的有益尝试。
链接：https://arxiv.org/abs/2610.31562v1

### 多机器人协调的分散树协议（2026-10-22）
arXiv 论文，将非线性系统多机器人协调表述为受群体约束的联合空间最优控制，提出分散树协议以逼近联合最优。**评分 5.2**。
简评：方法层面与上条同源（分布式协同最优控制），对卫星编队/集群控制有方法借鉴价值，但论文本身面向地面多机器人。
链接：https://arxiv.org/abs/2610.31540v1

### NASA fmdtools v2.5.7（2026-10-23）
NASA 开源故障建模工具 fmdtools 发布 v2.5.7，改进样本权重累积共享、保留 FMEA 加权与未分组表合计等。**评分 8.8**。
简评：fmdtools 面向系统故障建模与 FMEA 分析，是航天系统可靠性/功能建模的实用开源工具。本次为质量改进版本，无架构级变化。对做 MBSE 与功能失效分析的团队有直接使用价值。
链接：https://github.com/nasa/fmdtools/releases/tag/v2.5.7

### NASA harmony-maskfill 1.4.0（2026-10-23）
NASA harmony-maskfill 服务升级至 Python 3.14，Docker 镜像改为 python:3.14-slim，依赖改用 Pip 安装。**评分 8.8**。
简评：纯基础设施维护更新（运行时与打包方式迁移），无算法或功能变化。对使用该服务的用户而言，关注点是 Python 3.14 兼容性与镜像体积变化。
链接：https://github.com/nasa/harmony-maskfill/releases/tag/1.4.0

### NASA 罗曼空间望远镜进入最终调试阶段（2026-10-23）
Reddit 消息，罗曼空间望远镜进入最终调试阶段。**评分 2.5**。
简评：标题级信息。罗曼望远镜的最终调试阶段意味着其发射前集成测试接近收尾，但数据未提供具体节点与时间表，不做展开。
链接：https://www.reddit.com/r/nasa/comments/1xdidi9/nasas_roman_space_telescope_enters_final/

### NASA 资助国家科学院委员会建议月球人类探索四个地点（2026-10-23）
应 NASA 请求，国家科学院《Human Exploration Across the Moon》共识研究报告识别出月球极区之外的高价值科学目的地。**评分 2.5**。
简评：为短时长载人月面任务选址提供科学优先级依据，是「科学驱动任务设计」的典型产出。信息限于报告结论层面。
链接：https://www.reddit.com/r/nasa/comments/1xdf92l/nasasponsored_national_academies_committee/

### NASA SR-1 Freedom 核电源模块进展（2026-10-22）
Reddit 消息，NASA SR-1 Freedom 在核电源模块方面取得进展。**评分 2.5**。
简评：标题级信息，具体技术细节未提供。空间核电源是月面/深空长期驻留的关键使能技术，值得持续跟踪。
链接：https://www.reddit.com/r/nasa/comments/1xcjq70/nasas_sr1_freedom_advances_with_progress_on/

### NASA 三台月球车进展更新（2026-10-22）
NASA 就 Artemis 与月球基地建设至关重要的三台月球车给出更新。**评分 2.5**。
简评：标题级信息，具体状态未提供。
链接：https://www.reddit.com/r/nasa/comments/1xckf81/nasa_gives_update_on_3_lunar_rovers_crucial_to/

### NASA 哈勃图像「谱曲」工具（2026-10-23）
NASA 上线工具，将哈勃图像中的特征转为声音，可像乐谱一样「演奏」图像。**评分 2.5**。
简评：科学传播/数据可听化（sonification）应用，属科普创新而非工程方法创新。
链接：https://www.reddit.com/r/nasa/comments/1xd7jlt/nasa_built_a_tool_that_lets_you_compose_music/

### 挑战者号决策档案复盘（2026-10-22）
Reddit 长文，基于 NASA 1986 年飞行清单与重新设计文件，复盘发射前夜 Boisjoly 与管理者关于低温 O 型环的争论及「摘下工程师帽子」一幕。**评分 2.5**。
简评：工程伦理与组织决策的经典案例复盘，对航天质量管理与「异议渠道」制度建设有长期参考价值。属历史档案整理，非新技术。
链接：https://www.reddit.com/r/nasa/comments/1xcf0wg/take_off_your_engineering_hat_how_nasa_overruled/

### 其他（方法可迁移，非航天本体）
- **HiP3R：长时序 3D 重建的分层位姿图**（2026-10-22，评分 5.2）：解决前馈模型无法直接处理数千帧序列的计算/内存瓶颈，对星载视觉导航与在轨相对位姿估计的长时序建图有方法借鉴。https://arxiv.org/abs/2610.31635v1
- **OmniRay：相机无关单目 3D 重建**（2026-10-22，评分 5.2）：面向鱼眼/全景等非针孔相机的复合射线场重建，对宽视场星敏感器/空间相机的地形与目标重建有潜在参考。https://arxiv.org/abs/2610.31645v1
- **遥感视觉-语言模型综述**（2026-10-22，评分 5.2）：系统梳理遥感领域数据驱动的 VLM 进展，是星载遥感智能解译方向的入门级综述。https://arxiv.org/abs/2610.31304v1
- **AI 辅助早期结构设计智能体**（2026-10-22，评分 5.2）：将设计意图翻译为结构模型的 agentic 工作流，对航天结构早期方案迭代有方法参考。https://arxiv.org/abs/2610.31113v1

---

## 商业与融资 Business & Funding

### SpaceX 营收飙升 161%，AI 业务增长（2026-10-21）
ABC News 报道 SpaceX 营收同比增长 161%，AI 业务增长。**评分 8.7**。
简评：营收结构中出现「AI 业务」并成为增长驱动，反映 SpaceX 的收入构成已不止于发射与星链。具体财务口径与分部数据未在数据中给出。
链接：https://abcnews.com/Business/spacex-revenue-soars-161-ai-business-grows/story?id=137408509

### SpaceX 与特斯拉探索合并（2026-10-21）
NYT 报道 SpaceX 与特斯拉探索合并。**评分 5.1**。
简评：若成真将重塑航天与汽车/能源资产的资本结构。数据仅为「探索」阶段报道，无条款信息。
链接：https://www.nytimes.com/2026/10/21/business/elon-musk-spacex-tesla-merger.html

### 评论：马斯克的梦想合并