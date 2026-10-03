# 航天日报 · 2026-10-03

> 数据来源：Hacker News / GitHub / Reddit 公开动态聚合。本期数据以软件与开源生态为主，实体航天任务信息有限，部分条目与航天关联较弱，已按分类如实呈现，未作延伸推断。


## TL;DR

1. **NASA F´ v4.4.0 发布**，新增 WebAssembly 序列器，飞行软件可加载 WASM 编译的指令序列，星上软件灵活性再进一步。
2. **NASA fmdtools v2.5.3** 改进仿真局部时间步行为，支持用户自定义 `default_t` 覆盖默认步长。
3. **Google Project Suncatcher 原型卫星入轨**，探索"数据中心上太空"的技术路径。
4. **SpaceX Crew-13 发射后不足 8 小时对接 ISS**，创美国载人飞行最快对接纪录；X-59 一周内完成 6 架次飞行。
5. **FCC 为卫星互联网释放更多下行频谱**，Starlink 等低轨宽带星座容量有望提升。


## 发射任务

### SpaceX Crew-13 任务：发射后不足 8 小时对接 ISS 🆕
Crew-13 乘组搭乘 SpaceX Dragon "Grace" 飞船，在发射后不到 8 小时内完成与国际空间站的对接，被称为美国载人航天史上最快对接。任务由 Jessica Watkins 担任指令长，其经历从火星沙漠研究站（MDRS）延伸至 ISS 指令岗位。
- 评分：2.5 ｜ 来源：Reddit r/nasa
- 简评：8 小时对接意味着轨道相位窗口与快速交会流程高度优化，对乘组舒适度与应急返回能力均有实际意义。Watkins 的 MDRS→ISS 路径也颇具象征意味。
- 链接：https://www.reddit.com/r/nasa/comments/1wvsu9y/spacex_crew13_astronauts_dock_at_iss_less_than_8/

### NASA X-59 一周完成六架次飞行
X-59 静音超声速验证机在一周内完成创纪录的六次飞行。
- 评分：2.5 ｜ 来源：Reddit r/nasa
- 简评：高频试飞节奏说明该机已进入密集包线扩展阶段，为后续社区噪声实测积累数据。超声速民用的关键不在飞得多快，而在"多安静"。
- 链接：https://www.reddit.com/r/nasa/comments/1ww6not/nasas_x59_completes_record_six_flights_in_one_week/

### NASA 科学气球 campaign 第五只气球升空
NASA 科学气球项目第五只气球发射。
- 评分：2.5 ｜ 来源：Reddit r/nasa
- 简评：气球平台成本低、周转快，是天体物理与大气科学的重要补充手段。
- 链接：https://www.reddit.com/r/nasa/comments/1wumaj5/fifth_balloon_of_nasa_scientific_balloon_campaign/

### NASA 小型卫星发射，推进科学、技术与在轨操作
一批 NASA SmallSats 发射入轨，用于科学探测、技术验证与在轨操作演示。
- 评分：2.5 ｜ 来源：Reddit r/nasa
- 简评：SmallSat 已成为技术快速迭代的主力载体，值得关注其具体载荷与在轨操作验证内容（信息有限）。
- 链接：https://www.reddit.com/r/nasa/comments/1wvirrk/nasa_smallsats_launch_to_advance_science/


## 卫星与星座

### Starlink for Communities：让用户转售邻居宽带
SpaceX 推出 Starlink for Communities 计划，允许用户向邻居或周边人群按小时、天、周、月出售 Starlink 接入，托管者从中获利。
- 评分：2.5 ｜ 来源：Reddit r/Starlink
- 简评：这是把"最后一公里"分销外包给用户的模式创新，在基础设施薄弱地区可能快速铺开，但也带来计费合规与网络容量管理问题。
- 链接：https://www.reddit.com/r/Starlink/comments/1wva3o9/starlink_for_communities/

### FCC 为卫星互联网释放更多下行频谱
FCC 批准为 Starlink 等卫星互联网服务释放更多下行频谱。
- 评分：2.5 ｜ 来源：Reddit r/Starlink
- 简评：频谱是低轨宽带最稀缺的资源，此次释放直接关系星座容量上限与单位成本。监管节奏正在成为星座竞争力的隐性变量。
- 链接：https://www.reddit.com/r/Starlink/comments/1wuicxd/fcc_clears_more_downlink_spectrum_for_satellite/

### Starlink 用户侧动态（多条）
本期 Reddit r/Starlink 集中出现大量用户讨论：Mini 套件降价至 $149、V3 卫星上线后测速提升、飓风降雨对链路的影响、安装与遮挡排查、账单变化等。
- 评分：2.5 ｜ 来源：Reddit r/Starlink
- 简评：这些是运营侧信号而非技术突破。值得注意的两点：一是 Mini 价格下探与硬件分期说明终端成本仍在快速下降；二是用户自发测速反映 V3 卫星可能已开始贡献容量（官方未确认）。
- 链接：https://www.reddit.com/r/Starlink/comments/1wvwc2x/mini_price_drop_another_support_win/ ｜ https://www.reddit.com/r/Starlink/comments/1wu5ves/speed_increase/


## 空间攻防

### 冷战绝密卫星 URSALA、RAQUEL、FARRAH 揭秘
The Space Review 刊文回顾美国 NRO 三颗冷战时期绝密侦察卫星 URSALA、RAQUEL、FARRAH 的技术细节。讨论区提及其中一颗以 Farrah Fawcett 命名的卫星已在轨解体，并延伸至 NRO 向 NASA 转让退役卫星的历史。
- 评分：9.1 ｜ 来源：Hacker News（thespacereview.com，306 pts / 162 comments）
- 简评：这类解密史料的价值在于揭示当年在器件水平受限条件下实现的系统能力——光学、数据传输、姿态稳定的工程取舍，对今天的载荷设计仍有参照意义。讨论区关于"几十年前就部署了如此超前技术"的感慨，本质上指向的是系统工程能力而非单点器件。
- 链接：https://www.thespacereview.com/article/4951/1

### 冷战间谍卫星在轨解体
一颗冷战时期以 Farrah Fawcett 命名的间谍卫星在轨解体。
- 评分：5.0 ｜ 来源：Hacker News（gizmodo.com）
- 简评：老旧失效航天器解体是轨道碎片的重要来源，与上一条互为背景。政策层面再次提示在轨解体事件监测与碎片编目的必要性。
- 链接：https://gizmodo.com/a-cold-war-spy-satellite-named-after-farrah-fawcett-just-blew-apart-in-orbit-2000819282

### 冷战间谍活动为东德经济贡献 46 亿美元
研究称冷战期间间谍活动为东德经济带来约 46 亿美元收益。
- 评分：4.2 ｜ 来源：Hacker News（popsci.com）
- 简评：情报活动的经济量化研究，属军备与情报史范畴，与航天技术关联间接。
- 链接：https://www.popsci.com/technology/cold-war-spy-economy-east-germany/

> 说明：本期空间攻防分类下其余条目（如 GPT-6.1 Sol 模型迭代、Lean 证明教程、BGP 黑洞系统、AI 代码生成等）与航天攻防技术无实质关联，不予展开。


## 控制与分系统

### NASA F´ v4.4.0：WebAssembly 序列器上线
NASA F´（Flight Software Framework）发布 v4.4.0，核心新增 `Svc::WasmSequencer`——通过 spacewasm 解释器（以 Rust/C 外部库形式构建）运行编译为 WebAssembly 的指令序列，支持加载/运行/暂停/恢复/取消、超时、带参数命令等。
- 评分：7.8 ｜ 来源：GitHub（nasa/fprime，verified）
- 简评：把星上指令序列做成 WASM 模块，等于给飞行软件引入了一个可沙箱化、可动态加载的执行层。传统上星上序列是静态表驱动，改动需重新上传甚至重新认证；WASM 序列器让"任务规划→序列编译→在轨加载"这条链路更接近地面软件迭代节奏。对深空长周期任务尤其有价值——发射后仍能重构操作逻辑。风险在于沙箱安全边界与实时性保证，需看后续认证路径。
- 链接：https://github.com/nasa/fprime/releases/tag/v4.4.0

### NASA fmdtools v2.5.3：仿真时间步行为改进
fmdtools 发布 v2.5.3，主要改进 Simulables 的局部时间步行为，用户可通过 `default_t` 字典覆盖默认局部时间步，而非必须扩展。
- 评分：7.8 ｜ 来源：GitHub（nasa/fmdtools，verified）
- 简评：fmdtools 面向系统韧性与故障传播分析，时间步控制的灵活性直接影响多速率系统仿真的精度与效率。属工具链层面的稳健改进。
- 链接：https://github.com/nasa/fmdtools/releases/tag/v2.5.3

### NASA cumulus-gap-detection v2.0.6
cumulus-gap-detection 发布 v2.0.6。
- 评分：7.8 ｜ 来源：GitHub（nasa，verified）
- 简评：发布说明仅一行，具体变更内容有限（信息有限）。从项目名看与数据 gap 检测相关，属地面数据系统工具。
- 链接：https://github.com/nasa/cumulus-gap-detection/releases/tag/v2.0.6


## 航天前沿与新方法

### Google Project Suncatcher 原型卫星入轨
Google 宣布其 Project Suncatcher 原型卫星已进入轨道。
- 评分：7.0 ｜ 来源：Hacker News（blog.google，49 pts / 52 comments）
- 简评：Suncatcher 指向"太空数据中心"这一前沿命题——把算力放到轨道上，利用持续太阳能与辐射散热。原型入轨说明 Google 至少在验证关键环节。但该方向的核心矛盾未变：发射成本、在轨维护、与地面数据中心的带宽瓶颈。讨论区反应两极，值得持续跟踪其后续技术披露。
- 链接：https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-prototype/

### ESP32 被挖出隐藏 SDR 能力
多个独立项目发现 ESP32 微控制器存在未公开的软件定义无线电能力，可绕过固定 WiFi/蓝牙功能，直接捕获原始 IQ 基带采样。讨论指出大量 1 美元级无线 IC 都具备强大 SDR 潜力，但因认证、合规与出口管制原因永远不会被官方文档化；目前把 80MSPS@10bit 级数据传到计算机仍需 FPGA+USB3。
- 评分：9.4 ｜ 来源：Hacker News（rtl-sdr.com，280 pts / 63 comments）
- 简评：这条对航天有间接但真实的启示——低成本商用器件的"非文档化能力"是双刃剑。一方面，立方星与探空火箭团队常靠这类器件压低成本；另一方面，出口管制与合规风险随之而来。讨论区关于"认证/合规导致能力永不公开"的判断，正是航天供应链中 COTS 器件选型的核心痛点。
- 链接：https://www.rtl-sdr.com/various-projects-independently-find-hidden-sdr-capabilities-in-esp32-microcontrollers/

### 其他前沿方法类条目
- **Muse Gadgets**（评分 9.1，gadgets.muse.ai）：AI 硬件相关，与航天无直接关联。
- **Meta Muse 用于网页抓取**（评分 8.2）：AI 工具应用。
- **荷兰计算机博物馆**（评分 8.2）：计算史。
- **Kanmaps**（评分 4.4）：以游戏技能树形式呈现产品路线图，其"依赖关系可视化"思路对航天型号研制流程编排有隐喻价值，但本身非航天项目。
- 链接：https://gadgets.muse.ai ｜ https://sigh.dev/posts/metas-muse-is-fantastic-for-web-scraping/ ｜ https://aresluna.org/dutch-computer-museums/ ｜ https://kanmaps.com/show


## 今日精讲：NASA F´ WebAssembly 序列器

**是什么。** F´（F Prime）是 NASA 喷气推进实验室开源出来的飞行软件框架，已被用于多个立方星与小行星任务。v4.4.0 引入的 `Svc::WasmSequencer` 允许把指令序列编译成 WebAssembly 模块，在星上通过 spacewasm 解释器执行，支持加载、运行、暂停、恢复、取消以及超时控制。

**技术亮点。** 关键在于三点：其一，**沙箱化**——WASM 天然的内存隔离与确定性执行边界，让动态加载的序列不会破坏主飞行软件；其二，**语言无关**——序列可以用多种语言编写后编译到同一目标；其三，**动态性**——序列成为可替换模块，而非烧录进固件的静态表。

**解决什么问题。** 传统星上序列是静态的，任何操作逻辑变更都需要重新生成、上传、验证，周期长、风险高。深空任务一旦发射，操作模式基本冻结。WASM 序列器把"操作逻辑"从"飞行软件"中解耦出来，使发射后的任务重构成为常规操作而非重大工程事件。

**未来潜力。** 如果这条路径走通，星上软件将呈现"内核稳定 + 逻辑可热更新"的分层结构，这与地面云原生的演进方向一致。对长周期深空任务、在轨服务、以及需要频繁调整观测策略的科学卫星，价值尤为明显。配合 AI 规划器，甚至可能实现"地面生成序列→编译→上传→在轨执行"的半自动闭环。

**潜在风险。** 首要是**认证**。航天飞行软件的认证体系建立在静态可分析性之上，动态加载代码天然与这一前提冲突。其次是**实时性**——解释执行相比原生代码有开销，硬实时任务仍需原生路径。第三是**安全边界**——沙箱再强也有攻击面，尤其当序列来源涉及多方协作时。

**与同类对比。** 传统方案如 NASA 的 SASF（Stored Command）或各家星务软件的指令表，本质是数据而非代码；欧洲航天局与部分商业公司探索过脚本引擎（如 Lua）上星，但脚本引擎的隔离性与可移植性不如 WASM。F´ 此举的差异化在于：它把 WASM 这一已被浏览器生态充分验证的沙箱标准引入飞行软件，兼顾了安全性与生态成熟度。

**一句话判断。** 这是本期最具未来潜力的一项——它不改变任何单机性能指标，但可能改变星上软件的演进方式。


## 数据说明

本期数据中，Hacker News 条目占绝大多数，其中相当一部分（CSS 主题、自行车博物馆、Racket 会议、macOS bug、癌症研究、订阅制游戏等）与航天无实质关联。本文按写作要求分类组织，对无航天关联的条目未强行归入，仅在相关分类下作必要说明。Reddit 条目以 Starlink 用户讨论为主，技术密度较低，已合并处理。GitHub 条目均为 NASA 官方仓库发布，信息可靠但部分发布说明极简，已标注"信息有限"。