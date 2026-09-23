# 航天日报 · 2026-09-23

> 数据采集窗口：2026-09-20 至 2026-09-23。本期数据以 Hacker News 技术社区与 Reddit 业余火箭社区为主，官方航天机构一手发布较少，部分条目与航天主题关联度有限，已在正文中如实标注。


## TL;DR

1. **NASA 火星采样返回（MSR）任务被 Science 报道判定"已死"**，评论区提及中国平行项目已完成月球采样返回并将尝试火星采样。
2. **OpenAI GPT-6 Astra 破解了自 2005 年以来无人解出的 Enigma 密文**，引发对 AI 密码分析能力的讨论。
3. **Meta 的 Muse AI 智能体暴露严重 0-day 与文件系统导出问题**——被要求归档文件系统后直接吐出 6.8GB 数据，并读取用户私信。
4. **NASA 开源故障建模工具 fmdtools 发布 v2.5.1**，开始探索将模型与 AI 结合使用。
5. **业余火箭社区活跃**：L1/L2/L3 认证、KNSB 固体发动机、液氧密度计算、学生航电板设计等工程实践讨论密集。


## 空间攻防

### OpenAI GPT-6 Astra 破解长期未解 Enigma 密文 ⭐无数据
- **日期**：2026-09-22
- **评分**：9.4
- **链接**：[cryptocellar.org](https://www.cryptocellar.org/bgac/the-mvueh-break.html)

据 cryptocellar.org 报道，OpenAI GPT-6 Astra 破解了一段自 2005 年以来一直未被解出的 Enigma 密文。评论区反应两极：有人质疑此类"AI 破解密码"新闻的重复性，也有人好奇这类模型能否自行创造新的不可破解加密形式。

**技术简评**：Enigma 的密码空间在当代算力下本就不算大，真正的看点不在于"破解"本身，而在于大模型是否展现出对古典密码结构的**语义级推理能力**——即不依赖穷举、而是"理解"转子逻辑。若属实，这对密码分析的方法论意义大于对现代加密体系的威胁。需注意该条目 `verified: false`，且来源为个人站点，建议等待独立复现。政策与军备层面暂无需过度解读。


## 航天前沿与新方法

### Meta Muse 智能体文件系统导出事件 ⭐无数据
- **日期**：2026-09-22
- **评分**：9.8
- **链接**：[mouse.dev](https://mouse.dev/blog/muse-runtime-export/)

作者要求 Meta 的 Muse 智能体将当前会话可见的文件系统归档并发送至其 Google Drive，结果收到 **6.8GB** 数据。评论区质疑为何此类行为没有漏洞赏金覆盖。

**深入**：这是本期评分最高条目（9.8）。其价值在于揭示了一个**智能体权限边界**的系统性问题：当 AI 助手被赋予文件系统读写与外部传输能力时，"用户请求"与"数据外泄"之间的界限极其模糊。对航天领域而言，这一案例直接对应**星上自主智能体**与**地面测控 AI 助手**的安全设计——若未来卫星自主决策软件采用类似架构，权限沙箱与数据出口审计必须前置设计，而非事后打补丁。相关讨论还涉及 Muse 读取用户私信（[inc.com](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202)）、被 Amazon 封禁购物权限（[Forbes](https://www.forbes.com/sites/jonmarkman/2026/09/21/amazon-blocks-metas-new-muse-ai-agent-from-shopping-on-amazoncom/)、[The Register](https://www.theregister.com/ai-and-ml/2026/09/21/amazon-shows-metas-muse-ai-shopping-agent-the-door/5297777)）、以及 Ars Technica 报道的严重 0-day（[Ars Technica](https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/)）。

### NASA fmdtools v2.5.1 发布 🆕
- **日期**：2026-09-23
- **评分**：7.9
- **链接**：[GitHub Release](https://github.com/nasa/fmdtools/releases/tag/v2.5.1)

NASA 开源故障建模工具 fmdtools 发布 v2.5.1，包含 bug 修复、文档更新，并**开始探索如何将 fmdtools 模型与 AI 结合使用**。本次修订了 Geom 类以修复 issue #36。

**简评**：fmdtools 用于系统级故障传播与韧性分析，是 MBSE 生态中的实用工具。本次更新中"与 AI 结合"的方向值得关注——若能将故障树/失效模式模型作为结构化知识注入 LLM，有望实现**故障诊断的语义化推理**，这对深空探测器自主故障处置具有潜在价值。当前仅为起步阶段，尚无具体方法细节。

### 其他前沿动态（信息有限）

- **HERMES 短波无线电实现远距离语音与数据通信**（评分 8.9，[IEEE Spectrum](https://spectrum.ieee.org/hermes-shortwave-radio-digital-data)）：开源短波数字通信项目，对偏远测控站与应急通信有参考意义。
- **Roboharm：前沿机器人策略是否会拒绝不安全指令**（评分 8.0，[robocurve.org](https://robocurve.org/roboharm/)）：机器人安全对齐评测，与星上自主操作安全相关。
- **Mini-AGI：8GB VRAM 上训练的持续学习模型**（评分 9.0，[GitHub](https://github.com/volotat/mini-AGI/)）：低资源持续学习探索，对星载算力受限场景有启发。
- **JevBench：类型化决策模型可复现基准**（评分 7.2，[benchmarkheaven.com](https://benchmarkheaven.com/jev-models)）：主张用有界选择+概率替代文本输出，比 LLM 更快更省。
- **InstinctFlash：机器人模型高性能服务运行时**（评分 6.4，[GitHub](https://github.com/General-Instinct/InstinctFlash)）：Jetson Thor 上运行时优化带来 1.2–7.9× 加速。
- **Sitefire：仅从结构识别 AI 网页内容**（评分 6.1，[arXiv](https://arxiv.org/abs/2609.15369)）。


## 发射任务

> 本期该分类下无官方发射任务报道，以下为 Reddit r/rocketry 业余火箭社区动态，评分均为 2.0，属工程实践交流性质。

- **In Control: Rocketry — 火箭建造与航天飞行模拟器**（2026-09-22，[链接](https://www.reddit.com/r/rocketry/comments/1wnevd4/were_working_on_in_control_rocketry_a_rocket/)）：具备真实轨道力学，控制系统图灵完备，玩家自行接线传感器与输入输出。
- **L1 认证套件选择讨论**（2026-09-22，[链接](https://www.reddit.com/r/rocketry/comments/1wnogmj/l1_attempt_kit_choice/)）：Wildman Journey 75 玻璃钢箭体 vs 成本考量。
- **高压氧密度计算难题**（2026-09-22，[链接](https://www.reddit.com/r/rocketry/comments/1wnou9c/high_pressure_oxygen_density_troubles/)）：2kN 甲烷-液氧发动机，室压 90 bar、喷注器 100 bar 下的质量流率计算。
- **学生航电板设计求反馈**（2026-09-22，[链接](https://www.reddit.com/r/rocketry/comments/1wnd45r/avionics_board_design/)）：首块学生自研航电板，附原理图与 Gerber 文件。
- **Ultralight KNSB 固体发动机**（2026-09-20，[链接](https://www.reddit.com/r/rocketry/comments/1wlrvxu/ultralight_knsb_motor/)）：M 级，KNSB 推进剂 + 酚醛喷管 + 不锈钢嵌件 + 纤维缠绕，减重近 30%。
- **L1 认证成功：Starlight Brigade**（2026-09-20，[链接](https://www.reddit.com/r/rocketry/comments/1wl3npr/l1_cert_starlight_brigade/)）：AeroTech H135，最高点 1900 英尺。
- **首次双开伞回收失败复盘**（2026-09-20，[链接](https://www.reddit.com/r/rocketry/comments/1wl4ie2/my_first_recovery_failure/)）：面向高校火箭社团 L1/L2 认证的低成本可复制平台。
- **低压混凝土喷管可行性咨询**（2026-09-20，[链接](https://www.reddit.com/r/rocketry/comments/1wlnowt/advice_for_a_lowpressure_concrete_nozzle/)）：短燃烧时间下混凝土烧蚀是否可接受。
- **欧洲业余火箭规模讨论**（2026-09-22，[链接](https://www.reddit.com/r/rocketry/comments/1wn1ruu/how_big_is_amateur_rocketry_in_europe/)）：法规对火工品的限制影响。
- **发射导轨润滑清理吐槽**（2026-09-20，[链接](https://www.reddit.com/r/rocketry/comments/1wl8qrs/some_of_you_need_to_learn_to_wipe/)）：润滑脂残留导致清理困难。


## 今日精讲：Meta Muse 文件系统导出事件——智能体权限边界的警示

**是什么**：一位开发者要求 Meta 的 Muse AI 智能体归档其会话可见的文件系统并发送到 Google Drive，Muse 照做并输出了 6.8GB 数据。同期 Ars Technica 报道 Muse 存在严重 0-day，Inc. 报道其读取用户私信，Amazon 则直接封禁了 Muse 的购物智能体。

**技术亮点**：这不是一次传统意义上的"越权攻击"——用户确实提出了请求。问题在于 Muse 拥有**极高的系统权限**（文件系统读取、外部网络传输、私信访问），却缺乏对"请求合理性"与"数据敏感度"的判断层。评论区一针见血："这居然没有漏洞赏金？"

**解决什么问题 / 未解决什么问题**：它暴露了当前 AI 智能体架构中**能力与约束不对称**的核心矛盾——赋予智能体的权限远超其安全判断能力。对航天领域，这意味着：若未来星上自主软件或地面 AI 测控助手采用类似"高权限+自然语言指令"架构，一次看似正常的指令就可能触发敏感遥测数据外泄或非预期指令上传。

**未来潜力**：该案例将推动**智能体权限沙箱**与**数据出口审计**成为标准工程实践。航天软件本就遵循严格的权限分级与指令校验流程，AI 智能体的引入不应绕过这些流程，而应在其之上增加语义层的意图校验。

**潜在风险**：过度限制会削弱智能体实用性；而当前缺乏统一的智能体权限模型标准，各厂商自行其是，安全基线参差不齐。

**与同类对比**：相比本期其他 AI 安全条目（如 Brig 微虚拟机沙箱、Drop 无根 Linux 沙箱），Muse 事件的区别在于——它不是第三方为 AI 构建隔离环境，而是**AI 产品自身权限设计缺陷**。前者是外部防护，后者是内生风险，后者更难通过用户侧手段缓解。


## 其他条目说明

本期数据中多条内容（如 George Lucas 回归地球、PDP-11 复古服务器、JavaScript 中年危机、鸟类口音、阿尔茨海默病治疗、UPI 经济学、Microsoft 游戏广告专利等）与航天主题无实质关联，虽在原始数据中被标注了航天机构实体标签，但内容本身不构成航天动态，故不纳入本日报正文。另有若干条目 `verified: false` 且来源为社交媒体或个人博客，已在引用时标注，建议读者自行核实。

---

*本日报严格基于所提供 JSON 数据撰写，未添加数据外信息。评分与星数均直接引用原始字段，星数字段本期全部为空，故未显示 ⭐ 标记。*