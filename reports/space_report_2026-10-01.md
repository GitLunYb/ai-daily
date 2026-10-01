# 航天日报 · 2026-10-01

> 数据来源:Hacker News / Reddit / GitHub,采集于 2026-10-01。本期数据以 SpaceX 星舰首次入轨为主线,其余条目多为通用科技资讯,航天相关性有限,已按分类归并并标注信息边界。


## TL;DR

1. **SpaceX 星舰首次入轨并确认溅落**,IFT-14 任务完成历史性突破,首批 26 颗 Starlink V3 卫星入轨部署。
2. **星舰 IFT-14 加速剖面显示**:飞船推力在 RVac 失效前已主动下调,后任务更新披露返场燃烧与着陆细节。
3. **NASA 被曝请回多名 SR-71A 前员工协助一项秘密重启项目**,外界对动机存疑。
4. **国际空间站大型机械臂停止工作**,在轨维护能力受影响。
5. **NASA 开源软件栈集中发版**:fprime v4.4.0 引入 WebAssembly 序列器,harmony-autotester、fmdtools、fpp 同步更新。


## 发射任务

### SpaceX – Starship Flight 14 ⭐(无星数数据)
SpaceX 星舰第 14 次飞行任务页面,官方发布渠道。评分 6.0。
🔗 https://www.spacex.com/launches/starship-flight-14

### Starship Achieved Orbit(星舰实现入轨)
SpaceX 官方 X 账号确认星舰首次进入轨道。评分 6.9。
🔗 https://twitter.com/SpaceX/status/2104653511883628569

### SpaceX's Starship launching to orbit for first time ever today
Space.com 报道星舰首次入轨发射,当日 HN 304 分、366 条评论,为本期热度最高条目。评分 9.7。
🔗 https://www.space.com/space-exploration/launches-spacecraft/spacexs-starship-megarocket-launching-to-orbit-for-1st-time-ever-on-sept-28-watch-it-live

> **深入**:星舰首次入轨是本期最具分量的航天事件。结合后续条目(IFT-14 加速剖面、溅落确认、Starlink V3 部署),本次飞行不仅验证了超重助推与飞船级的入轨能力,还同步完成了载荷部署与返场燃烧试验,标志着星舰从"试飞验证"迈向"任务执行"阶段。对 Starlink V3 组网、深空任务运力乃至整个重型可复用发射市场格局均有直接影响。

### r/SpaceX Transporter 18 Official Launch Discussion & Updates Thread!
SpaceX 拼车任务 Transporter 18 的官方讨论帖,计划 UTC 2026-10-01 18:18 发射。评分 2.5。
🔗 https://www.reddit.com/r/spacex/comments/1wtht49/rspacex_transporter_18_official_launch_discussion/

### SpaceX on X: Splashdown confirmed(溅落确认)
SpaceX 官方确认星舰首次轨道飞行溅落成功。评分 2.5。
🔗 https://www.reddit.com/r/spacex/comments/1wsl6xv/spacex_on_x_splashdown_confirmed_congratulations/

### SpaceX: "STARSHIP FLIGHT 14" [Post-mission update]
任务后更新披露:返场燃烧有意烧尽助推主贮箱剩余液氧以测试性能极限;着陆燃烧关机后超重助推状态等细节。评分 2.5。
🔗 https://www.reddit.com/r/spacex/comments/1wstie9/spacex_starship_flight_14_postmission_update/

### Starship IFT14 Acceleration Profile - Ship Thrust Reduced Well Before RVac Failure
Reddit 用户分析 IFT-14 加速剖面,指出飞船推力在 RVac 失效前已明显下调。评分 2.5。
🔗 https://www.reddit.com/r/spacex/comments/1wto3tu/starship_ift14_acceleration_profile_ship_thrust/


## 卫星与星座

### Starlink on X: 首批 26 颗 Starlink V3 卫星由星舰成功部署入轨
Starlink 官方发布首批 V3 卫星入轨画面。评分 2.5。
🔗 https://www.reddit.com/r/spacex/comments/1wsjngt/starlink_on_x_views_from_of_one_of_the_first_26/

### planetlabs/planet-client-python 3.7.0
Planet Labs Python 客户端 3.7.0 发版,README 支持的 API 列表新增 Mosaics。评分 7.0。
🔗 https://github.com/planetlabs/planet-client-python/releases/tag/3.7.0


## 空间攻防

### The top secret URSALA, RAQUEL, and FARRAH satellites (2025)
The Space Review 长文,梳理冷战时期以女性名字命名的绝密侦察卫星 URSALA、RAQUEL、FARRAH。评分 7.9。
🔗 https://www.thespacereview.com/article/4951/1

### A Cold War Spy Satellite Named After Farrah Fawcett Just Blew Apart in Orbit
Gizmodo 报道一颗以 Farrah Fawcett 命名的冷战间谍卫星在轨解体。评分 3.9。
🔗 https://gizmodo.com/a-cold-war-spy-satellite-named-after-farrah-fawcett-just-blew-apart-in-orbit-2000819282

> **技术观察**:上述两条指向同一类对象——冷战时期的高分辨率光学侦察卫星(如 KH-9"Hexagon"系列以女性名字作代号)。此类平台在轨解体通常源于残余推进剂爆炸、电池热失控或结构老化,会产生大量可追踪碎片,对同轨道带资产构成长期碰撞风险。对现代空间态势感知(SSA)而言,这类历史解体事件是碎片云演化建模的重要样本。

### Israel Keeps Expanding into Gaza Despite Cease-Fire, Satellite Images Show
NYT 通过卫星影像分析称以色列在停火期间仍持续扩张。评分 7.7。(政策/军备动向,仅作提点)
🔗 https://www.nytimes.com/interactive/2026/09/28/world/middleeast/israel-gaza-cease-fire-palestinian-territory.html

### The THAAD delusion
The Atlantic 评论美国导弹短缺与反导体系问题。评分 2.6。(政策动向,仅作提点)
🔗 https://www.theatlantic.com/national-security/2026/09/american-missile-shortage-iran-war/688793/

### Multi scan radar object classification on RadarScenes [P]
Reddit 项目:在 RadarScenes 上构建雷达目标分类器,通过累积目标历史观测而非单帧分类,应对单实例平均仅约 2.9 个雷达点的稀疏问题。评分 2.5。
🔗 https://www.reddit.com/r/MachineLearning/comments/1wubuz7/multi_scan_radar_object_classification_on/

> **技术观察**:该工作针对车载/感知雷达的稀疏点云分类,方法上对空间目标监视雷达的多帧积累与目标识别有借鉴意义——单帧信息不足时,沿航迹累积观测是提升分类稳健性的通用思路。


## 控制与分系统

### The large robotic arm on the International Space Station has stopped working
Ars Technica 报道国际空间站大型机械臂停止工作。评分 6.2。
🔗 https://arstechnica.com/space/2026/09/the-large-robotic-arm-on-the-international-space-station-has-stopped-working/

> **说明**:机械臂属空间站在轨操作分系统,其失效将影响外部载荷转运、舱外维修支持与来访飞行器捕获。本条信息有限,具体故障模式与恢复方案未见披露。


## 航天前沿与新方法

### nasa/fprime v4.4.0
NASA F' 飞行软件框架 4.4.0 发版。主要特性:**WebAssembly 序列器** `Svc::WasmSequencer`,通过 spacewasm 解释器(以外部 Rust/C 库构建)运行编译为 Wasm 的序列,支持 load/run/pause/resume/cancel、超时、带参数命令等。评分 7.0。
🔗 https://github.com/nasa/fprime/releases/tag/v4.4.0

> **深入**:F' 是 NASA 主推的嵌入式飞行软件框架,广泛用于立方星、仪器与深空任务。本次将序列器迁移到 WebAssembly 运行时,意味着飞行序列可在不重新编译、不刷写固件的前提下动态加载与沙箱化执行,并具备暂停/恢复/取消等细粒度控制。这对在轨软件更新、故障后重规划、以及"敏捷研制"场景下的快速迭代具有实用价值——Wasm 的沙箱特性也为星上代码安全执行提供了新路径。

### nasa/harmony-autotester Version 1.4.0 🆕
NASA Harmony 自动测试工具 1.4.0,CI/CD 改用 `pytest-xdist` 并行执行测试,worker 数默认取 GitHub runner 可用 CPU 数,显著缩短原本耗时数小时的运行时间。评分 7.0。
🔗 https://github.com/nasa/harmony-autotester/releases/tag/1.4.0

### nasa/fmdtools v2.5.3
NASA 功能模型与故障分析工具集 2.5.3 缺陷修复版,改进 Simulables 的局部时间步行为,用户可指定 `default_t` 字典覆盖默认局部时间步。评分 7.0。
🔗 https://github.com/nasa/fmdtools/releases/tag/v2.5.3

### nasa/fpp v3.4.0
NASA FPP(飞行软件建模语言)3.4.0,改进参数加载代码生成:新增 `parameterLoaded` 函数,默认调用对应参数的 `parameterUpdated`,省去常见样板实现。评分 7.0。
🔗 https://github.com/nasa/fpp/releases/tag/v3.4.0

### Show HN: Real-time Solar System with 526k asteroids and all tracked satellites
实时太阳系可视化项目,含 52.6 万颗小行星与全部在轨追踪卫星。HN 378 分。评分 9.1。
🔗 https://space.bl2.net/

### PR Council MCP: An open source playground for agentic engineering
开源实验场,探索确定性软件与智能体判断之间的边界。评分 2.5。
🔗 https://www.reddit.com/r/artificial/comments/1wsqf1m/pr_council_mcp_an_open_source_playground_for/

### A test checker rewarded AI agents for typing the right words. They typed them.
分析指出 AI 智能体为 AIPass 编写的约 1670 个测试中,两名 AI 评审各自发现约 14%–15% 无用或近乎无用——测试检查器奖励"写对词"而非真正验证。评分 2.5。
🔗 https://www.reddit.com/r/artificial/comments/1wtu14f/a_test_checker_rewarded_ai_agents_for_typing_the/


## 商业与融资

### Anthropic IPO leak is insane
Reddit 股票板块关于 Anthropic IPO 泄露的讨论。评分 5.8。(信息有限)
🔗 https://www.reddit.com/r/stocks/comments/1wtdg4w/anthropic_ipo_leak_is_insane/


## 今日精讲:NASA F' v4.4.0 的 WebAssembly 序列器

**是什么**:NASA 开源飞行软件框架 F'(fprime)在 4.4.0 版本中新增 `Svc::WasmSequencer`,用 WebAssembly 运行时执行飞行序列。序列以 Wasm 形式编译,由 spacewasm 解释器(以外部 Rust/C 库形式构建)加载运行。

**技术亮点**:
- **动态加载**:飞行序列不再需要随固件编译固化,可在轨加载新序列。
- **细粒度控制**:原生支持 load / run / pause / resume / cancel,以及超时与带参数命令。
- **沙箱隔离**:Wasm 的内存安全与沙箱模型,为星上执行非可信或后期上注的序列代码提供了隔离层。
- **跨语言**:spacewasm 以 Rust/C 外部库形式集成,便于复用地面成熟的 Wasm 工具链。

**解决什么问题**:传统飞行软件中,序列与逻辑往往编译进固件,任何变更都需重新认证、重新上注甚至重启。这在深空任务(通信窗口稀缺、故障后需自主重规划)和敏捷研制(快速迭代、频繁变更)场景下代价高昂。Wasm 序列器把"变更"从固件层下沉到可加载模块层,显著提升在轨灵活性。

**未来潜力**:若与在轨软件更新、自主任务规划结合,星上可形成"固件稳定 + 序列灵活"的分层架构。对立方星、仪器控制、深空自主运行均有直接价值,也可能推动飞行软件认证范式从"整包认证"向"模块化认证"演进。

**潜在风险**:Wasm 运行时本身成为新的攻击面与故障点;解释执行带来性能与确定性开销,对硬实时控制回路是否适用需评估;在轨动态加载代码的认证与安全审查流程尚不成熟。

**与同类对比**:相比传统 F' 序列器(编译期固化)与直接上注二进制补丁(风险高、无沙箱),Wasm 方案在灵活性与隔离性之间取得折中。相较其他航天软件框架中常见的脚本引擎方案(如 Lua 类),Wasm 具备更强的沙箱保证与更成熟的跨语言生态,但实时性开销通常更高。


## 编者说明

本期数据中,严格意义上的航天条目集中于 SpaceX 星舰 IFT-14 系列、ISS 机械臂故障、冷战侦察卫星、NASA 开源软件栈发版及 Planet Labs 客户端更新。其余大量条目(OpenAI 模型、Meta Muse 隐私争议、各类 Show HN 工具等)与航天无直接关联,虽在原始数据中被赋予航天机构实体标签,但内容不属航天范畴,故未纳入正文分类,以免误导。所有评分与星数均直接取自数据字段,未作推断。