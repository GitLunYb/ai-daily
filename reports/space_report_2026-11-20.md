# 航天日报 · 2026-11-20

> 数据采集窗口：2026-11-17 至 2026-11-20。本期数据源以 Hacker News 与 arXiv 为主，航天垂类内容占比有限，部分条目为泛科技/安全事件，已按主题归入相应分类并标注信息边界。


## TL;DR

1. **Voyager 1 抵达距地球一光日**，成为人类首个跨越该距离尺度的人造物体，NASA 官方与多家媒体同步报道。
2. **低轨核爆效应研究（arXiv）** 系统评估 LEO 核爆对卫星与轨道环境的连锁影响，为空间攻防与碎片治理提供量化参考。
3. **年度入轨质量按火箭厂商统计** 的可视化分析发布，SpaceX 份额继续拉开差距，欧洲与中方数据被并列对比。
4. **在轨卫星数量已超过多数城镇可见恒星数**，星座密度对天文观测与轨道管理的压力进入公众视野。
5. **NASA 开源软件栈更新**：spacewasm v0.8.0-rc.2 与 fprime-gds v4.4.2a1 同日发布，星上 WebAssembly 与地面数据系统持续迭代。


## 发射任务

### Mass launched to orbit each year by rocket builder ⭐— ｜评分 8.8 ｜2026-11-18
按火箭厂商统计的年度入轨质量可视化分析，对比 SpaceX 与欧洲、中国等发射方的份额变化。（信息有限，仅基于标题与摘要）
链接：https://www.kadoa.com/companies/insights/spacex-europe-payload

> **深入**：该分析的价值不在单点数据，而在"入轨质量"这一口径的横向可比性——它比发射次数更能反映运力结构，也比载荷数量更能体现星座部署强度。对关注发射市场竞争格局的读者，这是少见的按厂商拆分的连续序列数据；但需注意统计口径（是否含拼车、是否含再入质量）会显著影响结论，引用时应回溯原始方法说明。


## 卫星与星座

### Satellites now outnumber the visible stars above most towns ⭐— ｜评分 7.3 ｜2026-11-18
报道指出在多数城镇上空，在轨卫星数量已超过肉眼可见恒星数量，讨论星座密度对观星与天文观测的影响。（信息有限）
链接：https://www.space.com/space-exploration/satellites/satellites-now-outnumber-the-visible-stars-above-most-towns

### Voyager 1 hits one light day from Earth ⭐— ｜评分 8.5 ｜2026-11-18 🆕（相关报道 11-19）
NASA 官方页面确认 Voyager 1 距地球达一光日，并给出双探测器实时位置。多源交叉报道（NYT、NPR、LiveScience）形成本期最集中的航天新闻簇。
链接：https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/

> **深入**：一光日约 259 亿公里，信号单程需 24 小时——这意味着任何指令发出后要等近两天才能确认结果，深空测控的"开环操作"特征被推到极致。Voyager 1 已运行 49 年，其电源（RTG）功率逐年衰减，工程团队近年通过关闭非必要载荷、重构供电策略维持基本科学探测。这一里程碑的实质意义在于：它标定了人类现有深空通信与航天器长寿设计的实际边界，也为后续星际探测任务的通信链路预算提供了真实参照点。

### Show HN: Take Voyager 1 apart, down to a single memory chip ⭐— ｜评分 7.8 ｜2026-11-18
交互式可视化项目，可逐层拆解 Voyager 1 至单颗存储芯片，并展示 RTG 钚球与金唱片封面说明。（信息有限，基于摘要）
链接：https://rshekhar.com/voyager/


## 空间攻防

### Effects of a Nuclear Detonation in Low Earth Orbit ⭐— ｜评分 8.8 ｜2026-11-17
arXiv 论文，评估低轨核爆对卫星、辐射环境与轨道碎片的连锁效应。（信息有限，仅基于标题）
链接：https://arxiv.org/abs/2611.09827

> **深入（技术）**：LEO 核爆的破坏机制与高空电磁脉冲（HEMP）和高能粒子注入两条链路相关：瞬发伽马与中子流直接损伤未加固电子器件，而爆后形成的人工辐射带可在数月到数年内持续俘获高能电子，对中低轨卫星造成累积剂量损伤。更棘手的是碎片级联——爆点附近的结构解体产生大量可追踪与不可追踪碎片，触发自维持碰撞风险。该研究的价值在于把"单次事件—环境扰动—星座失效"串成可量化的评估链，对星座抗辐射加固等级、轨道高度选择与在轨备份策略都有直接输入意义。政策层面，此类研究也是外空武器化讨论中"可逆/不可逆效应"论证的技术底稿。

### Russia reportedly planned mass-casualty attack in Poland to be blamed on Ukraine ⭐— ｜评分 9.2 ｜2026-11-18
地缘安全报道，与航天无直接技术关联，仅作安全态势背景记录。（信息有限）
链接：https://www.yahoo.com/news/world/articles/russia-reportedly-planned-mass-casualty-090500574.html

### Ukraine uses own guidance system to strike Crimean Bridge without Starlink ⭐— ｜评分 5.7 ｜2026-11-18
报道称乌方使用自研制导系统完成对刻赤桥的打击，未依赖 Starlink/Starshield。（信息有限）
链接：https://united24media.com/war-in-ukraine/ukraine-uses-its-own-missile-guidance-system-to-strike-the-4-billion-crimean-bridge-without-starlink-or-starshield-24469

### Ukraine blew up bridge using relay drones to bypass Starlink limits ⭐— ｜评分 5.4 ｜2026-11-19
Ars Technica 报道称通过中继无人机绕过 Starlink 地理围栏限制，属战术通信层面的工程规避。（信息有限）
链接：https://arstechnica.com/gadgets/2026/11/ukraine-blew-up-putins-bridge-using-relay-drones-to-bypass-starlink-limits/

> 注：上述两条为同一事件的不同技术侧报道，信息未经独立核实，仅作态势参考。


## 控制与分系统

### nasa/spacewasm v0.8.0-rc.2 ⭐— ｜评分 4.2 ｜2026-11-20 🆕
NASA 开源项目 spacewasm 发布候选版本，更新含 CI 基准测试与工作流 YAML 修复。（信息有限，基于 release notes）
链接：https://github.com/nasa/spacewasm/releases/tag/v0.8.0-rc.2

> **深入**：WebAssembly 进入星载软件栈的意义在于沙箱化与可移植性——同一载荷算法可在不同处理器架构上以受限执行环境运行，降低飞行软件认证的重复成本。本次更新以 CI 基准与工作流修复为主，属工程成熟度推进而非能力跃迁；对关注星上软件架构的团队，值得跟踪其后续是否引入确定性执行与 WCET 分析支持。

### nasa/fprime-gds v4.4.2a1 ⭐— ｜评分 4.2 ｜2026-11-19
F' 框架地面数据系统更新：修复 GDS 浅色模式按钮显示、chrono 插入复杂度优化至 O(1)、放弃 Python 3.9 支持并测试 Python 3.14。（基于 release notes）
链接：https://github.com/nasa/fprime-gds/releases/tag/v4.4.2a1


## 航天前沿与新方法

### JARVIS: An Agent That Designs, Builds, and Tests Circuit Boards on Its Own ⭐— ｜评分 6.2 ｜2026-11-19
具身 AI agent 自主完成电路板设计、制造与测试闭环，面向电力电子硬件迭代。（基于摘要）
链接：https://arxiv.org/abs/2611.26503v1

> **深入**：这是本期与航天硬件研制最贴近的 agent 工作——电力电子是星上电源、电推进驱动与载荷供电的共同基础，而其开发长期依赖人工"设计—打样—测试—改版"循环。JARVIS 的具身闭环若可复现，对缩短单机研制周期、降低对资深硬件工程师的依赖有直接价值；风险在于测试环节的物理不确定性（器件批次差异、热漂移）是否被 agent 的决策逻辑充分覆盖，论文未在摘要中给出失败模式统计。

### TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs ⭐— ｜评分 6.2 ｜2026-11-19
提出以真实实验室的数字孪生为环境，评估 AI 科学家在"执行流程—选择测量—形成结论"三层能力上的表现。（基于摘要）
链接：https://arxiv.org/abs/2611.26248v1

### From Seed to BLOOM: Autonomously Growing a Better Out-of-Order Core ⭐— ｜评分 6.2 ｜2026-11-19
以自主生长方式在面积与频率约束下改进乱序处理器核设计，属敏捷硬件研制方法探索。（基于摘要）
链接：https://arxiv.org/abs/2611.26517v1

### AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher ⭐— ｜评分 6.2 ｜2026-11-19
让同一模型兼任教师与学生的自主后训练方法，关注成功轨迹中的无效行为筛选。（基于摘要）
链接：https://arxiv.org/abs/2611.26510v1

### Tracing Magnetic Helicity in Interplanetary Space（2024-03-23 ICME 多航天器分析）⭐— ｜评分 6.2 ｜2026-11-19
结合遥感与就地测量，追踪一次 ICME 事件从太阳到地球的磁螺度演化，属空间天气物理研究。（基于摘要）
链接：https://arxiv.org/abs/2611.26455v1

### A Tensor-Algebraic No-Go Theorem for High-Dimensional Photonic GHZ States（AlphaProof Nexus 发现）⭐— ｜评分 6.2 ｜2026-11-19
以 AI 辅助证明工具发现光子 GHZ 态的不可行定理，展示形式化方法在量子光学中的发现能力。（基于摘要）
链接：https://arxiv.org/abs/2611.26300v1

### SKILL.PNG: Learning Agent Skills in Pixel Space ⭐— ｜评分 6.2 ｜2026-11-19
将 agent 技能从离散文本指令迁移到像素空间表示，以支持连续化技能学习。（基于摘要）
链接：https://arxiv.org/abs/2611.26296v1

### FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving ⭐— ｜评分 6.2 ｜2026-11-19
通过复用预测减少越野场景下 VLA 模型的重复多模态推理开销。（基于摘要）
链接：https://arxiv.org/abs/2611.26242v1

### Frontier models need only one text to unmask its human or AI author ⭐— ｜评分 6.2 ｜2026-11-19
零样本单文本条件下，前沿模型可分层判断作者身份（人类/AI/具体来源）。（基于摘要）
链接：https://arxiv.org/abs/2611.26216v1

### Reward misalignment as an opportunity for materials discovery ⭐— ｜评分 6.2 ｜2026-11-19
将生成式材料发现中奖励与专家判断的偏离重新解释为探索信号而非纯失败。（基于摘要）
链接：https://arxiv.org/abs/2611.26186v1

### SpatialScout-V2: Can VLM Agents Actively Explore Real-World 3D Scenes and Localize Objects? ⭐— ｜评分 6.2 ｜2026-11-19
评估 VLM agent 在真实三维场景中主动采集视觉证据并完成目标定位的能力。（基于摘要）
链接：https://arxiv.org/abs/2611.26177v1

### ClosureBench: A Benchmark for Reasoning under Closure Assumptions ⭐— ｜评分 6.2 ｜2026-11-19
针对不完整记录下"缺失即未知/缺失即假"的推理假设建立基准。（基于摘要）
链接：https://arxiv.org/abs/2611.26335v1

### DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease ⭐— ｜评分 6.2 ｜2026-11-19
研究 agent 如何识别有意义的知识缺口并判断可用数据能否解决，以阿尔茨海默病为案例。（基于摘要）
链接：https://arxiv.org/abs/2611.26343v1

### Learning to Defer under Expert Drift ⭐— ｜评分 6.2 ｜2026-11-19
在专家能力随时间漂移的条件下重构"学习 defer"框架，面向人机协同安全决策。（基于摘要）
链接：https://arxiv.org/abs/2611.26440v1

### Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models ⭐— ｜评分 6.2 ｜2026-11-19
为检索增强 VLA 模型的测试时自适应引入风险控制，避免无参数更新下的性能退化。（基于摘要）
链接：https://arxiv.org/abs/2611.26438v1

### PlayCraft: Designing Engaging Games from Agent Play Experience ⭐— ｜评分 6.2 ｜2026-11-19
利用 agent 试玩经验为"精通感"设计游戏，属 agent 驱动的生成式内容方法。（基于摘要）
链接：https://arxiv.org/abs/2611.26624v1

### Represented but misread: Post-training changes how language models read out what they represent ⭐— ｜评分 6.2 ｜2026-11-19
用线性探针与信号检测对比，区分后训练改变的是"表示"还是"读出"。（基于摘要）
链接：https://arxiv.org/abs/2611.26584v1

### ROGUE-AI: Replication of Agentic Security Events ⭐— ｜评分 6.2 ｜2026-11-19
针对 LLM agent 真实故障事件（如删除文件、代付）建立审计与调查的可复现方法。（基于摘要）
链接：https://arxiv.org/abs/2611.26553v1

### FLUID: Flexible, Evidence-Grounded Situated Task Guidance ⭐— ｜评分 6.2 ｜2026-11-19
面向实时任务引导的灵活响应与时机构建，允许 agent 在适当时保持沉默。（基于摘要）
链接：https://arxiv.org/abs/2611.26491v1

### Reasoning-Trace Analysis Using LLMs for Interpretable Q-Matrix Construction ⭐— ｜评分 6.2 ｜2026-11-19
用 LLM 推理轨迹分析提升 Q 矩阵构建的可解释性，属教育测量方法。（基于摘要）
链接：https://arxiv.org/abs/2611.26422v1

### How to Effectively Manage the Energy in Residential Systems ⭐— ｜评分 6.2 ｜2026-11-19
住宅能源管理方法的开发与对比，属能源系统优化研究。（基于摘要）
链接：https://arxiv.org/abs/2611.26412v1

### Democratizing Cross-Project Knowledge for Water Governance: an Agentic AI Ecosystem ⭐— ｜评分 6.2 ｜2026-11-19
以 agentic AI 生态整合欧盟水治理项目分散知识，属跨项目知识组织方法。（基于摘要）
链接：https://arxiv.org/abs/2611.26398v1

### To predict or to persist: decoherence in a spin-qubit quantum reservoir ⭐— ｜评分 6.2 ｜2026-11-19
六比特自旋链在马尔可夫耗散下的学习行为模拟，研究退相干与可观测量选择的影响。（基于摘要）
链接：https://arxiv.org/abs/2611.26215v1

### Backbone Matters: Benchmarking Encoder-Decoder Networks for Semantic Segmentation on BDD100K ⭐— ｜评分 6.2 ｜2026-11-19
驾驶场景语义分割的编码器-解码器骨干网络基准对比。（基于摘要）
链接：https://arxiv.org/abs/2611.26191v1

### Existence and uniqueness for a coagulation-transport equation ⭐— ｜评分 6.2 ｜2026-11-19
多物种聚合-输运方程的弱解存在性、唯一性与正则性，数学方法论文。（基于摘要）
链接：https://arxiv.org/abs/2611.26500v1

### Show HN: AgentMall – Let your AI agent buy groceries ⭐— ｜评分 6.2 ｜2026-11-19
为个人 agent 构建跨九家杂货商的可靠结账自动化，处理反爬、登录与 OTP。（基于摘要）
链接：https://getagentmall.com


## 今日精讲：JARVIS —— 自主设计-制造-测试电路板的具身 agent

**是什么**：JARVIS 是一个具身 AI agent，目标是把电力电子硬件的"设计—制板—测试—迭代"闭环交给机器自主完成，而非仅做设计辅助。

**技术亮点**：与纯软件 agent 不同，它必须处理物理世界的反馈延迟与不确定性