# CrewAI学习指南-第2章实践：核心概念循序渐进实战

> 🎯 按照CrewAI官方标准，由浅入深地掌握Agent、Task、Crew、Flow四大核心概念！

## 📚 学习路径设计

本实践指南采用循序渐进的方式：
1. **🤖 第一步：理解Agent** - 从最简单的单个Agent开始
2. **📋 第二步：掌握Task** - 学会设计和配置任务
3. **🏰 第三步：组建Crew** - 让多个Agent协作工作
4. **🌊 第四步：构建Flow** - 实现复杂的工作流控制

## 🎯 实践项目：智能内容创作助手

我们将构建一个由浅入深的智能内容创作系统：
- **阶段1**：单个研究员Agent
- **阶段2**：研究员Agent + 研究任务Task
- **阶段3**：研究员 + 写作员 + 编辑员组成的Crew
- **阶段4**：智能Flow工作流控制整个创作过程

---

## 第一步：环境准备与标准项目创建 🛠️

### 1.1 安装CrewAI CLI

**Windows用户注意**：如果遇到编译错误，请使用以下分步安装方法：

```bash
# 方法1：基础安装（推荐，避免编译问题）
pip install crewai
pip install requests beautifulsoup4 pandas python-dotenv langchain-openai

# 验证安装
crewai --version

# 如果上述命令成功，再尝试安装工具包（可选）
# pip install crewai[tools]
```

**如果仍有编译错误，请按以下步骤解决**：

1. **安装Microsoft C++ Build Tools**：
   - 下载：https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - 安装时选择"C++ build tools"工作负载

2. **或者使用conda安装**：
```bash
# 使用conda可以避免编译问题
conda install -c conda-forge crewai
```

### 1.2 使用官方CLI创建项目

```bash
# 使用CrewAI官方命令创建项目
crewai create crew content-creator

# 进入项目目录
cd content-creator
```

**📁 CrewAI标准项目结构**：
```
content-creator/
├── .env                    # 环境变量配置
├── .gitignore             # Git忽略文件
├── pyproject.toml         # 项目依赖配置
├── README.md              # 项目说明
└── src/
    └── content_creator/
        ├── __init__.py
        ├── main.py        # 主程序入口
        ├── crew.py        # Crew定义
        ├── tools/         # 自定义工具
        │   ├── __init__.py
        │   └── custom_tool.py
        └── config/        # 配置文件
            ├── agents.yaml    # Agent配置
            └── tasks.yaml     # Task配置
```

### 1.3 配置硅基流动API

编辑 `.env` 文件，配置硅基流动的OpenAI兼容接口：

```bash
# 硅基流动API配置（OpenAI兼容模式）
OPENAI_API_KEY=your_siliconflow_api_key_here
OPENAI_API_BASE=https://api.siliconflow.cn/v1
OPENAI_MODEL_NAME=deepseek-chat

# 项目配置
PROJECT_NAME=智能内容创作助手
```

**💡 硅基流动配置说明**：
- `OPENAI_API_KEY`: 你的硅基流动API密钥
- `OPENAI_API_BASE`: 硅基流动的API基础URL
- `OPENAI_MODEL_NAME`: 使用的模型名称（如deepseek-chat、qwen-plus等）

### 1.4 验证环境配置

创建测试脚本 `test_setup.py`：
```python
#!/usr/bin/env python3
"""验证CrewAI环境配置"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_basic_environment():
    """测试基础环境配置"""
    print("🧪 测试CrewAI基础环境配置...")

    # 检查环境变量
    api_key = os.getenv("OPENAI_API_KEY")
    api_base = os.getenv("OPENAI_API_BASE")
    model_name = os.getenv("OPENAI_MODEL_NAME")

    if not api_key:
        print("❌ 未设置OPENAI_API_KEY")
        return False

    print(f"✅ API密钥: {api_key[:10]}...")
    print(f"✅ API基础URL: {api_base}")
    print(f"✅ 模型名称: {model_name}")

    # 测试CrewAI导入
    try:
        import crewai
        print(f"✅ CrewAI版本: {crewai.__version__}")
    except ImportError as e:
        print(f"❌ CrewAI导入失败: {str(e)}")
        return False

    # 测试LangChain OpenAI导入
    try:
        from langchain_openai import ChatOpenAI
        print("✅ LangChain OpenAI导入成功")
    except ImportError as e:
        print(f"❌ LangChain OpenAI导入失败: {str(e)}")
        print("💡 请运行: pip install langchain-openai")
        return False

    return True

def test_api_connection():
    """测试API连接（可选）"""
    print("\n🔗 测试API连接...")

    try:
        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),
            model=os.getenv("OPENAI_MODEL_NAME"),
            temperature=0.1
        )

        response = llm.invoke("你好，请回复'连接成功'")
        print(f"✅ API连接测试成功: {response.content}")
        return True

    except Exception as e:
        print(f"⚠️ API连接测试失败: {str(e)}")
        print("💡 这可能是网络问题，不影响后续学习")
        return False

if __name__ == "__main__":
    basic_success = test_basic_environment()

    if basic_success:
        print("\n🎉 基础环境配置完成！")

        # 可选的API连接测试
        api_success = test_api_connection()

        if api_success:
            print("🚀 完整环境验证成功，可以开始CrewAI实践！")
        else:
            print("📚 基础环境OK，可以开始学习理论部分")
    else:
        print("\n❌ 环境配置有问题，请检查安装步骤")
```

运行测试：
```bash
python test_setup.py
```

**💡 故障排除提示**：
- 如果看到"基础环境配置完成"，说明CrewAI安装成功
- 如果API连接失败，可能是网络问题，不影响学习概念
- 如果导入失败，请检查pip安装是否成功

**✅ 检查点1**：确保看到"🎉 环境配置完成"的消息

---

## 第二步：从零开始理解Agent 🤖

### 2.1 什么是Agent？

在CrewAI中，Agent就像一个有专业技能的虚拟员工：
- **🎭 Role（角色）**：他的职位是什么？
- **🎯 Goal（目标）**：他要完成什么任务？
- **📖 Backstory（背景）**：他有什么经验和技能？

### 2.2 创建你的第一个Agent

编辑 `src/content_creator/config/agents.yaml`：

```yaml
# 研究员Agent - 我们的第一个智能体
researcher:
  role: >
    专业内容研究员
  goal: >
    收集和整理关于指定主题的准确、全面的信息，
    为内容创作提供可靠的素材基础
  backstory: >
    你是一位经验丰富的内容研究专家，拥有5年的信息收集和分析经验。
    你擅长从各种渠道快速找到准确、权威的信息，
    并能够识别信息的可靠性和相关性。
    你总是能够为创作者提供结构化、易于理解的研究材料。
  verbose: true
  allow_delegation: false
```

### 2.3 理解Agent配置参数

让我们逐一理解每个参数：

**🎭 Role（角色）**：
- 简洁明确地描述Agent的职业身份
- 例如："专业内容研究员"、"资深数据分析师"

**🎯 Goal（目标）**：
- 描述Agent要达成的具体目标
- 要具体、可衡量、可执行

**📖 Backstory（背景故事）**：
- 给Agent一个"人设"，包括经验、技能、工作风格
- 这会影响Agent的行为模式和回答风格

**⚙️ 其他重要参数**：
- `verbose: true` - 显示Agent的思考过程
- `allow_delegation: false` - 不允许委派任务给其他Agent

### 2.4 测试单个Agent

创建测试文件 `test_agent.py`：

```python
#!/usr/bin/env python3
"""测试单个Agent的功能"""

import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI

# 加载环境变量
load_dotenv()

def create_researcher_agent():
    """创建研究员Agent"""

    # 配置LLM（使用硅基流动）
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE"),
        model=os.getenv("OPENAI_MODEL_NAME"),
        temperature=0.1
    )

    # 创建Agent
    researcher = Agent(
        role="专业内容研究员",
        goal="收集和整理关于指定主题的准确、全面的信息，为内容创作提供可靠的素材基础",
        backstory="""
        你是一位经验丰富的内容研究专家，拥有5年的信息收集和分析经验。
        你擅长从各种渠道快速找到准确、权威的信息，
        并能够识别信息的可靠性和相关性。
        你总是能够为创作者提供结构化、易于理解的研究材料。
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    return researcher

def test_agent_basic():
    """测试Agent基本功能"""
    print("🧪 测试Agent基本功能...")

    # 创建Agent
    researcher = create_researcher_agent()

    # 验证Agent属性
    print(f"✅ Agent角色: {researcher.role}")
    print(f"✅ Agent目标: {researcher.goal[:50]}...")
    print(f"✅ 详细输出: {'启用' if researcher.verbose else '禁用'}")
    print(f"✅ 允许委派: {'是' if researcher.allow_delegation else '否'}")

    return researcher

if __name__ == "__main__":
    agent = test_agent_basic()
    print("\n🎉 Agent创建成功！准备进入下一步...")
```

运行测试：
```bash
python test_agent.py
```

### 2.5 Agent的工作原理

当Agent接收到任务时，它会：

1. **🧠 理解任务**：基于role、goal、backstory理解要做什么
2. **💭 制定计划**：思考如何完成任务
3. **🔄 执行循环**：
   - 分析当前情况
   - 决定下一步行动
   - 执行行动
   - 评估结果
   - 重复直到完成
4. **📝 输出结果**：提供最终答案

**✅ 检查点2**：确保Agent创建成功，理解Agent的基本概念

---

## 第三步：给Agent分配Task任务 📋

### 3.1 什么是Task？

Task就像给员工的工作指令：
- **📝 Description（任务描述）**：具体要做什么工作？
- **🎁 Expected Output（期望输出）**：完成后应该得到什么结果？
- **👤 Agent（执行者）**：谁来完成这个任务？

### 3.2 创建你的第一个Task

编辑 `src/content_creator/config/tasks.yaml`：

```yaml
# 研究任务 - 我们的第一个任务
research_task:
  description: >
    对"{topic}"这个主题进行深入研究。
    请收集以下信息：
    1. 主题的基本定义和核心概念
    2. 当前的发展趋势和最新动态
    3. 主要的应用场景和实际案例
    4. 相关的专家观点和权威资料
    5. 可能存在的争议或不同观点

    请确保信息的准确性和时效性，并注明信息来源。

  expected_output: >
    一份结构化的研究报告，包含：
    - 主题概述（200字以内）
    - 核心要点（5-8个要点，每个要点100字左右）
    - 最新趋势（3-5个趋势）
    - 实际案例（2-3个具体案例）
    - 专家观点（引用2-3位专家的观点）
    - 参考资料（列出主要信息来源）

    总长度控制在1500-2000字，使用Markdown格式。

  agent: researcher
```

### 3.3 理解Task配置参数

**📝 Description（任务描述）**：
- 要非常具体和详细
- 使用编号列表让任务更清晰
- 可以使用变量如`{topic}`来动态传入参数

**🎁 Expected Output（期望输出）**：
- 明确说明输出的格式和结构
- 指定长度、风格、格式要求
- 越具体越好，这样Agent知道如何完成任务

**👤 Agent（执行者）**：
- 指定哪个Agent来执行这个任务
- 必须是在agents.yaml中定义的Agent名称

### 3.4 测试Agent + Task组合

创建测试文件 `test_agent_task.py`：

```python
#!/usr/bin/env python3
"""测试Agent执行Task的完整流程"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task
from langchain_openai import ChatOpenAI

# 加载环境变量
load_dotenv()

def create_researcher_agent():
    """创建研究员Agent"""
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE"),
        model=os.getenv("OPENAI_MODEL_NAME"),
        temperature=0.1
    )

    return Agent(
        role="专业内容研究员",
        goal="收集和整理关于指定主题的准确、全面的信息",
        backstory="""
        你是一位经验丰富的内容研究专家，拥有5年的信息收集和分析经验。
        你擅长从各种渠道快速找到准确、权威的信息。
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_research_task(agent, topic="人工智能"):
    """创建研究任务"""
    return Task(
        description=f"""
        对"{topic}"这个主题进行深入研究。
        请收集以下信息：
        1. 主题的基本定义和核心概念
        2. 当前的发展趋势和最新动态
        3. 主要的应用场景和实际案例
        4. 相关的专家观点和权威资料

        请确保信息的准确性和时效性。
        """,

        expected_output="""
        一份结构化的研究报告，包含：
        - 主题概述（200字以内）
        - 核心要点（5个要点，每个要点100字左右）
        - 最新趋势（3个趋势）
        - 实际案例（2个具体案例）

        总长度控制在1000-1500字，使用Markdown格式。
        """,

        agent=agent
    )

def test_agent_task_execution():
    """测试Agent执行Task"""
    print("🧪 测试Agent执行Task...")

    # 创建Agent和Task
    researcher = create_researcher_agent()
    research_task = create_research_task(researcher, "机器学习")

    print(f"✅ Agent: {researcher.role}")
    print(f"✅ Task: {research_task.description[:50]}...")

    # 执行任务
    print("\n🚀 开始执行任务...")
    try:
        result = research_task.execute()

        print("\n✅ 任务执行完成！")
        print("📄 执行结果预览（前500字符）:")
        print("-" * 50)
        print(result.raw[:500] + "..." if len(result.raw) > 500 else result.raw)

        return result

    except Exception as e:
        print(f"❌ 任务执行失败: {str(e)}")
        return None

if __name__ == "__main__":
    result = test_agent_task_execution()
    if result:
        print("\n🎉 Agent + Task 测试成功！")
        print("💡 现在你理解了Agent如何执行Task")
    else:
        print("\n❌ 测试失败，请检查配置")
```

运行测试：
```bash
python test_agent_task.py
```

### 3.5 Task执行流程解析

当Task被执行时，发生了什么：

1. **📋 任务分配**：Task被分配给指定的Agent
2. **🧠 任务理解**：Agent基于自己的role和backstory理解任务
3. **📝 计划制定**：Agent分析description，制定执行计划
4. **⚡ 执行过程**：Agent按计划执行，可能包含多轮思考
5. **✅ 结果验证**：检查输出是否符合expected_output的要求
6. **📤 返回结果**：返回TaskOutput对象，包含执行结果

**💡 关键理解**：
- Agent提供"能力"（如何思考和行动）
- Task提供"指令"（做什么和怎么做）
- 两者结合才能产生有用的输出

**✅ 检查点3**：确保能看到Agent执行Task并产生研究报告

---

## 第四步：组建多Agent协作的Crew 🏰

### 4.1 什么是Crew？

Crew就像一个工作团队：
- **👥 多个Agent**：不同专业的团队成员
- **📋 多个Task**：需要协作完成的任务列表
- **⚡ Process**：团队的工作流程（顺序执行、层级管理等）

### 4.2 扩展我们的团队

现在我们要添加更多Agent。编辑 `src/content_creator/config/agents.yaml`：

```yaml
# 研究员Agent
researcher:
  role: >
    专业内容研究员
  goal: >
    收集和整理关于指定主题的准确、全面的信息，
    为内容创作提供可靠的素材基础
  backstory: >
    你是一位经验丰富的内容研究专家，拥有5年的信息收集和分析经验。
    你擅长从各种渠道快速找到准确、权威的信息，
    并能够识别信息的可靠性和相关性。
  verbose: true
  allow_delegation: false

# 写作员Agent - 新增
writer:
  role: >
    专业内容写作员
  goal: >
    基于研究材料创作引人入胜、结构清晰的文章内容，
    确保内容既有深度又易于理解
  backstory: >
    你是一位资深的内容写作专家，拥有8年的写作经验。
    你擅长将复杂的信息转化为通俗易懂、引人入胜的文章。
    你的文章总是结构清晰、逻辑严密，深受读者喜爱。
    你特别擅长开头吸引读者注意力，结尾给人深刻印象。
  verbose: true
  allow_delegation: false

# 编辑员Agent - 新增
editor:
  role: >
    专业内容编辑员
  goal: >
    审核和优化文章内容，确保文章质量达到发布标准，
    包括语言表达、逻辑结构、事实准确性等方面
  backstory: >
    你是一位严谨的内容编辑专家，拥有10年的编辑经验。
    你有敏锐的语言感觉和严格的质量标准。
    你擅长发现文章中的问题并提出具体的改进建议。
    你总是能让好文章变得更好。
  verbose: true
  allow_delegation: false
```

### 4.3 设计协作任务流程

编辑 `src/content_creator/config/tasks.yaml`：

```yaml
# 第一步：研究任务
research_task:
  description: >
    对"{topic}"这个主题进行深入研究。
    请收集以下信息：
    1. 主题的基本定义和核心概念
    2. 当前的发展趋势和最新动态
    3. 主要的应用场景和实际案例
    4. 相关的专家观点和权威资料

    请确保信息的准确性和时效性。

  expected_output: >
    一份结构化的研究报告，包含：
    - 主题概述（200字以内）
    - 核心要点（5个要点，每个要点100字左右）
    - 最新趋势（3个趋势）
    - 实际案例（2个具体案例）
    - 专家观点（引用专家观点）

    使用Markdown格式，总长度1000-1500字。

  agent: researcher

# 第二步：写作任务（依赖研究结果）
writing_task:
  description: >
    基于研究员提供的研究报告，创作一篇关于"{topic}"的高质量文章。

    文章要求：
    1. 开头要吸引读者注意力，可以用故事、问题或有趣的事实
    2. 结构清晰，包含引言、主体、结论
    3. 内容要深入浅出，既有专业性又易于理解
    4. 适当使用小标题来组织内容
    5. 结尾要有启发性，给读者留下思考空间

    目标读者：对该主题有一定兴趣但不是专家的普通读者。

  expected_output: >
    一篇完整的文章，包含：
    - 吸引人的标题
    - 引人入胜的开头（150-200字）
    - 结构清晰的主体内容（分为3-4个小节）
    - 有启发性的结尾（100-150字）

    使用Markdown格式，总长度2000-2500字。
    语言要生动有趣，避免过于学术化的表达。

  agent: writer
  context: [research_task]  # 依赖研究任务的结果

# 第三步：编辑任务（依赖写作结果）
editing_task:
  description: >
    对写作员创作的文章进行全面的编辑和优化。

    编辑重点：
    1. 检查语言表达是否流畅自然
    2. 验证逻辑结构是否清晰合理
    3. 确认事实信息是否准确
    4. 优化段落过渡和连接
    5. 提升整体可读性
    6. 检查标题和小标题是否恰当

    如果发现问题，请直接修改并说明修改原因。

  expected_output: >
    经过编辑优化的最终文章，包含：
    - 修改后的完整文章内容
    - 编辑说明（列出主要修改点和原因）
    - 质量评估（对文章质量的整体评价）

    确保文章达到发布标准，语言流畅，逻辑清晰，事实准确。

  agent: editor
  context: [research_task, writing_task]  # 依赖前两个任务的结果
```

### 4.4 创建Crew团队

编辑 `src/content_creator/crew.py`：

```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

@CrewBase
class ContentCreatorCrew():
    """内容创作团队"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        # 配置LLM（硅基流动）
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),
            model=os.getenv("OPENAI_MODEL_NAME"),
            temperature=0.1
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=self.llm
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            llm=self.llm
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            llm=self.llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            agent=self.writer()
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],
            agent=self.editor()
        )

    @crew
    def crew(self) -> Crew:
        """创建内容创作团队"""
        return Crew(
            agents=self.agents,  # 自动包含所有定义的agents
            tasks=self.tasks,    # 自动包含所有定义的tasks
            process=Process.sequential,  # 顺序执行
            verbose=True
        )
```

### 4.5 测试Crew团队协作

创建测试文件 `test_crew.py`：

```python
#!/usr/bin/env python3
"""测试Crew团队协作"""

from src.content_creator.crew import ContentCreatorCrew

def test_crew_execution():
    """测试Crew执行"""
    print("🧪 测试Crew团队协作...")

    # 创建Crew
    crew = ContentCreatorCrew().crew()

    print(f"✅ 团队成员数量: {len(crew.agents)}")
    print(f"✅ 任务数量: {len(crew.tasks)}")
    print(f"✅ 执行模式: {crew.process}")

    # 执行任务
    print("\n🚀 开始团队协作...")
    try:
        result = crew.kickoff(inputs={'topic': '区块链技术'})

        print("\n✅ 团队协作完成！")
        print("📄 最终结果预览（前800字符）:")
        print("-" * 50)
        print(result.raw[:800] + "..." if len(result.raw) > 800 else result.raw)

        return result

    except Exception as e:
        print(f"❌ 团队协作失败: {str(e)}")
        return None

if __name__ == "__main__":
    result = test_crew_execution()
    if result:
        print("\n🎉 Crew团队协作测试成功！")
        print("💡 你已经掌握了多Agent协作的基本概念")
    else:
        print("\n❌ 测试失败，请检查配置")
```

运行测试：
```bash
python test_crew.py
```

**✅ 检查点4**：确保看到三个Agent依次工作，最终产生完整的编辑后文章

---

## 第五步：构建智能Flow工作流 🌊

### 5.1 什么是Flow？

Flow是更高级的工作流控制系统：
- **🎬 事件驱动**：基于事件触发不同的执行路径
- **🔀 条件分支**：根据条件选择不同的处理方式
- **💾 状态管理**：记录和管理整个流程的状态
- **🔗 Crew集成**：可以在Flow中调用Crew团队

### 5.2 Flow vs Crew的区别

| 特性 | Crew | Flow |
|------|------|------|
| **适用场景** | 固定的协作流程 | 复杂的条件逻辑 |
| **执行方式** | 顺序或层级执行 | 事件驱动执行 |
| **灵活性** | 相对固定 | 高度灵活 |
| **复杂度** | 简单易用 | 功能强大 |

### 5.3 创建你的第一个Flow

创建 `src/content_creator/flow.py`：

```python
from crewai.flow.flow import Flow, start, listen, router
from pydantic import BaseModel
from typing import Dict, List
from .crew import ContentCreatorCrew
import os
from dotenv import load_dotenv

load_dotenv()

class ContentCreationState(BaseModel):
    """内容创作流程状态"""
    topic: str = ""
    content_type: str = "article"  # article, tutorial, review
    target_audience: str = "general"  # general, technical, beginner
    research_completed: bool = False
    writing_completed: bool = False
    editing_completed: bool = False
    final_content: str = ""
    quality_score: float = 0.0

class ContentCreationFlow(Flow[ContentCreationState]):
    """智能内容创作工作流"""

    @start()
    def initialize_creation(self):
        """🎬 初始化内容创作流程"""
        print("🚀 启动智能内容创作工作流...")

        # 从输入获取参数
        if hasattr(self, 'inputs') and self.inputs:
            self.state.topic = self.inputs.get('topic', '人工智能')
            self.state.content_type = self.inputs.get('content_type', 'article')
            self.state.target_audience = self.inputs.get('target_audience', 'general')

        print(f"📝 创作主题: {self.state.topic}")
        print(f"📄 内容类型: {self.state.content_type}")
        print(f"👥 目标受众: {self.state.target_audience}")

        return f"内容创作初始化完成 - 主题: {self.state.topic}"

    @listen(initialize_creation)
    def analyze_requirements(self):
        """📊 分析创作需求"""
        print("🔍 分析创作需求...")

        # 根据内容类型和受众分析复杂度
        complexity_score = 0.5  # 基础分数

        if self.state.content_type == "tutorial":
            complexity_score += 0.3
        elif self.state.content_type == "review":
            complexity_score += 0.2

        if self.state.target_audience == "technical":
            complexity_score += 0.2
        elif self.state.target_audience == "beginner":
            complexity_score += 0.1

        self.state.quality_score = complexity_score

        print(f"📈 复杂度评分: {complexity_score:.2f}")
        return f"需求分析完成 - 复杂度: {complexity_score:.2f}"

    @router(analyze_requirements)
    def choose_creation_strategy(self):
        """🔀 选择创作策略"""
        print("🎯 选择最优创作策略...")

        if self.state.quality_score > 0.7:
            print("🏆 选择高质量创作流程")
            return "high_quality_creation"
        else:
            print("⚡ 选择标准创作流程")
            return "standard_creation"

    @listen("standard_creation")
    def standard_content_creation(self):
        """📝 标准内容创作"""
        print("📝 执行标准创作流程...")

        try:
            # 创建并执行Crew
            crew = ContentCreatorCrew().crew()
            result = crew.kickoff(inputs={
                'topic': self.state.topic
            })

            self.state.final_content = result.raw
            self.state.research_completed = True
            self.state.writing_completed = True
            self.state.editing_completed = True

            print("✅ 标准创作流程完成")
            return result

        except Exception as e:
            print(f"❌ 标准创作失败: {str(e)}")
            raise

    @listen("high_quality_creation")
    def high_quality_content_creation(self):
        """🏆 高质量内容创作"""
        print("🏆 执行高质量创作流程...")

        try:
            # 执行增强版的创作流程
            crew = ContentCreatorCrew().crew()

            # 第一轮创作
            print("📝 第一轮创作...")
            result = crew.kickoff(inputs={
                'topic': self.state.topic
            })

            # 模拟质量检查和优化
            print("🔍 质量检查和优化...")
            enhanced_content = f"""
# 高质量版本

{result.raw}

---

## 质量增强说明
本文经过高质量创作流程处理，包含：
- 深度研究和事实核查
- 多轮写作优化
- 严格的编辑审核
- 针对{self.state.target_audience}受众的定制化调整
"""

            self.state.final_content = enhanced_content
            self.state.research_completed = True
            self.state.writing_completed = True
            self.state.editing_completed = True
            self.state.quality_score = 0.9

            print("✅ 高质量创作流程完成")
            return enhanced_content

        except Exception as e:
            print(f"❌ 高质量创作失败: {str(e)}")
            raise

    @listen("standard_creation", "high_quality_creation")
    def finalize_content(self):
        """🎉 完成内容创作"""
        print("✨ 完成内容创作流程...")

        summary = f"""
        🎉 内容创作完成！

        📊 创作详情:
        - 主题: {self.state.topic}
        - 类型: {self.state.content_type}
        - 受众: {self.state.target_audience}
        - 质量评分: {self.state.quality_score:.2%}

        📄 内容概览:
        - 内容长度: {len(self.state.final_content)}字符
        - 研究完成: {'✅' if self.state.research_completed else '❌'}
        - 写作完成: {'✅' if self.state.writing_completed else '❌'}
        - 编辑完成: {'✅' if self.state.editing_completed else '❌'}
        """

        print(summary)
        return summary

### 5.4 测试Flow工作流

创建测试文件 `test_flow.py`：

```python
#!/usr/bin/env python3
"""测试Flow工作流"""

from src.content_creator.flow import ContentCreationFlow

def test_standard_flow():
    """测试标准创作流程"""
    print("🧪 测试标准创作Flow...")

    flow = ContentCreationFlow()

    try:
        result = flow.kickoff(inputs={
            'topic': '机器学习入门',
            'content_type': 'article',
            'target_audience': 'beginner'
        })

        print("\n✅ 标准Flow测试成功！")
        print(f"📊 最终状态: {flow.state.quality_score:.2%}")
        print(f"📄 内容长度: {len(flow.state.final_content)}字符")

        return result

    except Exception as e:
        print(f"❌ 标准Flow测试失败: {str(e)}")
        return None

def test_high_quality_flow():
    """测试高质量创作流程"""
    print("\n🧪 测试高质量创作Flow...")

    flow = ContentCreationFlow()

    try:
        result = flow.kickoff(inputs={
            'topic': '深度学习架构设计',
            'content_type': 'tutorial',
            'target_audience': 'technical'
        })

        print("\n✅ 高质量Flow测试成功！")
        print(f"📊 最终状态: {flow.state.quality_score:.2%}")
        print(f"📄 内容长度: {len(flow.state.final_content)}字符")

        return result

    except Exception as e:
        print(f"❌ 高质量Flow测试失败: {str(e)}")
        return None

if __name__ == "__main__":
    # 测试两种不同的流程
    standard_result = test_standard_flow()
    high_quality_result = test_high_quality_flow()

    if standard_result and high_quality_result:
        print("\n🎉 Flow工作流测试全部成功！")
        print("💡 你已经掌握了事件驱动的工作流设计")
    else:
        print("\n❌ 部分测试失败，请检查配置")
```

运行测试：
```bash
python test_flow.py
```

### 5.5 Flow的核心概念

**🎬 装饰器系统**：
- `@start()`: 流程入口点
- `@listen(method)`: 监听某个方法的完成
- `@router(method)`: 根据条件选择不同路径

**💾 状态管理**：
- 使用Pydantic模型定义状态
- 状态在整个流程中持续更新
- 可以基于状态做决策

**🔀 条件分支**：
- router方法返回字符串决定下一步
- 不同的返回值触发不同的监听器
- 实现复杂的业务逻辑

**✅ 检查点5**：确保看到Flow根据不同输入选择不同的创作策略

---

## 第六步：完整实践演练 🎯

### 6.1 创建主程序入口

编辑 `src/content_creator/main.py`：

```python
#!/usr/bin/env python3
"""
CrewAI内容创作系统 - 主程序入口
演示Agent、Task、Crew、Flow四大核心概念的完整应用
"""

import argparse
from .crew import ContentCreatorCrew
from .flow import ContentCreationFlow

def run_single_agent_demo():
    """演示单个Agent的能力"""
    print("\n" + "="*60)
    print("🤖 演示1: 单个Agent能力")
    print("="*60)

    from test_agent import test_agent_basic
    agent = test_agent_basic()
    print("💡 单个Agent可以独立思考和回答问题")

def run_agent_task_demo():
    """演示Agent执行Task"""
    print("\n" + "="*60)
    print("📋 演示2: Agent执行Task")
    print("="*60)

    from test_agent_task import test_agent_task_execution
    result = test_agent_task_execution()
    if result:
        print("💡 Task为Agent提供了具体的工作指令")

def run_crew_demo(topic="人工智能"):
    """演示Crew团队协作"""
    print("\n" + "="*60)
    print("🏰 演示3: Crew团队协作")
    print("="*60)

    try:
        crew = ContentCreatorCrew().crew()
        result = crew.kickoff(inputs={'topic': topic})

        print(f"\n✅ Crew协作完成！")
        print(f"📄 最终文章长度: {len(result.raw)}字符")
        print("💡 多个Agent可以协作完成复杂任务")

        return result

    except Exception as e:
        print(f"❌ Crew演示失败: {str(e)}")
        return None

def run_flow_demo(topic="区块链", content_type="tutorial"):
    """演示Flow工作流"""
    print("\n" + "="*60)
    print("🌊 演示4: Flow智能工作流")
    print("="*60)

    try:
        flow = ContentCreationFlow()
        result = flow.kickoff(inputs={
            'topic': topic,
            'content_type': content_type,
            'target_audience': 'technical'
        })

        print(f"\n✅ Flow执行完成！")
        print(f"📊 质量评分: {flow.state.quality_score:.2%}")
        print(f"📄 最终内容长度: {len(flow.state.final_content)}字符")
        print("💡 Flow可以根据条件智能选择执行路径")

        return result

    except Exception as e:
        print(f"❌ Flow演示失败: {str(e)}")
        return None

def run_complete_demo():
    """运行完整演示"""
    print("🎉 CrewAI核心概念完整演示")
    print("从Agent到Task到Crew到Flow的完整学习之旅")

    # 逐步演示四个核心概念
    run_single_agent_demo()
    run_agent_task_demo()
    crew_result = run_crew_demo("机器学习")
    flow_result = run_flow_demo("深度学习", "tutorial")

    # 总结
    print("\n" + "="*60)
    print("🎊 演示完成总结")
    print("="*60)
    print("✅ Agent: 理解了智能体的基本概念和能力")
    print("✅ Task: 掌握了如何给Agent分配具体任务")
    print("✅ Crew: 学会了多Agent协作完成复杂工作")
    print("✅ Flow: 理解了事件驱动的智能工作流")

    if crew_result and flow_result:
        print("\n🚀 恭喜！你已经掌握了CrewAI的四大核心概念！")
        print("💡 现在你可以构建自己的智能体应用了")
    else:
        print("\n⚠️ 部分演示未成功，请检查配置和网络连接")

def main():
    """主程序入口"""
    parser = argparse.ArgumentParser(description='CrewAI内容创作系统')
    parser.add_argument('--mode', choices=['demo', 'crew', 'flow'],
                       default='demo', help='运行模式')
    parser.add_argument('--topic', default='人工智能', help='创作主题')
    parser.add_argument('--type', default='article',
                       choices=['article', 'tutorial', 'review'], help='内容类型')

    args = parser.parse_args()

    if args.mode == 'demo':
        run_complete_demo()
    elif args.mode == 'crew':
        run_crew_demo(args.topic)
    elif args.mode == 'flow':
        run_flow_demo(args.topic, args.type)

if __name__ == "__main__":
    main()
```

### 6.2 使用CrewAI CLI运行

现在你可以使用CrewAI的标准命令运行项目：

```bash
# 使用CrewAI CLI运行（推荐）
crewai run

# 或者直接运行Python
python src/content_creator/main.py --mode demo

# 运行特定模式
python src/content_creator/main.py --mode crew --topic "量子计算"
python src/content_creator/main.py --mode flow --topic "区块链" --type tutorial
```

### 6.3 核心概念总结

通过这个循序渐进的实践，你已经掌握了：

#### 🤖 Agent（智能体）
- **定义**：具有角色、目标、背景的AI执行单元
- **配置**：通过YAML文件定义role、goal、backstory
- **能力**：独立思考、分析问题、生成回答

#### 📋 Task（任务）
- **定义**：给Agent的具体工作指令
- **配置**：description（做什么）+ expected_output（要什么结果）
- **执行**：Agent根据Task指令完成具体工作

#### 🏰 Crew（团队）
- **定义**：多个Agent协作完成复杂任务
- **流程**：Sequential（顺序）或Hierarchical（层级）
- **协作**：通过context实现任务间的信息传递

#### 🌊 Flow（工作流）
- **定义**：事件驱动的智能工作流控制系统
- **特性**：条件分支、状态管理、Crew集成
- **优势**：灵活的业务逻辑控制

### 6.4 学习成果检验

**✅ 基础理解检验**
- [ ] 能够解释Agent、Task、Crew、Flow的区别和联系
- [ ] 理解YAML配置文件的作用和格式
- [ ] 掌握硅基流动API的配置方法

**✅ 实践能力检验**
- [ ] 能够创建自定义的Agent角色
- [ ] 能够设计结构化的Task任务
- [ ] 能够组建多Agent协作的Crew
- [ ] 能够构建条件分支的Flow工作流

**✅ 应用能力检验**
- [ ] 能够根据业务需求选择合适的实现方式
- [ ] 能够调试和优化Agent的表现
- [ ] 能够扩展系统功能和集成新工具

---

## 🎉 恭喜完成实践！

你已经成功完成了CrewAI核心概念的循序渐进实践！🎊

### 🚀 你的收获

通过这个实践指南，你获得了：
- ✅ **扎实的理论基础**：深度理解四大核心概念
- ✅ **完整的实践经验**：从零开始构建智能体系统
- ✅ **标准的开发流程**：遵循CrewAI官方最佳实践
- ✅ **实用的配置技巧**：掌握硅基流动API集成方法

### 🎯 下一步建议

1. **深入学习工具系统**：探索CrewAI的内置工具和自定义工具开发
2. **实践更复杂的场景**：尝试构建企业级的智能体应用
3. **学习高级特性**：研究记忆系统、知识库集成、性能优化等
4. **参与社区交流**：加入CrewAI社区，分享经验和学习最新发展

### 💡 实践项目建议

基于本指南的学习，你可以尝试构建：
- **智能客服系统**：多Agent处理不同类型的客户问题
- **自动化报告生成**：从数据收集到分析到报告的完整流程
- **内容营销助手**：自动化的内容策划、创作、优化流程
- **智能代码审查**：代码分析、问题识别、优化建议的Agent团队

**🚀 继续你的CrewAI学习之旅！你已经具备了构建强大智能体应用的基础！** 💪

### 2.1 数据收集Agent

创建 `src/agents/data_collector.py`：
```python
from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL_NAME

def create_data_collector_agent():
    """创建数据收集专家Agent"""
    return Agent(
        role="市场数据收集专家",
        goal="收集准确、全面的市场数据和竞争对手信息，为后续分析提供可靠的数据基础",
        backstory="""
        你是一位经验丰富的市场研究专家，拥有10年的数据收集经验。
        你擅长从各种渠道收集市场信息，包括：
        - 行业报告和统计数据
        - 竞争对手的公开信息
        - 市场趋势和消费者行为数据
        - 新闻资讯和行业动态
        
        你总是能够找到最相关、最新的数据，并且注重数据的准确性和可靠性。
        你会仔细验证数据来源，确保信息的真实性。
        """,
        
        # 工具配置（后续添加）
        tools=[],
        
        # LLM配置
        llm=ChatOpenAI(
            model=OPENAI_MODEL_NAME,
            temperature=0.1,  # 低温度确保数据收集的准确性
            api_key=OPENAI_API_KEY
        ),
        
        # 行为配置
        verbose=True,
        allow_delegation=False,  # 专注于数据收集，不委派任务
        max_iter=25,
        max_execution_time=300,  # 5分钟超时
        
        # 高级功能
        memory=True,  # 启用记忆功能
    )
```

### 2.2 数据分析Agent

创建 `src/agents/data_analyst.py`：
```python
from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL_NAME

def create_data_analyst_agent():
    """创建数据分析专家Agent"""
    return Agent(
        role="高级数据分析师",
        goal="对收集的市场数据进行深度分析，识别趋势、模式和商业洞察，提供数据驱动的结论",
        backstory="""
        你是一位资深的数据分析专家，拥有15年的数据科学经验。
        你曾在多家知名咨询公司工作，帮助企业通过数据分析实现业务增长。
        
        你的专长包括：
        - 统计分析和数据挖掘
        - 趋势识别和预测建模
        - 市场细分和客户画像
        - 竞争对手分析
        - 商业洞察提取
        
        你总是能从复杂的数据中发现有价值的模式，
        并将技术分析转化为易懂的商业建议。
        你的分析逻辑清晰，结论可靠，深受客户信赖。
        """,
        
        # 工具配置
        tools=[],
        
        # LLM配置
        llm=ChatOpenAI(
            model=OPENAI_MODEL_NAME,
            temperature=0.2,  # 适中温度平衡创造性和准确性
            api_key=OPENAI_API_KEY
        ),
        
        # 行为配置
        verbose=True,
        allow_delegation=False,
        max_iter=30,  # 增加迭代次数用于复杂分析
        max_execution_time=600,  # 10分钟超时
        
        # 高级功能
        memory=True,
        reasoning=True,  # 启用推理规划
    )
```

### 2.3 报告生成Agent

创建 `src/agents/report_writer.py`：
```python
from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL_NAME

def create_report_writer_agent():
    """创建报告撰写专家Agent"""
    return Agent(
        role="专业报告撰写专家",
        goal="将复杂的数据分析结果转化为清晰、专业、易懂的商业报告，为决策者提供可执行的建议",
        backstory="""
        你是一位专业的商业报告撰写专家，拥有12年的企业咨询和报告写作经验。
        你曾为众多Fortune 500企业撰写过战略分析报告。
        
        你的核心能力：
        - 将复杂的技术分析转化为商业语言
        - 构建逻辑清晰的报告结构
        - 提供可执行的商业建议
        - 创建引人入胜的数据可视化描述
        - 突出关键洞察和行动要点
        
        你的报告总是结构清晰、逻辑严密、建议实用，
        能够帮助决策者快速理解现状并制定行动计划。
        """,
        
        # 工具配置
        tools=[],
        
        # LLM配置
        llm=ChatOpenAI(
            model=OPENAI_MODEL_NAME,
            temperature=0.3,  # 适当提高温度增加创造性
            api_key=OPENAI_API_KEY
        ),
        
        # 行为配置
        verbose=True,
        allow_delegation=False,
        max_iter=25,
        max_execution_time=400,  # 7分钟超时
        
        # 高级功能
        memory=True,
    )
```

**✅ 检查点2**：测试Agent创建
创建 `tests/test_agents.py`：
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.data_collector import create_data_collector_agent
from src.agents.data_analyst import create_data_analyst_agent
from src.agents.report_writer import create_report_writer_agent

def test_agents_creation():
    """测试Agent创建"""
    print("🧪 测试Agent创建...")
    
    # 创建Agents
    collector = create_data_collector_agent()
    analyst = create_data_analyst_agent()
    writer = create_report_writer_agent()
    
    # 验证Agent属性
    assert collector.role == "市场数据收集专家"
    assert analyst.role == "高级数据分析师"
    assert writer.role == "专业报告撰写专家"
    
    print("✅ 所有Agent创建成功！")
    print(f"📊 数据收集专家: {collector.role}")
    print(f"📈 数据分析师: {analyst.role}")
    print(f"📝 报告撰写专家: {writer.role}")

if __name__ == "__main__":
    test_agents_creation()
```

运行测试：
```bash
python tests/test_agents.py
```

---

## 第三步：设计Task任务系统 📋

### 3.1 数据收集Task

创建 `src/tasks/data_collection.py`：
```python
from crewai import Task
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class MarketDataOutput(BaseModel):
    """市场数据输出模型"""
    industry: str
    data_sources: List[str]
    key_metrics: Dict[str, float]
    competitor_info: List[Dict[str, str]]
    market_trends: List[str]
    data_quality_score: float
    collection_timestamp: str

def create_data_collection_task(agent, industry: str = "人工智能"):
    """创建数据收集任务"""
    return Task(
        name="市场数据收集",
        description=f"""
        对{industry}行业进行全面的市场数据收集，具体要求：
        
        1. **行业概况收集**：
           - 市场规模和增长率
           - 主要细分领域
           - 发展阶段和成熟度
        
        2. **竞争对手分析**：
           - 识别前5名主要竞争对手
           - 收集其业务模式、产品特点
           - 分析其市场定位和优势
        
        3. **市场趋势识别**：
           - 技术发展趋势
           - 消费者需求变化
           - 监管政策影响
        
        4. **关键指标收集**：
           - 市场增长率
           - 用户采用率
           - 投资热度
           - 技术成熟度
        
        数据来源要求：
        - 优先使用权威行业报告
        - 参考知名咨询公司数据
        - 关注最新的新闻动态
        - 确保数据的时效性（近6个月内）
        """,
        
        expected_output=f"""
        结构化的{industry}行业市场数据报告，包含：
        
        1. **执行摘要**（200字以内）
        2. **行业概况**：
           - 市场规模：具体数值和增长率
           - 发展阶段：萌芽期/成长期/成熟期/衰退期
           - 关键驱动因素：3-5个主要因素
        
        3. **竞争格局**：
           - 主要竞争对手列表（至少5家）
           - 每家公司的核心信息：名称、业务模式、市场份额、特色产品
        
        4. **市场趋势**：
           - 技术趋势：3-5个关键技术方向
           - 市场趋势：3-5个重要市场变化
           - 未来预测：1-2年内的发展预期
        
        5. **关键指标**：
           - 市场规模（当前和预测）
           - 年增长率
           - 用户渗透率
           - 投资金额
        
        6. **数据质量评估**：
           - 数据来源可靠性评分（1-10分）
           - 数据完整性说明
           - 潜在局限性
        
        格式要求：
        - 使用Markdown格式
        - 包含数据表格
        - 标注数据来源
        - 总长度2000-3000字
        """,
        
        # Agent分配
        agent=agent,
        
        # 输出格式
        output_pydantic=MarketDataOutput,
        
        # 执行配置
        async_execution=False,
        
        # 质量保证
        max_retries=3,
    )

### 3.2 数据分析Task

创建 `src/tasks/data_analysis.py`：
```python
from crewai import Task
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class AnalysisInsight(BaseModel):
    """分析洞察模型"""
    insight_type: str  # trend, opportunity, threat, pattern
    description: str
    confidence_level: float  # 0-1
    supporting_data: List[str]
    business_impact: str

class MarketAnalysisOutput(BaseModel):
    """市场分析输出模型"""
    analysis_summary: str
    key_insights: List[AnalysisInsight]
    market_opportunities: List[str]
    potential_threats: List[str]
    growth_forecast: Dict[str, float]
    recommendations: List[str]
    confidence_score: float
    analysis_timestamp: str

def create_data_analysis_task(agent, context_tasks: List = None):
    """创建数据分析任务"""
    return Task(
        name="深度市场分析",
        description="""
        基于收集的市场数据进行深度分析，提取商业洞察：

        1. **趋势分析**：
           - 识别市场增长趋势和周期性模式
           - 分析技术发展轨迹
           - 预测未来6-12个月的发展方向

        2. **竞争分析**：
           - 对比主要竞争对手的优劣势
           - 识别市场空白和机会点
           - 分析竞争格局的变化趋势

        3. **机会识别**：
           - 发现未被满足的市场需求
           - 识别新兴细分市场
           - 评估进入壁垒和成功概率

        4. **风险评估**：
           - 识别潜在的市场威胁
           - 分析技术替代风险
           - 评估监管政策影响

        5. **量化分析**：
           - 计算市场增长率和预测
           - 评估投资回报潜力
           - 建立关键指标基准

        分析方法要求：
        - 使用多维度分析框架
        - 结合定量和定性分析
        - 提供数据支撑的结论
        - 考虑不确定性和风险因素
        """,

        expected_output="""
        全面的市场分析报告，包含：

        1. **分析摘要**（300字以内）
           - 核心发现概述
           - 主要结论和建议

        2. **深度洞察**（每个洞察包含）：
           - 洞察类型：趋势/机会/威胁/模式
           - 详细描述和分析逻辑
           - 置信度评估（百分比）
           - 支撑数据和证据
           - 对业务的潜在影响

        3. **市场机会**：
           - 具体的市场机会描述
           - 机会规模和时间窗口
           - 成功概率评估
           - 所需资源和能力

        4. **潜在威胁**：
           - 威胁类型和严重程度
           - 可能的影响范围
           - 应对策略建议

        5. **增长预测**：
           - 短期预测（6个月）
           - 中期预测（1-2年）
           - 关键假设和影响因素

        6. **战略建议**：
           - 3-5个可执行的建议
           - 优先级排序
           - 实施时间表

        格式要求：
        - 逻辑清晰，层次分明
        - 数据图表描述详细
        - 结论有数据支撑
        - 长度3000-4000字
        """,

        # Agent和上下文
        agent=agent,
        context=context_tasks or [],

        # 输出格式
        output_pydantic=MarketAnalysisOutput,

        # 执行配置
        async_execution=False,
        max_retries=3,
    )

### 3.3 报告生成Task

创建 `src/tasks/report_generation.py`：
```python
from crewai import Task
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class ExecutiveSummary(BaseModel):
    """执行摘要模型"""
    key_findings: List[str]
    strategic_recommendations: List[str]
    priority_actions: List[str]
    expected_outcomes: List[str]

class BusinessReport(BaseModel):
    """商业报告模型"""
    report_title: str
    executive_summary: ExecutiveSummary
    market_overview: str
    competitive_landscape: str
    opportunities_threats: str
    strategic_recommendations: str
    implementation_roadmap: str
    appendix: str
    report_date: str

def create_report_generation_task(agent, context_tasks: List = None):
    """创建报告生成任务"""
    return Task(
        name="专业商业报告生成",
        description="""
        基于数据收集和分析结果，生成高质量的商业分析报告：

        1. **报告结构设计**：
           - 设计清晰的报告框架
           - 确保逻辑流畅和层次分明
           - 突出关键信息和洞察

        2. **内容整合**：
           - 整合数据收集和分析结果
           - 提炼核心观点和发现
           - 确保信息的一致性和准确性

        3. **商业语言转化**：
           - 将技术分析转化为商业语言
           - 使用决策者易懂的表达方式
           - 避免过于复杂的技术术语

        4. **可视化描述**：
           - 描述关键数据图表
           - 解释图表的商业含义
           - 突出重要的数据趋势

        5. **行动建议**：
           - 提供具体可执行的建议
           - 设定优先级和时间表
           - 评估实施的资源需求

        报告质量要求：
        - 专业性：符合商业报告标准
        - 实用性：提供可执行的建议
        - 可读性：结构清晰，语言流畅
        - 完整性：涵盖所有关键要素
        """,

        expected_output="""
        完整的专业商业分析报告，包含以下章节：

        ## 执行摘要
        - 核心发现（3-5个要点）
        - 战略建议（3-5个建议）
        - 优先行动（按重要性排序）
        - 预期成果（量化目标）

        ## 市场概况
        - 行业现状和规模
        - 发展阶段和成熟度
        - 关键驱动因素
        - 市场细分情况

        ## 竞争格局
        - 主要竞争对手分析
        - 竞争优势对比
        - 市场份额分布
        - 竞争趋势预测

        ## 机会与威胁
        - 市场机会识别
        - 潜在威胁分析
        - SWOT分析矩阵
        - 风险缓解策略

        ## 战略建议
        - 短期行动计划（3-6个月）
        - 中期发展策略（6-18个月）
        - 长期愿景规划（1-3年）
        - 资源配置建议

        ## 实施路线图
        - 关键里程碑时间表
        - 责任分工建议
        - 成功指标定义
        - 风险控制措施

        ## 附录
        - 数据来源说明
        - 分析方法介绍
        - 关键假设列表
        - 术语解释

        格式要求：
        - 使用Markdown格式
        - 包含图表描述
        - 总长度5000-6000字
        - 专业商务写作风格
        """,

        # Agent和上下文
        agent=agent,
        context=context_tasks or [],

        # 输出格式
        output_pydantic=BusinessReport,
        output_file="reports/market_analysis_report_{timestamp}.md",

        # 执行配置
        async_execution=False,
        human_input=False,  # 可以设为True需要人工审核
        max_retries=3,
    )

def validate_report_quality(task_output) -> tuple[bool, str]:
    """验证报告质量的Guardrail函数"""
    content = task_output.raw

    # 检查必要章节
    required_sections = [
        "执行摘要", "市场概况", "竞争格局",
        "机会与威胁", "战略建议", "实施路线图"
    ]
    missing_sections = []

    for section in required_sections:
        if section not in content:
            missing_sections.append(section)

    if missing_sections:
        return False, f"报告缺少必要章节: {', '.join(missing_sections)}"

    # 检查内容长度
    if len(content) < 3000:
        return False, "报告内容过短，需要更详细的分析（至少3000字）"

    # 检查关键词密度
    key_terms = ["分析", "建议", "市场", "竞争", "机会", "风险"]
    term_count = sum(content.count(term) for term in key_terms)

    if term_count < 20:
        return False, "报告缺少足够的分析内容和专业术语"

    # 检查结构完整性
    if "##" not in content:
        return False, "报告缺少清晰的章节结构"

    return True, "报告质量验证通过"

**✅ 检查点3**：测试Task创建
创建 `tests/test_tasks.py`：
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tasks.data_collection import create_data_collection_task
from src.tasks.data_analysis import create_data_analysis_task
from src.tasks.report_generation import create_report_generation_task
from src.agents.data_collector import create_data_collector_agent

def test_tasks_creation():
    """测试Task创建"""
    print("🧪 测试Task创建...")

    # 创建测试Agent
    test_agent = create_data_collector_agent()

    # 创建Tasks
    collection_task = create_data_collection_task(test_agent, "人工智能")
    analysis_task = create_data_analysis_task(test_agent)
    report_task = create_report_generation_task(test_agent)

    # 验证Task属性
    assert collection_task.name == "市场数据收集"
    assert analysis_task.name == "深度市场分析"
    assert report_task.name == "专业商业报告生成"

    print("✅ 所有Task创建成功！")
    print(f"📊 数据收集任务: {collection_task.name}")
    print(f"📈 数据分析任务: {analysis_task.name}")
    print(f"📝 报告生成任务: {report_task.name}")

if __name__ == "__main__":
    test_tasks_creation()
```

运行测试：
```bash
python tests/test_tasks.py
```

---

## 第四步：构建Crew协作团队 🏰

### 4.1 Sequential执行模式Crew

创建 `src/crews/market_analysis_crew.py`：
```python
from crewai import Crew, Process
from crewai.memory import LongTermMemory
from src.agents.data_collector import create_data_collector_agent
from src.agents.data_analyst import create_data_analyst_agent
from src.agents.report_writer import create_report_writer_agent
from src.tasks.data_collection import create_data_collection_task
from src.tasks.data_analysis import create_data_analysis_task
from src.tasks.report_generation import create_report_generation_task, validate_report_quality
from config.settings import PROJECT_NAME
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def task_completion_callback(task_output):
    """任务完成回调函数"""
    logger.info(f"✅ 任务完成: {task_output.description[:50]}...")
    logger.info(f"📊 执行Agent: {task_output.agent}")
    logger.info(f"⏱️ 完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\n🎉 任务 '{task_output.description[:30]}...' 已完成！")

def step_execution_callback(step_output):
    """步骤执行回调函数"""
    if hasattr(step_output, 'action') and step_output.action:
        logger.info(f"🔄 执行步骤: {step_output.action}")
        print(f"⚡ 正在执行: {step_output.action}")

class MarketAnalysisCrew:
    """市场分析团队"""

    def __init__(self, industry: str = "人工智能"):
        self.industry = industry
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self):
        """创建团队成员"""
        return {
            'collector': create_data_collector_agent(),
            'analyst': create_data_analyst_agent(),
            'writer': create_report_writer_agent()
        }

    def _create_tasks(self):
        """创建任务列表"""
        # 创建任务
        collection_task = create_data_collection_task(
            self.agents['collector'],
            self.industry
        )

        analysis_task = create_data_analysis_task(
            self.agents['analyst'],
            context_tasks=[collection_task]
        )

        report_task = create_report_generation_task(
            self.agents['writer'],
            context_tasks=[collection_task, analysis_task]
        )

        # 添加质量验证
        report_task.guardrail = validate_report_quality

        return {
            'collection': collection_task,
            'analysis': analysis_task,
            'report': report_task
        }

    def _create_crew(self):
        """创建Crew团队"""
        return Crew(
            name=f"{PROJECT_NAME} - {self.industry}分析团队",

            # 团队成员（按执行顺序）
            agents=[
                self.agents['collector'],
                self.agents['analyst'],
                self.agents['writer']
            ],

            # 任务列表（按执行顺序）
            tasks=[
                self.tasks['collection'],
                self.tasks['analysis'],
                self.tasks['report']
            ],

            # 执行配置
            process=Process.sequential,
            verbose=True,

            # 团队能力
            memory=True,
            cache=True,

            # 监控回调
            task_callback=task_completion_callback,
            step_callback=step_execution_callback,

            # 性能控制
            max_rpm=10,  # 限制API调用频率
        )

    def execute(self, inputs: dict = None):
        """执行市场分析"""
        print(f"\n🚀 启动{self.industry}市场分析...")
        print(f"👥 团队成员: {len(self.agents)}个Agent")
        print(f"📋 任务数量: {len(self.tasks)}个Task")
        print("-" * 50)

        try:
            # 准备输入参数
            default_inputs = {
                "industry": self.industry,
                "analysis_depth": "深度分析",
                "report_format": "专业商业报告"
            }

            if inputs:
                default_inputs.update(inputs)

            # 执行分析
            result = self.crew.kickoff(inputs=default_inputs)

            print(f"\n🎉 {self.industry}市场分析完成！")
            print(f"📄 报告长度: {len(result.raw)}字符")
            print(f"💾 报告已保存到: reports/目录")

            return result

        except Exception as e:
            logger.error(f"❌ 执行失败: {str(e)}")
            print(f"❌ 分析执行失败: {str(e)}")
            raise

### 4.2 Hierarchical执行模式Crew

创建 `src/crews/hierarchical_crew.py`：
```python
from crewai import Crew, Process, Agent
from langchain_openai import ChatOpenAI
from src.agents.data_collector import create_data_collector_agent
from src.agents.data_analyst import create_data_analyst_agent
from src.agents.report_writer import create_report_writer_agent
from src.tasks.data_collection import create_data_collection_task
from src.tasks.data_analysis import create_data_analysis_task
from src.tasks.report_generation import create_report_generation_task
from config.settings import OPENAI_API_KEY, OPENAI_MODEL_NAME

def create_project_manager_agent():
    """创建项目经理Agent"""
    return Agent(
        role="项目经理",
        goal="协调团队成员，确保市场分析项目按时高质量完成，优化资源分配和任务执行效率",
        backstory="""
        你是一位经验丰富的项目经理，拥有10年的团队管理和项目协调经验。
        你擅长：
        1. 分析项目需求和任务复杂度
        2. 根据团队成员专长合理分配任务
        3. 监控项目进度和质量控制
        4. 协调团队沟通和解决冲突
        5. 确保项目目标的高效达成

        你总是能够识别项目中的关键路径，
        合理安排资源，确保团队协作顺畅。
        """,

        llm=ChatOpenAI(
            model=OPENAI_MODEL_NAME,
            temperature=0.1,
            api_key=OPENAI_API_KEY
        ),

        verbose=True,
        allow_delegation=True,  # 允许委派任务
        max_iter=20,
    )

class HierarchicalAnalysisCrew:
    """层级管理的分析团队"""

    def __init__(self, industry: str = "人工智能"):
        self.industry = industry
        self.manager = create_project_manager_agent()
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self):
        """创建团队成员"""
        return [
            create_data_collector_agent(),
            create_data_analyst_agent(),
            create_report_writer_agent()
        ]

    def _create_tasks(self):
        """创建任务池"""
        return [
            create_data_collection_task(None, self.industry),  # Manager会分配Agent
            create_data_analysis_task(None),
            create_report_generation_task(None)
        ]

    def _create_crew(self):
        """创建层级Crew"""
        return Crew(
            name=f"层级管理-{self.industry}分析团队",

            # 团队成员
            agents=self.agents,

            # 任务池
            tasks=self.tasks,

            # 层级执行配置
            process=Process.hierarchical,
            manager_agent=self.manager,  # 使用自定义管理者

            # 高级功能
            memory=True,
            planning=True,  # 启用规划功能
            verbose=True,

            # 性能控制
            max_rpm=15,
        )

    def execute(self, inputs: dict = None):
        """执行层级分析"""
        print(f"\n👑 启动层级管理的{self.industry}市场分析...")
        print(f"🎯 项目经理: {self.manager.role}")
        print(f"👥 团队成员: {len(self.agents)}个专家")
        print("-" * 50)

        try:
            default_inputs = {
                "industry": self.industry,
                "management_style": "层级协调",
                "quality_standard": "高标准"
            }

            if inputs:
                default_inputs.update(inputs)

            result = self.crew.kickoff(inputs=default_inputs)

            print(f"\n🏆 层级管理分析完成！")
            return result

        except Exception as e:
            print(f"❌ 层级分析失败: {str(e)}")
            raise

**✅ 检查点4**：测试Crew创建和执行
创建 `tests/test_crews.py`：
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.crews.market_analysis_crew import MarketAnalysisCrew
from src.crews.hierarchical_crew import HierarchicalAnalysisCrew

def test_sequential_crew():
    """测试顺序执行Crew"""
    print("🧪 测试顺序执行Crew...")

    crew = MarketAnalysisCrew("区块链")

    # 验证Crew配置
    assert len(crew.agents) == 3
    assert len(crew.tasks) == 3
    assert crew.crew.process.value == "sequential"

    print("✅ 顺序执行Crew创建成功！")
    print(f"👥 团队规模: {len(crew.agents)}个Agent")
    print(f"📋 任务数量: {len(crew.tasks)}个Task")

def test_hierarchical_crew():
    """测试层级执行Crew"""
    print("\n🧪 测试层级执行Crew...")

    crew = HierarchicalAnalysisCrew("云计算")

    # 验证Crew配置
    assert len(crew.agents) == 3
    assert len(crew.tasks) == 3
    assert crew.crew.process.value == "hierarchical"
    assert crew.manager is not None

    print("✅ 层级执行Crew创建成功！")
    print(f"👑 项目经理: {crew.manager.role}")
    print(f"👥 团队规模: {len(crew.agents)}个Agent")

if __name__ == "__main__":
    test_sequential_crew()
    test_hierarchical_crew()
```

运行测试：
```bash
python tests/test_crews.py
```

---

## 第五步：实现Flow智能工作流 🌊

### 5.1 基础Flow工作流

创建 `src/flows/market_analysis_flow.py`：
```python
from crewai.flow.flow import Flow, start, listen, router, and_, or_
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
from src.crews.market_analysis_crew import MarketAnalysisCrew
from src.crews.hierarchical_crew import HierarchicalAnalysisCrew
import logging

logger = logging.getLogger(__name__)

class AnalysisState(BaseModel):
    """分析流程状态"""
    industry: str = ""
    complexity_level: str = "medium"  # low, medium, high
    analysis_type: str = "standard"   # standard, deep, competitive
    crew_type: str = "sequential"     # sequential, hierarchical
    confidence_score: float = 0.0
    results: Dict[str, str] = {}
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    status: str = "pending"  # pending, running, completed, failed

class MarketAnalysisFlow(Flow[AnalysisState]):
    """智能市场分析工作流"""

    @start()
    def initialize_analysis(self):
        """🎬 初始化分析流程"""
        print("🚀 启动智能市场分析工作流...")

        self.state.start_time = datetime.now()
        self.state.status = "running"

        # 从输入获取行业信息
        if hasattr(self, 'inputs') and self.inputs:
            self.state.industry = self.inputs.get('industry', '人工智能')
            self.state.analysis_type = self.inputs.get('analysis_type', 'standard')
        else:
            self.state.industry = '人工智能'

        logger.info(f"初始化分析: {self.state.industry}行业")
        return f"分析初始化完成 - 目标行业: {self.state.industry}"

    @listen(initialize_analysis)
    def assess_complexity(self):
        """📊 评估分析复杂度"""
        print("🔍 评估分析复杂度...")

        # 基于行业和分析类型评估复杂度
        complex_industries = ['人工智能', '生物技术', '量子计算', '新能源']

        if self.state.industry in complex_industries:
            self.state.complexity_level = "high"
            self.state.confidence_score = 0.9
        elif self.state.analysis_type == "deep":
            self.state.complexity_level = "high"
            self.state.confidence_score = 0.85
        else:
            self.state.complexity_level = "medium"
            self.state.confidence_score = 0.75

        logger.info(f"复杂度评估: {self.state.complexity_level}")
        return f"复杂度评估完成 - 级别: {self.state.complexity_level}"

    @router(assess_complexity)
    def choose_execution_strategy(self):
        """🔀 选择执行策略"""
        print("🎯 选择最优执行策略...")

        if self.state.complexity_level == "high" and self.state.confidence_score > 0.8:
            self.state.crew_type = "hierarchical"
            return "hierarchical_execution"
        else:
            self.state.crew_type = "sequential"
            return "sequential_execution"

    @listen("sequential_execution")
    def execute_sequential_analysis(self):
        """📋 执行顺序分析"""
        print("⚡ 启动顺序执行分析...")

        try:
            crew = MarketAnalysisCrew(self.state.industry)
            result = crew.execute({
                'industry': self.state.industry,
                'analysis_type': self.state.analysis_type
            })

            self.state.results['sequential'] = result.raw
            self.state.status = "analysis_completed"

            logger.info("顺序分析完成")
            return result

        except Exception as e:
            logger.error(f"顺序分析失败: {str(e)}")
            self.state.status = "failed"
            raise

    @listen("hierarchical_execution")
    def execute_hierarchical_analysis(self):
        """👑 执行层级分析"""
        print("🏰 启动层级管理分析...")

        try:
            crew = HierarchicalAnalysisCrew(self.state.industry)
            result = crew.execute({
                'industry': self.state.industry,
                'analysis_type': self.state.analysis_type
            })

            self.state.results['hierarchical'] = result.raw
            self.state.status = "analysis_completed"

            logger.info("层级分析完成")
            return result

        except Exception as e:
            logger.error(f"层级分析失败: {str(e)}")
            self.state.status = "failed"
            raise

    @listen(and_(execute_sequential_analysis, execute_hierarchical_analysis))
    def finalize_analysis(self):
        """🎉 完成分析流程"""
        print("✨ 完成分析流程...")

        self.state.end_time = datetime.now()
        self.state.status = "completed"

        # 计算执行时间
        if self.state.start_time:
            duration = self.state.end_time - self.state.start_time
            execution_time = duration.total_seconds()
        else:
            execution_time = 0

        summary = f"""
        🎉 市场分析流程完成！

        📊 分析详情:
        - 目标行业: {self.state.industry}
        - 复杂度级别: {self.state.complexity_level}
        - 执行策略: {self.state.crew_type}
        - 置信度: {self.state.confidence_score:.2%}
        - 执行时间: {execution_time:.1f}秒

        📄 结果概览:
        - 报告长度: {len(self.state.results.get(self.state.crew_type, '')))}字符
        - 分析状态: {self.state.status}
        """

        logger.info("分析流程完成")
        print(summary)

        return summary

### 5.2 高级条件Flow

创建 `src/flows/advanced_flow.py`：
```python
from crewai.flow.flow import Flow, start, listen, router, and_, or_
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
from src.crews.market_analysis_crew import MarketAnalysisCrew

class MultiIndustryState(BaseModel):
    """多行业分析状态"""
    industries: List[str] = []
    completed_analyses: List[str] = []
    failed_analyses: List[str] = []
    comparative_report: str = ""
    total_start_time: Optional[datetime] = None
    analysis_results: Dict[str, str] = {}

class MultiIndustryFlow(Flow[MultiIndustryState]):
    """多行业对比分析工作流"""

    @start()
    def initialize_multi_analysis(self):
        """🎬 初始化多行业分析"""
        print("🚀 启动多行业对比分析...")

        self.state.total_start_time = datetime.now()

        # 设置默认行业列表
        if hasattr(self, 'inputs') and self.inputs:
            self.state.industries = self.inputs.get('industries', ['人工智能', '区块链'])
        else:
            self.state.industries = ['人工智能', '区块链']

        print(f"📋 分析行业: {', '.join(self.state.industries)}")
        return "多行业分析初始化完成"

    @listen(initialize_multi_analysis)
    def analyze_ai_industry(self):
        """🤖 分析AI行业"""
        if "人工智能" not in self.state.industries:
            return "跳过AI行业分析"

        print("🤖 开始AI行业分析...")
        try:
            crew = MarketAnalysisCrew("人工智能")
            result = crew.execute()
            self.state.analysis_results["人工智能"] = result.raw
            self.state.completed_analyses.append("人工智能")
            return "AI行业分析完成"
        except Exception as e:
            self.state.failed_analyses.append("人工智能")
            return f"AI行业分析失败: {str(e)}"

    @listen(initialize_multi_analysis)
    def analyze_blockchain_industry(self):
        """⛓️ 分析区块链行业"""
        if "区块链" not in self.state.industries:
            return "跳过区块链行业分析"

        print("⛓️ 开始区块链行业分析...")
        try:
            crew = MarketAnalysisCrew("区块链")
            result = crew.execute()
            self.state.analysis_results["区块链"] = result.raw
            self.state.completed_analyses.append("区块链")
            return "区块链行业分析完成"
        except Exception as e:
            self.state.failed_analyses.append("区块链")
            return f"区块链行业分析失败: {str(e)}"

    @listen(initialize_multi_analysis)
    def analyze_cloud_industry(self):
        """☁️ 分析云计算行业"""
        if "云计算" not in self.state.industries:
            return "跳过云计算行业分析"

        print("☁️ 开始云计算行业分析...")
        try:
            crew = MarketAnalysisCrew("云计算")
            result = crew.execute()
            self.state.analysis_results["云计算"] = result.raw
            self.state.completed_analyses.append("云计算")
            return "云计算行业分析完成"
        except Exception as e:
            self.state.failed_analyses.append("云计算")
            return f"云计算行业分析失败: {str(e)}"

    # 使用OR条件：任意两个行业分析完成即可生成对比报告
    @listen(or_(
        and_(analyze_ai_industry, analyze_blockchain_industry),
        and_(analyze_ai_industry, analyze_cloud_industry),
        and_(analyze_blockchain_industry, analyze_cloud_industry)
    ))
    def generate_comparative_report(self):
        """📊 生成对比分析报告"""
        print("📊 生成多行业对比报告...")

        completed = self.state.completed_analyses
        if len(completed) < 2:
            return "需要至少完成2个行业分析才能生成对比报告"

        # 生成对比报告
        report_sections = []
        report_sections.append("# 多行业对比分析报告\n")
        report_sections.append(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report_sections.append(f"对比行业: {', '.join(completed)}\n\n")

        # 添加各行业分析摘要
        for industry in completed:
            if industry in self.state.analysis_results:
                result = self.state.analysis_results[industry]
                # 提取前500字符作为摘要
                summary = result[:500] + "..." if len(result) > 500 else result
                report_sections.append(f"## {industry}行业分析摘要\n")
                report_sections.append(f"{summary}\n\n")

        # 添加对比分析
        report_sections.append("## 行业对比分析\n")
        report_sections.append("基于以上分析，各行业对比如下：\n")
        report_sections.append("- 市场成熟度对比\n")
        report_sections.append("- 增长潜力对比\n")
        report_sections.append("- 技术发展水平对比\n")
        report_sections.append("- 投资机会对比\n\n")

        self.state.comparative_report = "".join(report_sections)

        print(f"✅ 对比报告生成完成，涵盖{len(completed)}个行业")
        return "多行业对比报告生成完成"

**✅ 检查点5**：测试Flow工作流
创建 `tests/test_flows.py`：
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.flows.market_analysis_flow import MarketAnalysisFlow
from src.flows.advanced_flow import MultiIndustryFlow

def test_basic_flow():
    """测试基础Flow"""
    print("🧪 测试基础市场分析Flow...")

    flow = MarketAnalysisFlow()

    # 验证Flow配置
    assert hasattr(flow, 'state')
    assert flow.state.industry == ""
    assert flow.state.status == "pending"

    print("✅ 基础Flow创建成功！")
    print(f"📊 初始状态: {flow.state.status}")

def test_multi_industry_flow():
    """测试多行业Flow"""
    print("\n🧪 测试多行业对比Flow...")

    flow = MultiIndustryFlow()

    # 验证Flow配置
    assert hasattr(flow, 'state')
    assert isinstance(flow.state.industries, list)
    assert isinstance(flow.state.completed_analyses, list)

    print("✅ 多行业Flow创建成功！")
    print(f"📋 默认行业列表: {flow.state.industries}")

if __name__ == "__main__":
    test_basic_flow()
    test_multi_industry_flow()
```

运行测试：
```bash
python tests/test_flows.py
```

---

## 第六步：完整实践演练 🎯

### 6.1 创建主程序入口

创建 `main.py`：
```python
#!/usr/bin/env python3
"""
CrewAI市场分析系统 - 主程序入口
演示Agent、Task、Crew、Flow四大核心概念的完整应用
"""

import sys
import os
import argparse
from datetime import datetime
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from src.crews.market_analysis_crew import MarketAnalysisCrew
from src.crews.hierarchical_crew import HierarchicalAnalysisCrew
from src.flows.market_analysis_flow import MarketAnalysisFlow
from src.flows.advanced_flow import MultiIndustryFlow
from config.settings import PROJECT_NAME

def run_sequential_analysis(industry: str):
    """运行顺序执行分析"""
    print(f"\n{'='*60}")
    print(f"🚀 {PROJECT_NAME}")
    print(f"📊 顺序执行模式 - {industry}行业分析")
    print(f"{'='*60}")

    try:
        crew = MarketAnalysisCrew(industry)
        result = crew.execute()

        print(f"\n✅ 分析完成！")
        print(f"📄 报告预览（前500字符）:")
        print("-" * 50)
        print(result.raw[:500] + "..." if len(result.raw) > 500 else result.raw)

        return result

    except Exception as e:
        print(f"❌ 分析失败: {str(e)}")
        return None

def run_hierarchical_analysis(industry: str):
    """运行层级执行分析"""
    print(f"\n{'='*60}")
    print(f"🏰 {PROJECT_NAME}")
    print(f"👑 层级管理模式 - {industry}行业分析")
    print(f"{'='*60}")

    try:
        crew = HierarchicalAnalysisCrew(industry)
        result = crew.execute()

        print(f"\n✅ 层级分析完成！")
        print(f"📄 报告预览（前500字符）:")
        print("-" * 50)
        print(result.raw[:500] + "..." if len(result.raw) > 500 else result.raw)

        return result

    except Exception as e:
        print(f"❌ 层级分析失败: {str(e)}")
        return None

def run_flow_analysis(industry: str):
    """运行Flow工作流分析"""
    print(f"\n{'='*60}")
    print(f"🌊 {PROJECT_NAME}")
    print(f"⚡ 智能工作流模式 - {industry}行业分析")
    print(f"{'='*60}")

    try:
        flow = MarketAnalysisFlow()
        result = flow.kickoff(inputs={
            'industry': industry,
            'analysis_type': 'deep'
        })

        print(f"\n✅ Flow分析完成！")
        print(f"📊 流程状态: {flow.state.status}")
        print(f"🎯 执行策略: {flow.state.crew_type}")
        print(f"📈 置信度: {flow.state.confidence_score:.2%}")

        return result

    except Exception as e:
        print(f"❌ Flow分析失败: {str(e)}")
        return None

def run_multi_industry_analysis(industries: list):
    """运行多行业对比分析"""
    print(f"\n{'='*60}")
    print(f"🔄 {PROJECT_NAME}")
    print(f"📊 多行业对比分析 - {', '.join(industries)}")
    print(f"{'='*60}")

    try:
        flow = MultiIndustryFlow()
        result = flow.kickoff(inputs={'industries': industries})

        print(f"\n✅ 多行业分析完成！")
        print(f"✅ 完成分析: {', '.join(flow.state.completed_analyses)}")
        if flow.state.failed_analyses:
            print(f"❌ 失败分析: {', '.join(flow.state.failed_analyses)}")

        print(f"\n📄 对比报告预览:")
        print("-" * 50)
        preview = flow.state.comparative_report[:800] + "..." if len(flow.state.comparative_report) > 800 else flow.state.comparative_report
        print(preview)

        return result

    except Exception as e:
        print(f"❌ 多行业分析失败: {str(e)}")
        return None

def main():
    """主程序入口"""
    parser = argparse.ArgumentParser(description=f'{PROJECT_NAME} - CrewAI核心概念实践')
    parser.add_argument('--mode', choices=['sequential', 'hierarchical', 'flow', 'multi'],
                       default='sequential', help='执行模式')
    parser.add_argument('--industry', default='人工智能', help='分析行业')
    parser.add_argument('--industries', nargs='+', default=['人工智能', '区块链'],
                       help='多行业分析的行业列表')

    args = parser.parse_args()

    print(f"\n🎉 欢迎使用 {PROJECT_NAME}！")
    print(f"⏰ 启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 根据模式执行不同的分析
    if args.mode == 'sequential':
        result = run_sequential_analysis(args.industry)
    elif args.mode == 'hierarchical':
        result = run_hierarchical_analysis(args.industry)
    elif args.mode == 'flow':
        result = run_flow_analysis(args.industry)
    elif args.mode == 'multi':
        result = run_multi_industry_analysis(args.industries)

    print(f"\n🎊 感谢使用 {PROJECT_NAME}！")
    print(f"⏰ 结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()

### 6.2 创建演示脚本

创建 `demo.py`：
```python
#!/usr/bin/env python3
"""
CrewAI核心概念演示脚本
逐步展示Agent、Task、Crew、Flow的创建和使用
"""

import sys
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def demo_agents():
    """演示Agent创建"""
    print("\n" + "="*50)
    print("🤖 演示1: Agent智能体创建")
    print("="*50)

    from src.agents.data_collector import create_data_collector_agent
    from src.agents.data_analyst import create_data_analyst_agent
    from src.agents.report_writer import create_report_writer_agent

    # 创建Agents
    collector = create_data_collector_agent()
    analyst = create_data_analyst_agent()
    writer = create_report_writer_agent()

    print(f"✅ 数据收集专家: {collector.role}")
    print(f"   目标: {collector.goal[:50]}...")
    print(f"   记忆功能: {'启用' if collector.memory else '禁用'}")

    print(f"\n✅ 数据分析师: {analyst.role}")
    print(f"   目标: {analyst.goal[:50]}...")
    print(f"   推理功能: {'启用' if analyst.reasoning else '禁用'}")

    print(f"\n✅ 报告撰写专家: {writer.role}")
    print(f"   目标: {writer.goal[:50]}...")
    print(f"   最大迭代: {writer.max_iter}")

    return collector, analyst, writer

def demo_tasks():
    """演示Task创建"""
    print("\n" + "="*50)
    print("📋 演示2: Task任务创建")
    print("="*50)

    from src.tasks.data_collection import create_data_collection_task
    from src.tasks.data_analysis import create_data_analysis_task
    from src.tasks.report_generation import create_report_generation_task
    from src.agents.data_collector import create_data_collector_agent

    # 创建测试Agent
    test_agent = create_data_collector_agent()

    # 创建Tasks
    collection_task = create_data_collection_task(test_agent, "云计算")
    analysis_task = create_data_analysis_task(test_agent)
    report_task = create_report_generation_task(test_agent)

    print(f"✅ 数据收集任务: {collection_task.name}")
    print(f"   描述长度: {len(collection_task.description)}字符")
    print(f"   输出模型: {collection_task.output_pydantic.__name__ if collection_task.output_pydantic else '无'}")

    print(f"\n✅ 数据分析任务: {analysis_task.name}")
    print(f"   最大重试: {analysis_task.max_retries}")
    print(f"   输出模型: {analysis_task.output_pydantic.__name__ if analysis_task.output_pydantic else '无'}")

    print(f"\n✅ 报告生成任务: {report_task.name}")
    print(f"   质量验证: {'启用' if report_task.guardrail else '禁用'}")
    print(f"   文件输出: {'启用' if report_task.output_file else '禁用'}")

    return collection_task, analysis_task, report_task

def demo_crews():
    """演示Crew创建"""
    print("\n" + "="*50)
    print("🏰 演示3: Crew团队创建")
    print("="*50)

    from src.crews.market_analysis_crew import MarketAnalysisCrew
    from src.crews.hierarchical_crew import HierarchicalAnalysisCrew

    # 创建不同类型的Crew
    sequential_crew = MarketAnalysisCrew("新能源")
    hierarchical_crew = HierarchicalAnalysisCrew("生物技术")

    print(f"✅ 顺序执行团队:")
    print(f"   团队名称: {sequential_crew.crew.name}")
    print(f"   执行模式: {sequential_crew.crew.process.value}")
    print(f"   成员数量: {len(sequential_crew.agents)}")
    print(f"   任务数量: {len(sequential_crew.tasks)}")
    print(f"   记忆功能: {'启用' if sequential_crew.crew.memory else '禁用'}")

    print(f"\n✅ 层级管理团队:")
    print(f"   团队名称: {hierarchical_crew.crew.name}")
    print(f"   执行模式: {hierarchical_crew.crew.process.value}")
    print(f"   项目经理: {hierarchical_crew.manager.role}")
    print(f"   成员数量: {len(hierarchical_crew.agents)}")
    print(f"   规划功能: {'启用' if hierarchical_crew.crew.planning else '禁用'}")

    return sequential_crew, hierarchical_crew

def demo_flows():
    """演示Flow创建"""
    print("\n" + "="*50)
    print("🌊 演示4: Flow工作流创建")
    print("="*50)

    from src.flows.market_analysis_flow import MarketAnalysisFlow
    from src.flows.advanced_flow import MultiIndustryFlow

    # 创建Flow实例
    basic_flow = MarketAnalysisFlow()
    multi_flow = MultiIndustryFlow()

    print(f"✅ 基础分析流程:")
    print(f"   状态模型: {basic_flow.state.__class__.__name__}")
    print(f"   初始状态: {basic_flow.state.status}")
    print(f"   默认行业: {basic_flow.state.industry or '未设置'}")
    print(f"   复杂度级别: {basic_flow.state.complexity_level}")

    print(f"\n✅ 多行业对比流程:")
    print(f"   状态模型: {multi_flow.state.__class__.__name__}")
    print(f"   默认行业: {multi_flow.state.industries}")
    print(f"   完成分析: {len(multi_flow.state.completed_analyses)}")
    print(f"   失败分析: {len(multi_flow.state.failed_analyses)}")

    return basic_flow, multi_flow

def main():
    """主演示程序"""
    print("🎉 CrewAI核心概念完整演示")
    print("展示Agent、Task、Crew、Flow四大核心概念")

    try:
        # 逐步演示各个概念
        agents = demo_agents()
        tasks = demo_tasks()
        crews = demo_crews()
        flows = demo_flows()

        print("\n" + "="*50)
        print("🎊 演示完成总结")
        print("="*50)
        print("✅ Agent智能体: 3个专业角色创建成功")
        print("✅ Task任务: 3个结构化任务创建成功")
        print("✅ Crew团队: 2种执行模式团队创建成功")
        print("✅ Flow工作流: 2种智能流程创建成功")

        print("\n🚀 所有核心概念演示完成！")
        print("💡 你现在可以运行 python main.py 来体验完整的分析流程")

    except Exception as e:
        print(f"❌ 演示过程中出现错误: {str(e)}")
        print("💡 请检查环境配置和依赖安装")

if __name__ == "__main__":
    main()

### 6.3 实践验证步骤

**步骤1: 环境验证**
```bash
# 验证Python环境
python --version

# 验证依赖安装
python -c "import crewai; print('CrewAI版本:', crewai.__version__)"

# 验证配置文件
python -c "from config.settings import *; print('配置验证通过')"
```

**步骤2: 组件测试**
```bash
# 测试所有组件
python tests/test_agents.py
python tests/test_tasks.py
python tests/test_crews.py
python tests/test_flows.py
```

**步骤3: 演示运行**
```bash
# 运行完整演示
python demo.py
```

**步骤4: 实际分析**
```bash
# 顺序执行模式
python main.py --mode sequential --industry "人工智能"

# 层级管理模式
python main.py --mode hierarchical --industry "区块链"

# 智能工作流模式
python main.py --mode flow --industry "云计算"

# 多行业对比模式
python main.py --mode multi --industries "人工智能" "区块链" "云计算"
```

---

## 第七步：故障排除与优化 🔧

### 7.1 常见问题解决

**问题1: API密钥错误**
```bash
# 错误信息: "请在.env文件中设置OPENAI_API_KEY"
# 解决方案:
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
echo "OPENAI_MODEL_NAME=gpt-4o-mini" >> .env
```

**问题2: 模块导入错误**
```bash
# 错误信息: "ModuleNotFoundError: No module named 'src'"
# 解决方案: 确保在项目根目录运行
cd crewai-market-analysis
python main.py
```

**问题3: 内存不足**
```python
# 在config/settings.py中添加内存优化配置
MEMORY_CONFIG = {
    "provider": "chroma",
    "config": {
        "host": "localhost",
        "port": 8000,
        "collection_name": "crew_memory",
        "persist_directory": "./memory_db"
    }
}

# 在Crew配置中启用缓存
cache=True,
max_rpm=5,  # 降低请求频率
```

**问题4: 执行超时**
```python
# 增加超时时间
max_execution_time=600,  # 10分钟
max_iter=50,  # 增加最大迭代次数

# 或者启用异步执行
async_execution=True
```

### 7.2 性能优化建议

**优化1: Agent配置优化**
```python
# 优化Agent性能
optimized_agent = Agent(
    role="优化的分析师",
    goal="高效完成分析任务",
    backstory="...",

    # 性能优化配置
    llm=ChatOpenAI(
        model="gpt-4o-mini",  # 使用更快的模型
        temperature=0.1,      # 降低随机性
        max_tokens=2000,      # 限制输出长度
    ),

    max_iter=20,              # 适中的迭代次数
    max_execution_time=300,   # 5分钟超时
    verbose=False,            # 关闭详细输出以提高速度
    cache=True,               # 启用缓存
)
```

**优化2: Task批量处理**
```python
# 批量处理多个相似任务
def create_batch_tasks(industries: list, agent):
    """批量创建任务"""
    tasks = []
    for industry in industries:
        task = create_data_collection_task(agent, industry)
        task.async_execution = True  # 启用异步执行
        tasks.append(task)
    return tasks

# 并行执行
import asyncio

async def execute_tasks_parallel(tasks):
    """并行执行任务"""
    results = await asyncio.gather(*[
        task.execute_async() for task in tasks
    ])
    return results
```

**优化3: 内存管理**
```python
# 定期清理内存
import gc

def cleanup_memory():
    """清理内存"""
    gc.collect()
    print("🧹 内存清理完成")

# 在长时间运行的流程中定期调用
@listen(some_task)
def memory_intensive_task(self):
    # 执行任务
    result = heavy_computation()

    # 清理内存
    cleanup_memory()

    return result
```

### 7.3 监控和日志

创建 `src/utils/monitoring.py`：
```python
import logging
import time
from datetime import datetime
from functools import wraps
from typing import Any, Callable

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/crewai_system.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def monitor_execution(func: Callable) -> Callable:
    """监控函数执行时间和状态"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"🚀 开始执行: {func.__name__}")

        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"✅ 执行完成: {func.__name__} - 耗时: {execution_time:.2f}秒")
            return result

        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ 执行失败: {func.__name__} - 耗时: {execution_time:.2f}秒 - 错误: {str(e)}")
            raise

    return wrapper

class PerformanceMonitor:
    """性能监控器"""

    def __init__(self):
        self.metrics = {}
        self.start_times = {}

    def start_timer(self, name: str):
        """开始计时"""
        self.start_times[name] = time.time()
        logger.info(f"⏱️ 开始计时: {name}")

    def end_timer(self, name: str):
        """结束计时"""
        if name in self.start_times:
            duration = time.time() - self.start_times[name]
            self.metrics[name] = duration
            logger.info(f"⏱️ 计时结束: {name} - 耗时: {duration:.2f}秒")
            del self.start_times[name]
            return duration
        return None

    def get_metrics(self):
        """获取性能指标"""
        return self.metrics

    def print_summary(self):
        """打印性能摘要"""
        print("\n📊 性能监控摘要:")
        print("-" * 40)
        for name, duration in self.metrics.items():
            print(f"{name}: {duration:.2f}秒")

        if self.metrics:
            total_time = sum(self.metrics.values())
            print(f"\n总执行时间: {total_time:.2f}秒")

# 全局性能监控器
performance_monitor = PerformanceMonitor()
```

### 7.4 调试技巧

**调试技巧1: 启用详细输出**
```python
# 在开发阶段启用详细输出
debug_agent = Agent(
    role="调试专家",
    goal="帮助调试问题",
    backstory="...",
    verbose=True,        # 启用详细输出
    debug=True,          # 启用调试模式（如果支持）
)

debug_crew = Crew(
    agents=[debug_agent],
    tasks=[debug_task],
    verbose=True,        # 启用详细输出
    debug=True,          # 启用调试模式
)
```

**调试技巧2: 分步执行**
```python
def debug_step_by_step():
    """分步调试执行"""
    print("🔍 开始分步调试...")

    # 步骤1: 创建Agent
    print("步骤1: 创建Agent")
    agent = create_data_collector_agent()
    print(f"✅ Agent创建成功: {agent.role}")

    # 步骤2: 创建Task
    print("步骤2: 创建Task")
    task = create_data_collection_task(agent, "测试行业")
    print(f"✅ Task创建成功: {task.name}")

    # 步骤3: 执行Task
    print("步骤3: 执行Task")
    try:
        result = task.execute()
        print(f"✅ Task执行成功")
        return result
    except Exception as e:
        print(f"❌ Task执行失败: {str(e)}")
        return None
```

**调试技巧3: 日志分析**
```python
def analyze_logs():
    """分析日志文件"""
    import re

    log_file = "logs/crewai_system.log"

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            logs = f.read()

        # 统计错误
        errors = re.findall(r'ERROR.*', logs)
        print(f"🔍 发现 {len(errors)} 个错误:")
        for error in errors[-5:]:  # 显示最近5个错误
            print(f"  ❌ {error}")

        # 统计执行时间
        times = re.findall(r'耗时: ([\d.]+)秒', logs)
        if times:
            avg_time = sum(float(t) for t in times) / len(times)
            print(f"📊 平均执行时间: {avg_time:.2f}秒")

    except FileNotFoundError:
        print("📝 日志文件不存在，请先运行系统生成日志")
```

---

## 第八步：实践总结与进阶 🎓

### 8.1 核心概念掌握检查

**✅ Agent智能体掌握程度**
- [ ] 能够创建具有明确角色和目标的Agent
- [ ] 理解Agent的工作机制和执行流程
- [ ] 掌握Agent的高级配置（记忆、推理、工具）
- [ ] 能够优化Agent的性能参数

**✅ Task任务掌握程度**
- [ ] 能够设计结构化的Task定义
- [ ] 理解Task的上下文传递机制
- [ ] 掌握输出格式化和质量验证
- [ ] 能够实现Task的错误处理和重试

**✅ Crew团队掌握程度**
- [ ] 理解Sequential和Hierarchical执行模式
- [ ] 能够配置团队记忆和知识库
- [ ] 掌握回调函数和监控机制
- [ ] 能够优化团队协作效率

**✅ Flow工作流掌握程度**
- [ ] 理解事件驱动的工作流设计
- [ ] 掌握装饰器系统（@start, @listen, @router）
- [ ] 能够实现复杂的条件逻辑（and_, or_）
- [ ] 理解状态管理和持久化

### 8.2 实践成果展示

通过本实践指南，你已经构建了一个完整的智能市场分析系统，包含：

**🏗️ 系统架构**
```
智能市场分析系统
├── 🤖 Agent层: 3个专业智能体
├── 📋 Task层: 结构化任务系统
├── 🏰 Crew层: 协作团队管理
├── 🌊 Flow层: 智能工作流控制
├── 🛠️ 工具层: 自定义工具集成
└── 📊 监控层: 性能监控和日志
```

**📈 功能特性**
- ✅ 多模式执行：顺序、层级、工作流
- ✅ 智能路由：根据复杂度自动选择策略
- ✅ 质量保证：输出验证和错误重试
- ✅ 性能监控：执行时间和状态跟踪
- ✅ 扩展性：支持新行业和新功能

### 8.3 进阶学习建议

**🚀 下一步学习方向**

1. **工具系统深入**
   - 学习CrewAI内置工具的使用
   - 开发自定义工具和集成
   - 掌握工具链的组合使用

2. **高级Flow模式**
   - 学习更复杂的条件逻辑
   - 实现Flow的持久化和恢复
   - 掌握Flow的错误处理和容错

3. **企业级应用**
   - 学习大规模部署和运维
   - 掌握安全性和权限控制
   - 实现监控和告警系统

4. **性能优化**
   - 深入理解LLM调用优化
   - 学习缓存和内存管理
   - 掌握并发和异步处理

### 8.4 实践项目建议

基于本指南的学习，你可以尝试以下进阶项目：

**项目1: 智能客服系统**
- 使用多个Agent处理不同类型的客户问题
- 实现对话上下文的记忆和传递
- 构建知识库集成和智能路由

**项目2: 自动化内容创作平台**
- 设计内容策划、写作、编辑、发布的完整流程
- 实现多种内容格式的自动生成
- 构建质量评估和优化反馈循环

**项目3: 智能数据分析助手**
- 集成多种数据源和分析工具
- 实现自动化的数据清洗和分析
- 构建交互式的报告生成系统

---

## 🎉 恭喜完成实践！

你已经成功完成了CrewAI核心概念的完整实践！🎊

通过这个实践指南，你不仅理解了理论知识，更重要的是获得了：
- ✅ 完整的项目开发经验
- ✅ 系统化的问题解决能力
- ✅ 可扩展的代码架构设计
- ✅ 实用的调试和优化技巧

**🚀 继续你的CrewAI学习之旅！**

现在你已经具备了扎实的基础，可以继续学习CrewAI的高级特性，或者开始构建自己的智能体应用项目。

记住：实践是最好的老师，持续的项目实战将让你成为CrewAI专家！💪
```
