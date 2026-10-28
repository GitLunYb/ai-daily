# 航天日报 · 2026-10-28

> 数据采集窗口：2026-10-25 至 2026-10-27。本期数据以 Hacker News / Reddit / arXiv / GitHub 为主，**绝大多数条目的 entity 字段与内容主题不匹配**（例如 GPT 模型发布被标注为 Relativity Space、ESA），已按内容实质归类，未采信 entity 标签。无 stars 字段数据，故全篇不显示星标。

---

## TL;DR

1. **SpaceX 确认主动限制乌克兰 Starlink 速度/接入**，马斯克称"那个漏洞已被关闭"，服务随后恢复；乌克兰同步宣布与 Nokia、ICEYE 合作建设替代方案。
2. **星链用户遭疑似以色列间谍公司大规模监控**（路透社，verified），安全面成为星座运营的新焦点。
3. **佛罗里达发射暂停至少 6 周**，叠加 Raptor 3 实测推力仅约 230 tf（低于公布的 280 tf），SpaceX 近期节奏承压。
4. **中国"星链对标"星座与遥感星座（Yaogan）持续扩容**；一颗中国成像卫星与本月 63 星拼车任务物体交会距离仅约 130 米。
5. **NASA 的 F Prime 框架发布 fpp v4.0.0a1 模板系统**，星上飞控软件工程化工具链继续迭代。

---

## 发射任务

### Florida launches paused for at least 6 weeks
佛罗里达发射活动至少暂停六周。
**评分 2.5** ｜ 2026-10-27 ｜ [链接](https://www.reddit.com/r/spacex/comments/1xh1h6g/florida_launches_paused_for_at_least_6_weeks/)
**简评**：信息有限，未给出暂停原因。若属实，将对东海岸高密度发射节奏产生实质影响，需等待官方口径确认。

### r/SpaceX Starlink 15-16 Official Launch Discussion & Updates Thread
Starlink 15-16 批次发射讨论帖，计划 UTC 2026-10-27 07:25:51 发射。
**评分 2.5** ｜ 2026-10-25 ｜ [链接](https://www.reddit.com/r/spacex/comments/1xeta4g/rspacex_starlink_1516_official_launch_discussion/)
**简评**：常规组批发射。与上条"佛州暂停"对照阅读，可判断暂停生效时点与影响范围。

### Elon Musk: "We can only reliably get to around 230 t-F with Raptor 3… Raptor 4 will be 300 tons of thrust at sea level"
马斯克称 Raptor 3 可靠工作推力约 230 tf，低于此前公布的 280 tf；Raptor 4 目标海平面 300 tf、质量大致相当。
**评分 2.5** ｜ 2026-10-26 ｜ [链接](https://www.reddit.com/r/spacex/comments/1xg4zul/elon_musk_we_can_only_reliably_get_to_around_230/)
**简评**：**这是本期最具工程含量的一条**。公布指标与"可靠工作指标"之间 18% 的落差，直接压缩上面级性能余量与复用周转裕度；把希望寄托在下一代 Raptor 4 上，意味着推力提升必须在不增质量的前提下完成，对涡轮泵、燃烧室热管理和冷却通道设计提出极高要求。对以"推力/质量比"为核心竞争力的两级完全复用方案而言，这是需要严肃对待的信号。

---

## 卫星与星座

### China's Starlink Rival Is Growing
中国版"星链"对标星座持续扩张。
**评分 2.0** ｜ 2026-10-26 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xgc25h/chinas_starlink_rival_is_growing/)
**简评**：信息有限，未披露具体星座名称、在轨数量与批次。可作为趋势信号记录，不宜据此推断规模。

### China's Yaogan Constellation Grows Bigger
中国遥感（Yaogan）星座规模进一步扩大。
**评分 2.0** ｜ 2026-10-25 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xf0br1/chinas_yaogan_constellation_grows_bigger/)
**简评**：信息有限。Yaogan 系列长期兼具遥感与一定的情报侦察属性，星座化后重访率提升是其核心价值。

### A Chinese imaging satellite and an object from this month's 63-satellite rideshare passed about 130 metres apart
据公开轨道数据，一颗中国成像卫星与本月 63 星拼车任务的某个物体最近距离约 130 米。
**评分 2.0** ｜ 2026-10-27 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xgl31x/a_chinese_imaging_satellite_and_an_object_from/)
**简评**：**值得关注**。130 米在 LEO 已属高风险交会量级，且对方是未受控的拼车遗留物——这类"大批量释放 + 长期滞留"的部署模式正在把碰撞风险从"卫星 vs 卫星"扩展到"卫星 vs 碎片云"。拼车任务方在释放策略与离轨承诺上的工程约束，会成为下一阶段星座运营的隐性成本。

### Ice mission CRISTAL opens its wings
冰层探测任务 CRISTAL 展开翼板（太阳能翼/天线展开）。
**评分 2.0** ｜ 2026-10-26 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xg2u29/ice_mission_cristal_opens_its_wings/)
**简评**：信息有限。CRISTAL 为欧方极地冰与海冰高度计任务，展开动作属总装测试或入轨后关键节点。

### NASA's Swift Mission Ends, Leaves Behind Scientific Bonanza
NASA Swift 伽马暴观测任务结束，留下丰硕科学成果。
**评分 2.0** ｜ 2026-10-25 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xf85pb/nasas_swift_mission_ends_leaves_behind_scientific/)
**简评**：信息有限。Swift 长期承担伽马暴快速定位与多波段后随观测，其退役意味着 GRB 触发响应能力出现空缺，需由后续任务填补。

### Navigation via space junk, magnetic fields, and gravity: The dawn of new navigation tech
利用空间碎片、磁场与重力实现导航——新型导航技术的开端。
**评分 2.0** ｜ 2026-10-27 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xh34rc/navigation_via_space_junk_magnetic_fields_and/)
**简评**：信息有限，但方向值得留意：在 GNSS 拒止环境下，以"环境特征"替代"外部信标"的导航思路，是当前抗干扰 PNT 研究的主流分支之一。

### I built an open-source (AGPLv3) orbital telemetry filter calibrated on 1,657 ILRS laser-ranging passes…
开源轨道遥测滤波器，基于 1,657 次 ILRS 激光测距弧段标定，声称可预测 LEO 的"正午—午夜"径向凹陷（约 -100.5 m），无需经验性 1-CPR 调参，将 7 天盲推漂移降低 99.8%、位保 ΔV 显著下降。
**评分 2.0** ｜ 2026-10-26 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xg60br/i_built_an_opensource_agplv3_orbital_telemetry/)
**简评**：**本期最值得技术侧细读的一条，但需谨慎对待**。1-CPR 经验项长期是精密定轨与位保中的"必要之恶"，用物理模型替代经验拟合在方法论上正确；不过"99.8% 漂移削减"这类指标高度依赖标定集与验证集划分方式，且 ILRS 测距覆盖的轨道类型有限，外推至 VLEO/GEO 的泛化性未经独立验证。建议按"有前景的待复现工作"看待，而非既成结论。

### I built an app that tells you when to go outside to see ISS, Hubble, and Tiangong…（Phoebe）
个人开发的卫星过境预报应用，含 3D 地球与约 1.6 万颗卫星可视化，并集成 Claude 问答。
**评分 2.0** ｜ 2026-10-27 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xgw99b/i_built_an_app_that_tells_you_when_to_go_outside/)
**简评**：信息有限。属科普/爱好者工具，工程价值有限，但"LLM + 轨道数据"的交互形态对地面运控前端有参考意义。

### Interactive planet simulator with ~16k live satellites
交互式行星模拟器，可切换卫星、风场、飞机、船舶等图层，含约 1.6 万颗在轨卫星。
**评分 2.0** ｜ 2026-10-25 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xeyypj/interactive_planet_simulator_with_16k_live/)
**简评**：信息有限。可视化演示项目。

### Meet Europe's New Rocket Salesman
欧洲新任火箭销售负责人。
**评分 2.0** ｜ 2026-10-26 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xft0f1/meet_europes_new_rocket_salesman/)
**简评**：信息有限。反映欧洲发射服务在商业化竞争下的销售体系调整。

### Google Cloud and NASA: Testing robotic systems for deep space missions
Google Cloud 与 NASA 联合测试深空任务机器人系统。
**评分 2.0** ｜ 2026-10-27 ｜ [链接](https://www.reddit.com/r/satellites/comments/1xh6uyt/google_cloud_and_nasa_testing_robotic_systems_for/)
**简评**：信息有限。云侧算力/仿真参与深空机器人验证，属地面支持链路的能力外延。

### 其余（信息有限，仅列条目）
- *Experiments*（2026-10-25）[链接](https://www.reddit.com/r/satellites/comments/1xfeq3j/experiments/) — 标题无实质信息。
- *I want to get into this hobby looking at the GOES weather satellites…*（2026-10-25）[链接](https://www.reddit.com/r/satellites/comments/1xfc038/i_want_to_get_into_this_hobby_looking_at_the_goes/) — 爱好者求助帖。
- *this is my idea atm…two arms that has two cameras…*（2026-10-25）[链接](https://www.reddit.com/r/satellites/comments/1xfe5bn/this_is_my_idea_atm_what_i_was_thinking_is_the/) — 个人构想，非工程方案。

---

## 空间攻防

### Alleged Israeli spy company targeted Starlink users ⭐（verified）
路透社报道，一家被指为以色列间谍公司的机构对 Starlink 用户进行了大规模定向攻击。
**评分 9.1** ｜ 2026-10-27 ｜ [链接](https://www.reuters.com/business/media-telecom/alleged-israeli-spy-company-heavily-targeted-starlink-users-sources-say-2026-10-27/)
**简评**：**本期最高分的实质安全事件**。技术上看，针对卫星互联网用户终端的攻击面与传统运营商截然不同：用户终端（dishy）固件、终端与网关之间的空口链路、以及用户侧 LAN 都是潜在入口，而终端往往部署在缺乏边界防护的战术/野外环境。一旦攻击者能批量识别并定位终端（例如通过信号特征或订阅信息侧信道），"通信安全"就退化为"位置安全"问题——这对军用/政府用户的 OPSEC 是结构性挑战。星座运营方需要把终端固件签名、密钥轮换与异常流量检测提升到与星上载荷同等的安全等级。

### Musk says SpaceX restricted Ukraine's Starlink connection as service restored ⭐（verified）
马斯克表示 SpaceX 限制了乌克兰的 Starlink 连接，随后服务恢复。
**评分 4.5** ｜ 2026-10-25 ｜ [链接](https://www.bbc.com/news/articles/cvx28ljp8n4xo)
**简评**：政策/军备动向，简提。核心问题是商业星座在冲突中的"可用性即权力"，服务条款被用作战术杠杆。

### Elon Musk says he was behind restricting Ukraine's Starlink speed ⭐（verified）
马斯克称其本人主导了对乌克兰 Starlink 限速。
**评分 7.8** ｜ 2026-10-25 ｜ [链接](https://www.chicagotribune.com/2026/10/24/musk-behind-starlink-speed-restriction-in-ukraine/)
**简评**：政策动向，简提。与上条为同一事件的不同信源，限速而非断网，说明存在可调的服务分级机制。

### Musk claims Ukraine violated Starlink service agreement ⭐（verified）
马斯克称乌克兰违反了 Starlink 服务协议。
**评分 5.7** ｜ 2026-10-25 ｜ [链接](https://www.cnbc.com/2026/10/24/ukraine-starlink-starshield-service-restored.html)
**简评**：政策动向，简提。Starshield 服务已恢复。

### Musk admits SpaceX restricted Ukraine's Starlink: "That loophole was closed" ⭐（verified）
马斯克承认 SpaceX 有意限制乌克兰 Starlink 接入，"那个漏洞已被关闭"。
**评分 5.3** ｜ 2026-10-25 ｜ [链接](https://www.mediaite.com/media/news/elon-musk-admits-spacex-purposely-restricted-ukraines-starlink-access-in-war-with-russia-that-loophole-was-closed/)
**简评**：政策动向，简提。"loophole"措辞暗示此前存在绕过地理围栏的技术路径。

### For Starlink alternative, Ukraine partners with Nokia and satellite maker ICEYE ⭐（verified）
乌克兰与 Nokia 及卫星制造商 ICEYE 合作，建设 Starlink 替代方案。
**评分 5.3** ｜ 2026-10-25 ｜ [链接](https://www.cnbc.com/2026/10/23/ukraine-partners-with-nokia-and-iceye-for-starlink-alternative.html)
**简评**：**技术侧值得注意**。ICEYE 的 SAR 能力 + Nokia 的通信地面/网络能力，组合出的是"侦察—通信"一体的自主链路，绕开了对单一商业星座运营方的依赖。这是"星座主权化"趋势的典型案例：用户不再只买带宽，而是买"不被单点断供"的能力。

### Ukrainian launch test military-purpose communications satellite into orbit ⭐（verified）
乌克兰发射并测试一颗军用通信卫星入轨。
**评分 5.3** ｜ 2026-10-27 ｜ [链接](https://www.pravda.com.ua/eng/news/2026/10/27/8059951/)
**简评**：信息有限，未披露运载、轨道与平台。与上条合并看，是同一"通信自主"逻辑的资产侧落地。

### Researchers Uncover Signs of Surveillance Operation on Starlink Users ⭐（verified）
研究人员发现针对 Starlink 用户的大规模监控行动迹象。
**评分 4.0** ｜ 2026-10-27 ｜ [链接](https://gizmodo.com/researchers-uncover-signs-of-massive-surveillance-operation-on-starlink-users-2000831366)
**简评**：与首条路透社报道为同一事件的技术侧补充，简提。

### Trump admin cuts to satellites will set back US weather forecasting by a decade ⭐（verified）
特朗普政府削减卫星项目将使美国天气预报能力倒退十年。
**评分 4.3** ｜ 2026-10-27 ｜ [链接](https://www.cnn.com/2026/10/19/weather/trump-satellites-extreme-weather-forecast-future-set-back)
**简评**：政策动向，简提。气象卫星是典型的"双用途"基础设施，其能力空窗同时影响民用预报与军事气象保障。

### 其余（信息有限，仅列条目）
- *The 't Hooft model on (A)dS₂*（2026-10-27，评分 6.4）[链接](https://arxiv.org/abs/2610.37667v1) — 高能理论，与空间攻防无实质关联，entity 标签不可信。
- *Weighing dark matter particles with gravitational waves*（2026-10-27，评分 6.4）[链接](https://arxiv.org/abs/2610.37638v1) — 引力波天体物理。
- *A Quiet Night in the Millihertz Sky? LISA Forecasts from LIGO/Virgo/KAGRA Populations*（2026-10-27，评分 6.4）[链接](https://arxiv.org/abs/2610.37617v1) — LISA 探测率预测。
- *Cosmological Constraints on