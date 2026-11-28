# 航天日报 · 2026-11-28

> 数据采集窗口：2026-11-25 至 2026-11-28。本期数据源以 Hacker News 与 arXiv 为主，航天实体标签（SpaceX、ESA、NASA、CASC 等）由采集端自动标注，部分条目与航天主题关联较弱，已在正文中据实说明。所有评分、星数均直接取自数据，未作补全。

---

## TL;DR

1. **FCC 批准 SpaceX 部署 100 万颗"轨道数据中心"卫星**，多家媒体同日跟进，欧洲南方天文台（ESO）随即发表声明，暗夜天空与轨道资源争议升温。
2. **Hera 任务传回 DART 撞击现场首批图像**，人类首次小行星动能撞击试验的碎片与撞击坑细节开始成像。
3. **欧洲最大卫星工厂在比利时投产**，明确以对标 Starlink 为目标，欧洲星座产能竞赛进入实体化阶段。
4. **NASA 火星舰队约半数因技术问题离线**，老旧深空资产的运维压力显性化。
5. **arXiv 出现"燃料即身份"的星间激光链路认证方案**，针对密钥全失陷场景，是本期最具航天专属价值的技术新思路。

---

## 空间攻防 Space Defense & Security

### First images of the impact of DART asteroid deflection experiment ⭐— ｜评分 9.6 ｜2026-11-26
Hera 任务抵达 DART 撞击现场并传回首批撞击后图像，用于评估动能撞击造成的小行星结构改变。(信息有限，摘要仅含来源与讨论量，未披露成像细节)
**简评**：行星防御从"撞得动"进入"看得清"阶段，Hera 的近距离测绘是判断动量传递效率能否外推到真实威胁目标的关键一环。
🔗 https://arstechnica.com/space/2026/11/europes-hera-mission-returns-to-the-chaotic-scene-of-a-cosmic-smashup/

> **深入**：DART 只证明了"能改变轨道"，但偏转模型的工程可用性取决于 β（动量增强因子）能否被独立测量。Hera 携带的激光测高、多光谱成像与雷达将重建 Dimorphos 的质量、形状与撞击坑形貌，把一次单点实验变成可标定的物理模型。对任何未来的偏转决策链而言，这一步的价值高于撞击本身。

### OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster ｜评分 9.9 ｜2026-11-26
讨论指向 GPT-6.2 系列模型的使用限额调整与计费口径问题。(信息有限，摘要为论坛讨论摘录，与航天攻防无实质技术关联)
**简评**：本条被采集端归入"空间攻防"，实为 AI 产品运营话题，建议读者按 AI 行业动态看待，不构成航天攻防情报。
🔗 https://twitter.com/thsottiaux/status/2125784147889393806

### GPT 6.2 Astra Solves a Historical Mystery ｜评分 9.9 ｜2026-11-25
据称 GPT-6.2 Astra 自主识别出耶鲁 Beinecke 图书馆所藏 1808 年匿名速写本的作者。(信息有限，摘要为论坛讨论摘录)
**简评**：属 AI 用于史料鉴定的应用案例，与航天无直接关系；若此类推理能力迁移到遥感影像判读与情报融合，才具备攻防侧意义，目前尚无该证据。
🔗 https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical

### Proposed unification of quantum gravity and General relativity ｜评分 5.0 ｜2026-11-26
Reddit 讨论帖，声称 GPT-6 Astra 在物理问题上取得进展。(信息有限，标题与摘要均未提供可核验的技术内容)
**简评**：来源为社交平台讨论，无同行评议支撑，不作为技术条目采信。
🔗 https://www.reddit.com/r/singularity/comments/1y5u48p/openai_and_gpt6_astra_just_tackled_physics_holy/

### Fuel as Identity: Authenticating Inter-Satellite Laser Links after Total Key Compromise ｜评分 4.6 ｜2026-11-25
提出在卫星全部密钥失陷后，利用推进剂消耗特征作为物理身份凭证，对星间激光链路进行认证。
**简评**：把"剩余燃料"这一不可伪造、不可复制的物理量转化为身份因子，思路新颖，但工程上受限于燃料测量精度与长期可观测性。
🔗 https://arxiv.org/abs/2611.34470v1

> **深入**：低轨星座的星间光链路是整个系统的骨干，而现有安全模型默认"密钥保密"这一前提。一旦单星被捕获或地面段被渗透，密钥体系整体失效，传统密码学手段无从补救。该文转向物理层：每颗星的推进剂存量与消耗历史由其轨道机动行为唯一决定，攻击者即便拿到全部密钥，也无法复制目标的燃料账本。技术亮点在于把身份认证从"你知道什么"迁移到"你消耗了什么"。潜在风险同样明显——燃料测量在微重力下的精度、长期漂移标定、以及星座规模化后的账本同步，都是尚未验证的环节。与同类工作（基于时钟偏差、器件指纹的物理指纹方案）相比，其优势是不可克隆性更强，劣势是可观测性更差。

---

## 卫星与星座 Satellite & Constellation

### SpaceX wins FCC approval to deploy 1M orbital data center satellites ｜评分 9.1 ｜2026-11-25
FCC 批准 SpaceX 部署最多 100 万颗用于轨道数据中心的卫星。
**简评**：数量级远超现有任何星座规划，监管闸门先于工程可行性打开，后续频谱协调、轨道碎片与天文影响将成为主要制约。
🔗 https://www.cnbc.com/2026/11/25/spacex-fcc-satellite-approval.html

> **深入**：100 万颗的规模已不是"星座"而是"轨道基础设施"的概念。真正的瓶颈不在发射（即便按星舰量级估算，年发射能力与百万颗之间仍存在数量级差距），而在三处：一是轨道壳层容量与碰撞规避的自主化程度；二是散热——真空环境下数据中心的热排散只能靠辐射，单位算力的散热面积远高于地面；三是频谱与地面关口站的聚合带宽。FCC 的批准是必要非充分条件，把它读作"工程时间表"会严重误判。

### US authorizes SpaceX to deploy 1M satellites for data centers in space ｜评分 8.5 ｜2026-11-25
路透社对同一 FCC 批准的报道。
**简评**：与上条为同一事件的不同信源，可交叉印证批准事实，但均未披露部署时间表与分期安排。
🔗 https://www.reuters.com/business/media-telecom/us-authorizes-spacex-deploy-1-million-satellites-data-centers-space-2026-11-25/

### ESO statement on approval of launch of one million space data centres ｜评分 8.6 ｜2026-11-27
欧洲南方天文台就百万颗轨道数据中心获批发表声明。
**简评**：天文界对巨型星座的光污染与射电干扰关切首次以机构声明形式进入监管流程，后续或影响国际暗夜保护政策走向。
🔗 https://www.eso.org/public/news/eso2614/

### Taking on Starlink: Europe's largest satellite factory opens in push to rival ｜评分 4.0 ｜2026-11-26
Aerospacelab 在比利时开设欧洲最大卫星工厂，目标对标 Starlink。
**简评**：欧洲星座短板在产能而非设计，工厂落地是补链的关键一步，但星座组网的发射节奏仍受制于欧洲运载能力。
🔗 https://www.cnbc.com/2026/11/26/starlink-satellites-aerospacelab-factory-belgium.html

### One in 25 Starlink IPs Is a Residential Proxy ｜评分 3.2 ｜2026-11-26
称约每 25 个 Starlink IP 中有一个被用作住宅代理。
**简评**：属网络安全观测，反映卫星宽带出口 IP 的滥用治理问题，与星座技术本身关系有限。
🔗 https://iptrust.co/blog/one-in-25-starlink-ips-is-a-residential-proxy

### State of the UNIONS: Four Milky Way companions discovered in a systematic search for northern Local Group satellites ｜评分 4.6 ｜2026-11-25
基于 UNIONS 巡天 gri 测光系统搜索，新发现四个银河系伴星系。
**简评**：此处 "satellite" 为天文学意义的伴星系，非人造卫星；对暗物质分布与星系形成研究有增量价值。
🔗 https://arxiv.org/abs/2611.34775v1

### AutoRSP: An AI Agent for Radar Sensing Pipeline Design ｜评分 4.6 ｜2026-11-25
提出用 AI 智能体自动设计雷达探测流水线，覆盖软硬件协同。
**简评**：若方法可迁移，对星载 SAR/雷达载荷的快速构型设计有参考意义，但论文面向地面雷达，星载适配性未验证。
🔗 https://arxiv.org/abs/2611.34754v1

### Enhancing Maritime Domain Awareness using Latent Space Representations ｜评分 5.1 ｜2026-11-25
基于 TerraMind 地理空间基础模型的潜空间表征，用于海域态势感知。
**简评**：对海洋监视卫星的下游信息处理有直接借鉴价值，属遥感应用侧的实用方向。
🔗 https://arxiv.org/abs/2611.34899v1

---

## 控制与分系统 Control & GNC（仅卫星）

### Azimuth Pointing and Momentum Management for a Lightweight High-Altitude Balloon Payload ｜评分 4.6 ｜2026-11-25
针对 ALTAIR 高空气球载荷（以积分球作为人造星进行光度定标）的方位指向与角动量管理方法。
**简评**：虽为气球平台，但其"轻量载荷 + 角动量管理 + 精确指向"的组合与卫星姿控问题同构，对低成本定标载荷有参考价值。
🔗 https://arxiv.org/abs/2611.34817v1

> **深入**：ALTAIR 的任务本质是"在天上造一颗已知亮度的假星"，为地面望远镜提供大气干扰校正基准。难点在于积分球必须稳定指向特定地面站点，而气球平台的姿态扰动大、执行机构功率受限。论文给出的方位指向与角动量管理方案，核心是在有限力矩器能力下把扰动谱搬到可控频段。对卫星工程的启示在于：小惯量、低功耗平台的指向控制，往往不是控制律问题，而是执行机构选型与扰动源管理问题。

### Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs ｜评分 4.6 ｜2026-11-25
用物体级三维轨迹先验引导冻结的视觉-语言-动作模型，改善布局变化下的操作鲁棒性。
**简评**：属机器人操作方向，与卫星 GNC 无直接关系；若未来用于在轨服务机械臂的任务规划，需另行验证空间环境适应性。
🔗 https://arxiv.org/abs/2611.34914v1

### SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator ｜评分 4.6 ｜2026-11-25
以免训练的稀疏有序关键位姿替代逐步密集控制，提升 LLM 智能体操作效率。
**简评**：稀疏关键位姿思路与在轨机械臂的"路点级"任务描述有相通之处，但论文场景为地面操作。
🔗 https://arxiv.org/abs/2611.34750v1

### Was the Model Given the Right Action? Auditing and Repairing Action Interfaces in Navigation World Models ｜评分 4.6 ｜2026-11-25
审计并修复导航世界模型中动作接口与训练时不一致的问题。
**简评**：对任何"用世界模型做闭环验证"的工程实践都有方法论价值，包括卫星自主导航的地面仿真验证链。
🔗 https://arxiv.org/abs/2611.34739v1

---

## 航天前沿与新方法 Frontier & Methods

### REE: A Scientific Research Entrance Exam for AI Agents ｜评分 5.1 ｜2026-11-25
提出面向自主科研智能体的"科研入学考试"基准，评估其通过反复实验改进解的能力。
**简评**：科研智能体的评测标准化是当前空白，此类基准对航天研制中的 AI 辅助设计流程有间接参考意义。
🔗 https://arxiv.org/abs/2611.34646v1

### A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models ｜评分 5.1 ｜2026-11-25
针对缺乏大规模部署机队的团队，用失败驱动的方式构建 VLA 模型后训练数据飞轮。
**简评**："失败驱动数据闭环"与航天小样本、高价值任务的数据策略高度契合，方法可迁移至星上自主任务的后训练。
🔗 https://arxiv.org/abs/2611.34698v1

### RoboEvo²: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution ｜评分 5.1 ｜2026-11-25
提出"夹具-策略协同演化"的机器人递归自我改进框架。
**简评**：把工具/夹具纳入演化回路是较新颖的设计，对在轨服务中"工具+策略"联合优化有概念启发。
🔗 https://arxiv.org/abs/2611.34675v1

### Do We Still Need Reinforcement Learning When We Can Read the World Model? ｜评分 5.1 ｜2026-11-25
探讨在可读取世界模型的条件下，强化学习是否仍必要。
**简评**：属方法论层面的反思性工作，对基于模型的自主决策架构选型有参考价值。
🔗 https://arxiv.org/abs/2611.34656v1

### Spectrum Adaptation of AI-Native Autoencoder Communications with Transfer Learning ｜评分 5.1 ｜2026-11-25
用迁移学习实现 AI 原生自编码器通信的频谱自适应。
**简评**：端到端物理层学习在星地链路的频谱动态适配上有潜在应用，但论文未涉及卫星信道特性。
🔗 https://arxiv.org/abs/2611.34942v1

### Make the Adversary Spend More: Stateful Deception as a Cost-Exchange Primitive for AI-Era Cyber Defense ｜评分 5.1 ｜2026-11-25
提出以有状态欺骗作为"成本交换"原语，抬高 LLM 辅助攻击者的代价。
**简评**：成本交换思路可延伸至地面段与测控链路的防御设计，属通用网络安全方法论。
🔗 https://arxiv.org/abs/2611.34770v1

### Attack Policy Selection can Mislead Monitor Evaluators ｜评分 5.1 ｜2026-11-25
指出攻击策略的选择会系统性误导 AI 监控器的评估结论。
**简评**：对任何依赖"红队代理"评估安全监控的体系都是警示，包括星上自主软件的安全验证。
🔗 https://arxiv.org/abs/2611.34934v1

### Drilling for the Radio Neutrino Observatory in Greenland (RNO-G): field performance of BigRAID ｜评分 5.1 ｜2026-11-25
报道格陵兰射电中微子天文台 BigRAID 钻探系统的现场性能。
**简评**：属极地/深冰探测的野外工程，与航天为间接关联（极端环境无人探测技术同源）。
🔗 https://arxiv.org/abs/2611.34772v1

### KEBBABS: Kilometric Enhanced Balloon-Baseline for Axion Birefringence Search ｜评分 5.1 ｜2026-11-25
提出用 30–40 km 高度平流层气球编队，通过激光偏振旋转搜寻超轻轴子暗物质。
**简评**：气球基长基线干涉思路对空间科学载荷编队有借鉴意义，属暗物质探测新方案。
🔗 https://arxiv.org/abs/2611.34927v1

### Tracking Any Point with Agentic Visual Reasoning ｜评分 5.1 ｜2026-11-25
用智能体式视觉推理完成任意点跟踪。
**简评**：点跟踪是遥感视频与在轨目标监视的基础能力，VLM 路线值得关注。
🔗 https://arxiv.org/abs/2611.34943v1

---

## 发射任务 / 商业与融资（据实说明）

本期数据中**未出现可核验的发射任务条目**，故省略该分类。

商业与融资侧，数据中与航天实体相关的条目主要为公司治理与舆情，非融资事件，列此备查：

- **States sue SpaceX to stop Grok from generating child sex images, revenge porn** ｜评分 9.3 ｜2026-11-27
  多州总检察长对 SpaceX（作为 xAI/Grok 母公司）提起诉讼，涉平台生成非法图像。
  **简评**：属法律与合规风险事件，与航天业务无技术关联，但对 SpaceX 的公共事务与估值叙事有外溢影响。
  🔗 https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform

- **Musk makes $18B SpaceX stock pledge for every kid in America** ｜评分