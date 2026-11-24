"""课程元数据：讲次顺序、中英文标题、日期、摘要、推荐阅读（来自 https://cs2680.com 课表）。"""

S = "https://cs2680.com/"
P1, P2, AX = "第一部分 · LLM 与智能体入门", "第二部分 · 面向 LLM 与智能体的系统", "附 · 作业讲义"

LECTURES = [
    dict(id="1_intro", no="L01", part=P1, when="第 1 周 · 2026-09-02",
         en="Course overview and logistics", zh="课程概览与事务安排",
         summary="这门课讲什么、五个作业与项目、评分政策；AI 系统与智能体系统为何不同于传统计算机系统。",
         readings=[]),
    dict(id="2_agent_use_1", no="L02", part=P1, when="第 2 周 · 2026-09-09",
         en="Agents use I: How Claude Code Works", zh="智能体使用 I：Claude Code 是如何工作的",
         summary="LLM 基础与智能体循环；拆解 Claude Code 的上下文、工具、权限与会话机制，以及高效使用它的方法。",
         readings=[("How I use LLMs（Karpathy）", "https://www.youtube.com/watch?v=EWvNQjAaOHw"),
                   ("Claude Code 最佳实践", "https://code.claude.com/docs/en/best-practices"),
                   ("Agentic Engineering Patterns", "https://simonwillison.net/guides/agentic-engineering-patterns/"),
                   ("更多阅读 →", S + "readings/sep-09.html")]),
    dict(id="3_agent_use_2", no="L03", part=P1, when="第 3 周 · 2026-09-14",
         en="Agents use II: 100x Engineer with Multi-agents", zh="智能体使用 II：用多智能体成为 100 倍工程师",
         summary="子智能体、并行智能体、智能体团队；如何拆分任务、验证产出，把多个智能体组织成高效的工程流程。",
         readings=[("Claude Code agent teams", "https://code.claude.com/docs/en/agent-teams"),
                   ("Software is changing (again)", "https://www.youtube.com/watch?v=LCEmiRjPEtQ"),
                   ("Research acceleration: The view inside OpenAI", "https://openai.com/index/research-acceleration-view-inside-openai/"),
                   ("更多阅读 →", S + "readings/sep-14.html")]),
    dict(id="4_agent_design_1", no="L04", part=P1, when="第 3 周 · 2026-09-16",
         en="Agents design I: context management and tool design", zh="智能体设计 I：上下文管理与工具设计",
         summary="从零设计一个智能体：智能体循环、上下文工程（压缩、检索、缓存友好）与工具接口设计。",
         readings=[("ReAct", "https://arxiv.org/abs/2210.03629"),
                   ("A practical guide to building agents（OpenAI）", "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents"),
                   ("LLM Powered Autonomous Agents（Lilian Weng）", "https://lilianweng.github.io/posts/2023-06-23-agent"),
                   ("更多阅读 →", S + "readings/sep-16.html")]),
    dict(id="5_agent_design_2", no="L05", part=P1, when="第 4 周 · 2026-09-23",
         en="Agents design II: multi-agent architecture, coordination, and communication",
         zh="智能体设计 II：多智能体架构、协调与通信",
         summary="何时该用多智能体、常见架构模式、智能体之间如何分工与通信，以及多智能体带来的代价。",
         readings=[("Anthropic 多智能体研究系统", "https://www.anthropic.com/engineering/multi-agent-research-system"),
                   ("Scaling agent systems", "https://arxiv.org/pdf/2512.08296"),
                   ("Don't build multi-agents（Cognition）", "https://cognition.com/blog/dont-build-multi-agents"),
                   ("更多阅读 →", S + "readings/sep-23.html")]),
    dict(id="6_agent_design_3", no="L06", part=P1, when="第 5 周 · 2026-09-28",
         en="Agents design III: agent memory and reliability", zh="智能体设计 III：智能体记忆与可靠性",
         summary="智能体的记忆层次与持久化；智能体在哪里失败、如何提升可靠性。",
         readings=[("Where agents fail", "https://arxiv.org/abs/2509.25370"),
                   ("MemGPT", "https://arxiv.org/abs/2310.08560"),
                   ("更多阅读 →", S + "readings/sep-28.html")]),
    dict(id="7_agent_design_4", no="L07", part=P1, when="第 5 周 · 2026-09-30",
         en="Agent design IV: agent evaluation", zh="智能体设计 IV：智能体评测",
         summary="如何评测智能体：评测设计、指标、可靠性、成本与基准测试的选择。",
         readings=[("Agent evaluation and benchmarks（课程笔记）", S + "notes/agent-evaluation.html")]),
    dict(id="8_agent_design_5", no="L08", part=P1, when="第 6 周 · 2026-10-07",
         en="Advanced agent design I: Cost and performance", zh="高级智能体设计 I：成本与性能",
         summary="在整个任务维度上分配模型、推理、上下文、协作与推理服务资源，打造高性价比的智能体。",
         readings=[("Cost-effective agents（课程笔记）", S + "notes/cost-effective-agents.html")]),
    dict(id="9_llm_serving_basics_1", no="L09", part=P2, when="第 8 周 · 2026-10-19",
         en="Efficient LLM serving basics I: intro to LLMs", zh="高效 LLM 推理服务基础 I：LLM 入门",
         summary="一个 LLM 请求的生命周期（分词→调度→预填充→解码→流式输出）；Transformer 块、注意力与 GQA、MoE，以及滑动窗口、MLA、线性注意力、扩散 LM 等新变体。",
         readings=[("Transformer", "https://arxiv.org/abs/1706.03762"), ("Llama 3", "https://arxiv.org/abs/2407.21783"),
                   ("Mixtral", "https://arxiv.org/abs/2401.04088"), ("更多阅读 →", S + "readings/oct-19.html")]),
    dict(id="10_llm_serving_basics_2a", no="L10", part=P2, when="第 8 周 · 2026-10-21",
         en="Efficient LLM serving basics II: intro to GPUs", zh="高效 LLM 推理服务基础 II：GPU 入门",
         summary="GPU 为何是“吞吐机器”：SIMT、warp 与延迟隐藏；roofline 与算术强度、batch-1 解码为何吃不满 GPU；SM、Tensor Core、存储层次与 Hopper/Blackwell 新特性。",
         readings=[("CUDA C++ 编程指南", "https://docs.nvidia.com/cuda/cuda-c-programming-guide/"),
                   ("更多阅读 →", S + "readings/oct-21.html")]),
    dict(id="10_llm_serving_basics_2b", no="L11", part=P2, when="第 10 周 · 2026-11-02",
         en="GPU programming (cont.)", zh="GPU 编程（续）",
         summary="GPU 编程模型与 Triton / TileLang / CUTLASS 等抽象层级；用 MFU、MBU 和剖析工具衡量效率；kernel 融合、FlashAttention、持久化 kernel、CUDA Graphs、Megakernel 等近期进展。",
         readings=[]),
    dict(id="11_llm_serving_basics_3", no="L12", part=P2, when="第 10 周 · 2026-11-04",
         en="Efficient LLM serving basics III: Batching, paging, and parallelism",
         zh="高效 LLM 推理服务基础 III：批处理、分页与并行",
         summary="推理服务的指标与评测陷阱；连续批处理与选择性批处理、分块预填充与 PD 分离、SJF 类调度；PagedAttention 与前缀缓存；DP / TP / PP / EP / 上下文并行。",
         readings=[("Orca", "https://www.usenix.org/conference/osdi22/presentation/yu"),
                   ("vLLM / PagedAttention", "https://arxiv.org/abs/2309.06180"),
                   ("更多阅读 →", S + "readings/nov-04.html")]),
    dict(id="12_llm_serving_spec_decoding", no="L13", part=P2, when="第 11 周 · 2026-11-11",
         en="Efficient LLM serving: speculative decoding", zh="高效 LLM 推理服务：推测解码",
         summary="推测解码为何精确（拒绝采样）与加速比公式 S = E/(ck+1)；从独立小模型到 Medusa、EAGLE 1–4、MTP、DFlash、后缀检索等草稿方法；树验证、有损变体，以及按负载动态选择 k。",
         readings=[("Speculative decoding", "https://arxiv.org/abs/2211.17192"), ("EAGLE", "https://arxiv.org/abs/2401.15077"),
                   ("Medusa", "https://arxiv.org/abs/2401.10774"), ("DSpark", "https://arxiv.org/abs/2607.05147"),
                   ("更多阅读 →", S + "readings/nov-11.html")]),
    dict(id="8_assignment3", no="A3", part=AX, when="作业 3 · 10-05 发布",
         en="Assignment 3 — Mads-Opt: Harness Competition", zh="作业 3 — Mads-Opt：Harness 优化竞赛",
         summary="优化你的编程智能体 Harness，让每个 token 都物有所值；按排行榜排名与相对基线的提升计分。",
         readings=[]),
]

COURSE = dict(
    intro_html="""
<section class="cover">
  <div class="kicker">哈佛大学 SEAS · 2026 秋季 · 讲师 Juncheng Yang · 非官方中文译本</div>
  <h1>CS2680 现代 AI 系统<br><span>智能体与系统优化</span></h1>
  <div class="en">Modern AI Systems: Agents and System Optimizations</div>
  <p class="lead">这门课沿着<b>同一个智能体系统</b>，从智能体循环一路向下贯穿到推理服务栈。
  你先使用一个现代编程智能体（Claude Code），再利用提供的 API 设计你自己的智能体，测量它、优化它；
  然后亲手部署一个开放权重模型，并为其下面的各层负责：批处理与调度、KV-cache 与前缀复用、路由、量化与推测解码。</p>
  <div class="facts">
    <div><b>先修</b>CS61 + 至少一门研究生级计算机系统课；熟悉 Python 与 PyTorch</div>
    <div><b>考核</b>5 个作业 + 期末项目 + 课堂参与，无考试</div>
    <div><b>上课</b>周一、周三 11:15–12:30 · SEC LL2.229</div>
  </div>
</section>
<section class="stack">
  <h2 class="sec">五个作业：沿技术栈逐层向下</h2>
  <ol class="steps">
    <li><b>Mads-Lens</b>看智能体如何工作 <i>10%</i></li>
    <li><b>Mads-Loop</b>亲手搭建智能体循环 <i>10%</i></li>
    <li><b>Mads-Opt</b>让每个 token 都物有所值 <i>20%</i></li>
    <li><b>Mads-Serve</b>掌控推理服务引擎 <i>20%</i></li>
    <li><b>Mads-Stack</b>优化整个技术栈 <i>10%</i></li>
  </ol>
  <p class="note">“Mads” 是 Modern Agent Design and Systems（现代智能体设计与系统）的缩写，也致敬了开设本课的哈佛 MaDSys 研究组。
  课程期望：这门课不会教会你完成作业所需的每一个知识点，而是专注于“学习的技能”，并为你指出值得探索的方向——请预期课后要花大量时间自学与实验。</p>
</section>
""",
    tail_html="""
<section class="gloss">
  <h2 class="sec">术语对照</h2>
  <p class="note">译文力求贴合课程语境：业界通行的英文术语保留原文或在首次出现时括注。</p>
  <dl>
    <div><dt>Agent / Agentic</dt><dd>智能体 / 智能体式的</dd></div>
    <div><dt>Harness</dt><dd>Harness（智能体运行框架：包住模型的循环、工具、上下文与权限管理）</dd></div>
    <div><dt>Subagent</dt><dd>子智能体</dd></div>
    <div><dt>Context / Context window</dt><dd>上下文 / 上下文窗口</dd></div>
    <div><dt>Tool call</dt><dd>工具调用</dd></div>
    <div><dt>Trajectory</dt><dd>轨迹（智能体一次任务中的完整步骤序列）</dd></div>
    <div><dt>Serving</dt><dd>推理服务</dd></div>
    <div><dt>Prefill / Decode</dt><dd>预填充 / 解码</dd></div>
    <div><dt>KV-cache / Prefix cache</dt><dd>KV 缓存 / 前缀缓存</dd></div>
    <div><dt>Batching / Continuous batching</dt><dd>批处理 / 连续批处理</dd></div>
    <div><dt>Speculative decoding</dt><dd>推测解码</dd></div>
    <div><dt>Throughput / Latency</dt><dd>吞吐量 / 延迟</dd></div>
    <div><dt>TTFT / TPOT</dt><dd>首 token 延迟 / 每输出 token 耗时</dd></div>
    <div><dt>Kernel</dt><dd>kernel（GPU 上执行的计算函数）</dd></div>
    <div><dt>Leaderboard</dt><dd>排行榜</dd></div>
    <div><dt>TF</dt><dd>助教（Teaching Fellow）</dd></div>
  </dl>
</section>
<footer class="foot">
  原课程：<a href="https://cs2680.com" target="_blank" rel="noopener">cs2680.com</a>（Harvard SEAS · Juncheng Yang）。
  本网页为个人学习用的非官方中文翻译，版权归原作者所有；每页均附原版页面图像以便对照。
</footer>
""",
)
