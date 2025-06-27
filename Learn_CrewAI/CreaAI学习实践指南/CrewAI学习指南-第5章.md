# 第5章：工具集成与自定义开发

> 🔧 给AI装上翅膀！学会使用和开发各种工具，让智能体拥有超能力。

## 📋 章节大纲

本章将全面介绍：

1. **🛠️ CrewAI内置工具详解** - 掌握强大的内置工具库
2. **🌐 第三方工具集成方法** - 连接外部服务和API
3. **🔧 自定义工具开发实战** - 为特定需求开发专门工具
4. **🎯 工具链设计和优化** - 构建高效的工具使用策略
5. **🛡️ 工具安全和权限管理** - 确保工具使用的安全性
6. **📊 工具性能监控** - 监控和优化工具性能
7. **🚀 高级工具开发技巧** - 掌握工具开发的最佳实践
8. **🎪 实战案例分析** - 通过实际案例学习工具应用

## 🎯 学习目标

完成本章学习后，你将能够：
- ✅ 熟练使用CrewAI提供的所有内置工具
- ✅ 掌握第三方工具集成的方法和最佳实践
- ✅ 独立开发满足特定需求的自定义工具
- ✅ 设计高效、安全的工具链架构
- ✅ 实现工具的性能监控和优化
- ✅ 具备解决复杂工具集成问题的能力

---

## 5.1 CrewAI内置工具详解🛠️

### 🎮 游戏化理解：装备系统

CrewAI的工具系统就像RPG游戏中的装备系统：

- **⚔️ 武器装备**：攻击型工具（搜索、分析）
- **🛡️ 防具装备**：防护型工具（验证、安全）
- **💎 饰品装备**：辅助型工具（文件、通信）
- **🧪 消耗品**：一次性工具（计算、转换）

每个Agent可以装备不同的工具组合，形成独特的能力配置。

### 📊 内置工具分类体系

```mermaid
graph TD
    A[CrewAI内置工具] --> B[🔍 信息获取工具]
    A --> C[📄 文件操作工具]
    A --> D[🌐 网络服务工具]
    A --> E[💻 代码执行工具]
    A --> F[🎨 内容创作工具]
    A --> G[🤝 协作通信工具]
    A --> H[☁️ 云服务工具]
    A --> I[🧠 AI/ML工具]

    B --> B1[SerperDevTool - 搜索引擎]
    B --> B2[WebsiteSearchTool - 网站搜索]
    B --> B3[ScrapeWebsiteTool - 网页抓取]

    C --> C1[FileReadTool - 文件读取]
    C --> C2[FileWriterTool - 文件写入]
    C --> C3[DirectoryReadTool - 目录读取]
    C --> C4[CSVSearchTool - CSV搜索]

    D --> D1[BrowserTool - 浏览器操作]
    D --> D2[YoutubeChannelSearchTool - YouTube搜索]
    D --> D3[YoutubeVideoSearchTool - 视频搜索]

    E --> E1[CodeInterpreterTool - 代码解释器]
    E --> E2[PythonCodeTool - Python执行]

    F --> F1[DallETool - 图像生成]
    F --> F2[VisionTool - 图像分析]

    G --> G1[DelegateWorkTool - 任务委派]
    G --> G2[AskQuestionTool - 询问同事]

    H --> H1[S3ReaderTool - S3读取]
    H --> H2[S3WriterTool - S3写入]
    H --> H3[BedrockInvokeAgentTool - Bedrock调用]

    I --> I1[EmbeddingSearchTool - 向量搜索]
    I --> I2[RAGTool - 检索增强生成]
```

### 🔍 信息获取工具详解

#### 1. SerperDevTool - 强大的搜索引擎

```python
# 🔍 SerperDevTool - 最常用的搜索工具
from crewai_tools import SerperDevTool

# 基础使用
search_tool = SerperDevTool()

# 高级配置
advanced_search_tool = SerperDevTool(
    search_url="https://google.serper.dev/search",
    n_results=10,           # 返回结果数量
    country="cn",           # 搜索地区
    locale="zh-cn",         # 语言设置
    time_range="y",         # 时间范围：d(天), w(周), m(月), y(年)
    search_type="search"    # 搜索类型：search, images, videos, news
)

# 在Agent中使用
research_agent = Agent(
    role="研究专家",
    goal="收集最新的行业信息",
    backstory="专业的信息收集专家...",
    tools=[advanced_search_tool],
    verbose=True
)

# 搜索示例
search_result = search_tool.run("CrewAI多智能体框架最新发展")
print(search_result)
```

#### 2. WebsiteSearchTool - 网站内容搜索

```python
# 🌐 WebsiteSearchTool - 在特定网站内搜索
from crewai_tools import WebsiteSearchTool

# 搜索特定网站
website_search = WebsiteSearchTool(
    website="https://docs.crewai.com",
    max_results=5,
    search_depth=3  # 搜索深度
)

# 使用示例
docs_agent = Agent(
    role="文档专家",
    goal="从官方文档中找到准确信息",
    backstory="熟悉技术文档的专家...",
    tools=[website_search],
    verbose=True
)
```

#### 3. ScrapeWebsiteTool - 网页内容抓取

```python
# 📄 ScrapeWebsiteTool - 抓取网页完整内容
from crewai_tools import ScrapeWebsiteTool

# 基础网页抓取
scrape_tool = ScrapeWebsiteTool()

# 高级配置
advanced_scrape_tool = ScrapeWebsiteTool(
    website_url="https://example.com",
    css_selector=".content",  # CSS选择器
    max_length=5000,          # 最大内容长度
    include_links=True        # 包含链接
)

# 使用示例
content_agent = Agent(
    role="内容分析师",
    goal="分析网页内容并提取关键信息",
    backstory="专业的内容分析专家...",
    tools=[advanced_scrape_tool],
    verbose=True
)
```

### 📄 文件操作工具详解

#### 1. FileReadTool - 文件读取工具

```python
# 📖 FileReadTool - 读取各种格式文件
from crewai_tools import FileReadTool

# 基础文件读取
file_reader = FileReadTool()

# 指定文件类型的读取器
text_reader = FileReadTool(
    file_path="documents/report.txt",
    encoding="utf-8"
)

json_reader = FileReadTool(
    file_path="data/config.json"
)

# 在Agent中使用
data_analyst = Agent(
    role="数据分析师",
    goal="分析文件中的数据",
    backstory="经验丰富的数据分析专家...",
    tools=[file_reader, text_reader, json_reader],
    verbose=True
)
```

#### 2. FileWriterTool - 文件写入工具

```python
# ✍️ FileWriterTool - 写入文件
from crewai_tools import FileWriterTool

# 基础文件写入
file_writer = FileWriterTool()

# 配置写入选项
configured_writer = FileWriterTool(
    directory="output",      # 输出目录
    filename="report.md",    # 文件名
    overwrite=True          # 是否覆盖
)

# 使用示例
report_agent = Agent(
    role="报告撰写员",
    goal="生成详细的分析报告",
    backstory="专业的报告写作专家...",
    tools=[file_writer],
    verbose=True
)
```

#### 3. CSVSearchTool - CSV数据搜索

```python
# 📊 CSVSearchTool - 在CSV文件中搜索数据
from crewai_tools import CSVSearchTool

# CSV搜索工具
csv_search = CSVSearchTool(
    csv_file_path="data/sales_data.csv",
    encoding="utf-8",
    delimiter=","
)

# 高级CSV搜索
advanced_csv_search = CSVSearchTool(
    csv_file_path="data/large_dataset.csv",
    search_columns=["name", "category", "description"],  # 指定搜索列
    case_sensitive=False,                                # 不区分大小写
    max_results=20                                       # 最大结果数
)

# 使用示例
data_researcher = Agent(
    role="数据研究员",
    goal="从CSV数据中找到相关信息",
    backstory="专业的数据挖掘专家...",
    tools=[csv_search, advanced_csv_search],
    verbose=True
)
```

### 💻 代码执行工具详解

#### 1. CodeInterpreterTool - 代码解释器

```python
# 💻 CodeInterpreterTool - 强大的代码执行工具
from crewai_tools import CodeInterpreterTool

# 基础代码解释器
code_interpreter = CodeInterpreterTool()

# 安全模式配置
safe_interpreter = CodeInterpreterTool(
    unsafe_mode=False,       # 安全模式
    timeout=30,              # 执行超时
    max_memory_mb=512        # 内存限制
)

# 高级配置
advanced_interpreter = CodeInterpreterTool(
    unsafe_mode=True,        # 允许更多操作
    workspace_dir="workspace", # 工作目录
    allowed_imports=[        # 允许的导入模块
        "pandas", "numpy", "matplotlib", "seaborn"
    ]
)

# 使用示例
data_scientist = Agent(
    role="数据科学家",
    goal="执行数据分析和可视化",
    backstory="精通Python数据分析的专家...",
    tools=[advanced_interpreter],
    verbose=True
)
```

#### 2. 代码执行最佳实践

```python
# 🎯 代码执行工具的最佳实践
class SafeCodeExecutor:
    """安全的代码执行器"""

    def __init__(self):
        self.interpreter = CodeInterpreterTool(
            unsafe_mode=False,
            timeout=60,
            max_memory_mb=1024
        )
        self.allowed_operations = [
            "data_analysis", "visualization", "calculation"
        ]

    def execute_data_analysis(self, code: str, data_path: str):
        """执行数据分析代码"""
        safe_code = f"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
data = pd.read_csv('{data_path}')

# 用户代码
{code}

# 保存结果
plt.savefig('analysis_result.png')
plt.close()
"""
        return self.interpreter.run(safe_code)

    def execute_calculation(self, formula: str, variables: dict):
        """执行数学计算"""
        safe_code = f"""
import math
import numpy as np

# 设置变量
{chr(10).join([f"{k} = {v}" for k, v in variables.items()])}

# 执行计算
result = {formula}
print(f"计算结果: {{result}}")
"""
        return self.interpreter.run(safe_code)

# 使用安全执行器
safe_executor = SafeCodeExecutor()

calculation_agent = Agent(
    role="计算专家",
    goal="执行安全的数学计算和数据分析",
    backstory="专业的计算和分析专家...",
    tools=[safe_executor.interpreter],
    verbose=True
)
```
### 🎨 内容创作工具详解

#### 1. DallETool - AI图像生成

```python
# 🎨 DallETool - DALL-E图像生成工具
from crewai_tools import DallETool

# 基础图像生成
dalle_tool = DallETool()

# 高级配置
advanced_dalle = DallETool(
    model="dall-e-3",        # 模型版本
    size="1024x1024",        # 图像尺寸
    quality="hd",            # 图像质量
    style="vivid"            # 图像风格
)

# 使用示例
creative_agent = Agent(
    role="创意设计师",
    goal="生成高质量的创意图像",
    backstory="富有创意的视觉设计专家...",
    tools=[advanced_dalle],
    verbose=True
)
```

#### 2. VisionTool - 图像分析工具

```python
# 👁️ VisionTool - 图像理解和分析
from crewai_tools import VisionTool

# 图像分析工具
vision_tool = VisionTool()

# 配置分析选项
detailed_vision = VisionTool(
    max_tokens=1000,         # 最大分析长度
    detail_level="high",     # 分析详细程度
    include_objects=True,    # 包含物体识别
    include_text=True        # 包含文字识别
)

# 使用示例
image_analyst = Agent(
    role="图像分析师",
    goal="深入分析图像内容并提供详细描述",
    backstory="专业的计算机视觉专家...",
    tools=[detailed_vision],
    verbose=True
)
```

### 🤝 协作通信工具详解

#### 1. DelegateWorkTool - 任务委派工具

```python
# 🤝 DelegateWorkTool - 智能任务委派
from crewai.tools import DelegateWorkTool

# 任务委派工具（通常由Crew自动配置）
class SmartDelegationAgent(Agent):
    """智能委派Agent"""

    def __init__(self, team_agents):
        super().__init__(
            role="项目协调员",
            goal="智能分配任务给最合适的团队成员",
            backstory="经验丰富的项目管理专家...",
            allow_delegation=True,  # 启用委派功能
            verbose=True
        )
        self.team_agents = team_agents

    def delegate_task_intelligently(self, task_description, task_complexity):
        """智能委派任务"""
        # 分析任务类型
        if "数据" in task_description or "分析" in task_description:
            best_agent = self.find_agent_by_role("数据分析师")
        elif "设计" in task_description or "创意" in task_description:
            best_agent = self.find_agent_by_role("设计师")
        elif "代码" in task_description or "开发" in task_description:
            best_agent = self.find_agent_by_role("开发工程师")
        else:
            best_agent = self.find_most_available_agent()

        return f"将任务委派给: {best_agent.role}"

    def find_agent_by_role(self, role):
        """根据角色找到Agent"""
        for agent in self.team_agents:
            if role in agent.role:
                return agent
        return self.team_agents[0]  # 默认返回第一个

    def find_most_available_agent(self):
        """找到最空闲的Agent"""
        # 这里可以实现负载均衡逻辑
        return self.team_agents[0]
```

#### 2. AskQuestionTool - 询问同事工具

```python
# ❓ AskQuestionTool - 智能询问工具
from crewai.tools import AskQuestionTool

class CollaborativeAgent(Agent):
    """协作型Agent"""

    def __init__(self, name, role, team_agents):
        super().__init__(
            role=role,
            goal=f"作为{role}，与团队协作完成任务",
            backstory=f"经验丰富的{role}，善于团队协作...",
            verbose=True
        )
        self.name = name
        self.team_agents = team_agents

    def ask_expert_opinion(self, question, expert_role):
        """向专家询问意见"""
        expert = self.find_expert(expert_role)
        if expert:
            return f"向{expert.role}询问: {question}"
        return "未找到相关专家"

    def find_expert(self, role):
        """找到特定角色的专家"""
        for agent in self.team_agents:
            if role.lower() in agent.role.lower():
                return agent
        return None

    def collaborative_decision(self, decision_topic):
        """协作决策"""
        opinions = []
        for agent in self.team_agents:
            if agent != self:
                opinion = f"{agent.role}的观点: 基于我的专业经验..."
                opinions.append(opinion)

        return {
            "topic": decision_topic,
            "team_opinions": opinions,
            "consensus": "基于团队讨论的共识..."
        }
```

---

## 5.2 第三方工具集成方法🌐

### 🎮 游戏化理解：插件系统

第三方工具集成就像游戏的插件系统：

- **🔌 官方插件**：CrewAI Tools生态系统
- **🛠️ 社区插件**：LangChain Tools
- **⚙️ 自制插件**：自定义API集成
- **🔧 工具链**：多个插件的组合使用

### 📊 第三方工具生态系统

```mermaid
graph TD
    A[第三方工具生态] --> B[🏢 企业服务工具]
    A --> C[🌐 Web服务工具]
    A --> D[📊 数据服务工具]
    A --> E[🤖 AI服务工具]
    A --> F[☁️ 云平台工具]

    B --> B1[Slack, Teams, Discord]
    B --> B2[Jira, Asana, Trello]
    B --> B3[Salesforce, HubSpot]

    C --> C1[REST API, GraphQL]
    C --> C2[WebSocket, SSE]
    C --> C3[OAuth, JWT认证]

    D --> D1[MySQL, PostgreSQL]
    D --> D2[MongoDB, Redis]
    D --> D3[Elasticsearch, InfluxDB]

    E --> E1[OpenAI, Anthropic]
    E --> E2[Hugging Face, Cohere]
    E --> E3[Google AI, Azure AI]

    F --> F1[AWS, Azure, GCP]
    F --> F2[Docker, Kubernetes]
    F --> F3[Serverless Functions]
```

### 🔌 LangChain工具集成

#### 1. 集成LangChain工具

```python
# 🔗 集成LangChain工具到CrewAI
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from crewai import Agent

# 创建LangChain工具
ddg_search = DuckDuckGoSearchRun()
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# 包装为CrewAI兼容的工具
def create_langchain_tool_wrapper(langchain_tool, name, description):
    """将LangChain工具包装为CrewAI工具"""
    from crewai.tools import BaseTool
    from pydantic import BaseModel, Field
    from typing import Type

    class ToolInput(BaseModel):
        query: str = Field(description="查询内容")

    class WrappedTool(BaseTool):
        name: str = name
        description: str = description
        args_schema: Type[BaseModel] = ToolInput

        def _run(self, query: str) -> str:
            return langchain_tool.run(query)

    return WrappedTool()

# 创建包装后的工具
ddg_tool = create_langchain_tool_wrapper(
    ddg_search,
    "DuckDuckGo搜索",
    "使用DuckDuckGo搜索引擎搜索信息"
)

wiki_tool = create_langchain_tool_wrapper(
    wikipedia,
    "维基百科查询",
    "在维基百科中查询相关信息"
)

# 在Agent中使用
research_agent = Agent(
    role="研究专家",
    goal="使用多种搜索引擎收集信息",
    backstory="专业的信息收集和验证专家...",
    tools=[ddg_tool, wiki_tool],
    verbose=True
)
```

#### 2. 数据库工具集成

```python
# 🗄️ 数据库工具集成
import sqlite3
import psycopg2
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class DatabaseQueryInput(BaseModel):
    """数据库查询输入"""
    query: str = Field(description="SQL查询语句")
    database: str = Field(description="数据库名称", default="default")

class SQLiteTool(BaseTool):
    """SQLite数据库工具"""
    name: str = "SQLite查询工具"
    description: str = "执行SQLite数据库查询"
    args_schema: Type[BaseModel] = DatabaseQueryInput

    def __init__(self, db_path: str):
        super().__init__()
        self.db_path = db_path

    def _run(self, query: str, database: str = "default") -> str:
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query)

            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                columns = [description[0] for description in cursor.description]

                # 格式化结果
                formatted_results = []
                for row in results:
                    row_dict = dict(zip(columns, row))
                    formatted_results.append(row_dict)

                return f"查询结果: {formatted_results}"
            else:
                conn.commit()
                return f"查询执行成功，影响行数: {cursor.rowcount}"

        except Exception as e:
            return f"数据库查询错误: {str(e)}"
        finally:
            conn.close()

class PostgreSQLTool(BaseTool):
    """PostgreSQL数据库工具"""
    name: str = "PostgreSQL查询工具"
    description: str = "执行PostgreSQL数据库查询"
    args_schema: Type[BaseModel] = DatabaseQueryInput

    def __init__(self, connection_string: str):
        super().__init__()
        self.connection_string = connection_string

    def _run(self, query: str, database: str = "default") -> str:
        try:
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute(query)

            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                formatted_results = []
                for row in results:
                    row_dict = dict(zip(columns, row))
                    formatted_results.append(row_dict)

                return f"查询结果: {formatted_results}"
            else:
                conn.commit()
                return f"查询执行成功，影响行数: {cursor.rowcount}"

        except Exception as e:
            return f"数据库查询错误: {str(e)}"
        finally:
            conn.close()

# 使用数据库工具
sqlite_tool = SQLiteTool("data/company.db")
postgres_tool = PostgreSQLTool("postgresql://user:password@localhost/dbname")

data_analyst = Agent(
    role="数据分析师",
    goal="从数据库中提取和分析数据",
    backstory="专业的数据库查询和分析专家...",
    tools=[sqlite_tool, postgres_tool],
    verbose=True
)
```

#### 3. API服务集成

```python
# 🌐 REST API服务集成
import requests
import json
from typing import Type, Optional, Dict, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class APIRequestInput(BaseModel):
    """API请求输入"""
    endpoint: str = Field(description="API端点路径")
    method: str = Field(description="HTTP方法", default="GET")
    params: Optional[Dict[str, Any]] = Field(description="查询参数", default=None)
    data: Optional[Dict[str, Any]] = Field(description="请求数据", default=None)

class RESTAPITool(BaseTool):
    """通用REST API工具"""
    name: str = "REST API工具"
    description: str = "调用REST API服务"
    args_schema: Type[BaseModel] = APIRequestInput

    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        super().__init__()
        self.base_url = base_url.rstrip('/')
        self.headers = headers or {}

    def _run(self, endpoint: str, method: str = "GET",
             params: Optional[Dict[str, Any]] = None,
             data: Optional[Dict[str, Any]] = None) -> str:
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"

            response = requests.request(
                method=method.upper(),
                url=url,
                headers=self.headers,
                params=params,
                json=data,
                timeout=30
            )

            response.raise_for_status()

            try:
                result = response.json()
                return json.dumps(result, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                return response.text

        except requests.exceptions.RequestException as e:
            return f"API请求错误: {str(e)}"

# 特定服务的API工具
class WeatherAPITool(BaseTool):
    """天气API工具"""
    name: str = "天气查询工具"
    description: str = "查询指定城市的天气信息"
    args_schema: Type[BaseModel] = BaseModel

    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def _run(self, city: str) -> str:
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric",
                "lang": "zh_cn"
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            weather_info = {
                "城市": data["name"],
                "温度": f"{data['main']['temp']}°C",
                "体感温度": f"{data['main']['feels_like']}°C",
                "湿度": f"{data['main']['humidity']}%",
                "天气": data["weather"][0]["description"],
                "风速": f"{data['wind']['speed']} m/s"
            }

            return json.dumps(weather_info, ensure_ascii=False, indent=2)

        except Exception as e:
            return f"天气查询失败: {str(e)}"

# 使用API工具
weather_tool = WeatherAPITool(api_key="your_openweather_api_key")
generic_api_tool = RESTAPITool(
    base_url="https://api.example.com",
    headers={"Authorization": "Bearer your_token"}
)

api_agent = Agent(
    role="API集成专家",
    goal="调用各种外部API服务获取数据",
    backstory="专业的API集成和数据获取专家...",
    tools=[weather_tool, generic_api_tool],
    verbose=True
)
```

---

## 5.3 自定义工具开发实战🔧

### 🎮 游戏化理解：装备锻造系统

自定义工具开发就像游戏中的装备锻造：

- **⚒️ 基础锻造**：继承BaseTool创建简单工具
- **🔥 高级锻造**：复杂逻辑和状态管理
- **💎 传说锻造**：集成多种技术的复合工具
- **🌟 神器锻造**：具有学习能力的智能工具

### 📊 自定义工具开发流程

```mermaid
graph TD
    A[需求分析] --> B[工具设计]
    B --> C[基础实现]
    C --> D[功能测试]
    D --> E[性能优化]
    E --> F[安全加固]
    F --> G[文档编写]
    G --> H[部署发布]

    B --> B1[定义输入输出]
    B --> B2[设计错误处理]
    B --> B3[规划扩展性]

    C --> C1[继承BaseTool]
    C --> C2[实现_run方法]
    C --> C3[定义参数模型]

    D --> D1[单元测试]
    D --> D2[集成测试]
    D --> D3[边界测试]

    E --> E1[缓存机制]
    E --> E2[异步处理]
    E --> E3[资源管理]
```

### 🛠️ 基础工具开发

#### 1. 简单计算工具

```python
# 🧮 基础计算工具开发
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import math

class CalculatorInput(BaseModel):
    """计算器输入模型"""
    expression: str = Field(description="数学表达式，如：2+3*4")
    precision: int = Field(description="小数点精度", default=2)

class AdvancedCalculatorTool(BaseTool):
    """高级计算器工具"""
    name: str = "高级计算器"
    description: str = "执行复杂数学计算，支持基础运算、三角函数、对数等"
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, expression: str, precision: int = 2) -> str:
        """执行数学计算"""
        try:
            # 安全的数学函数映射
            safe_dict = {
                "__builtins__": {},
                "abs": abs, "round": round, "min": min, "max": max,
                "sum": sum, "pow": pow,
                # 数学函数
                "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "asin": math.asin, "acos": math.acos, "atan": math.atan,
                "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
                "log": math.log, "log10": math.log10, "log2": math.log2,
                "exp": math.exp, "sqrt": math.sqrt,
                "pi": math.pi, "e": math.e,
                "degrees": math.degrees, "radians": math.radians,
                "factorial": math.factorial,
                "gcd": math.gcd, "lcm": math.lcm if hasattr(math, 'lcm') else lambda a, b: abs(a*b) // math.gcd(a, b)
            }

            # 预处理表达式
            expression = expression.replace("^", "**")  # 支持^作为幂运算

            # 执行计算
            result = eval(expression, safe_dict)

            # 格式化结果
            if isinstance(result, float):
                result = round(result, precision)

            return f"计算结果: {result}"

        except ZeroDivisionError:
            return "错误: 除零错误"
        except ValueError as e:
            return f"错误: 数值错误 - {str(e)}"
        except SyntaxError:
            return "错误: 表达式语法错误"
        except Exception as e:
            return f"错误: 计算失败 - {str(e)}"

# 使用示例
calculator_tool = AdvancedCalculatorTool()

math_agent = Agent(
    role="数学计算专家",
    goal="执行各种数学计算任务",
    backstory="精通数学计算的专业助手...",
    tools=[calculator_tool],
    verbose=True
)
```

#### 2. 文本处理工具

```python
# 📝 文本处理工具开发
import re
import jieba
from collections import Counter
from typing import Type, List, Dict
import json

class TextProcessorInput(BaseModel):
    """文本处理输入模型"""
    text: str = Field(description="要处理的文本")
    operation: str = Field(description="处理操作：word_count, sentiment, keywords, summary")
    language: str = Field(description="文本语言", default="zh")

class TextProcessorTool(BaseTool):
    """智能文本处理工具"""
    name: str = "文本处理工具"
    description: str = "提供文本分析、关键词提取、情感分析等功能"
    args_schema: Type[BaseModel] = TextProcessorInput

    def __init__(self):
        super().__init__()
        # 初始化中文分词
        jieba.initialize()

        # 停用词列表
        self.stop_words = {
            '的', '了', '在', '是', '我', '有', '和', '就', '不', '人',
            '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去',
            '你', '会', '着', '没有', '看', '好', '自己', '这'
        }

    def _run(self, text: str, operation: str, language: str = "zh") -> str:
        """执行文本处理操作"""
        try:
            if operation == "word_count":
                return self._word_count(text, language)
            elif operation == "sentiment":
                return self._sentiment_analysis(text)
            elif operation == "keywords":
                return self._extract_keywords(text, language)
            elif operation == "summary":
                return self._text_summary(text)
            else:
                return f"不支持的操作: {operation}"

        except Exception as e:
            return f"文本处理错误: {str(e)}"

    def _word_count(self, text: str, language: str) -> str:
        """词频统计"""
        if language == "zh":
            words = jieba.lcut(text)
            words = [w for w in words if w not in self.stop_words and len(w) > 1]
        else:
            words = re.findall(r'\b\w+\b', text.lower())

        word_count = Counter(words)
        total_words = len(words)
        unique_words = len(word_count)

        top_words = word_count.most_common(10)

        result = {
            "总词数": total_words,
            "唯一词数": unique_words,
            "词汇丰富度": round(unique_words / total_words, 3) if total_words > 0 else 0,
            "高频词汇": dict(top_words)
        }

        return f"词频统计结果:\n{json.dumps(result, ensure_ascii=False, indent=2)}"

    def _sentiment_analysis(self, text: str) -> str:
        """简单情感分析"""
        positive_words = ['好', '棒', '优秀', '喜欢', '满意', '开心', '高兴', '赞']
        negative_words = ['坏', '差', '糟糕', '讨厌', '不满', '难过', '生气', '失望']

        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)

        if positive_count > negative_count:
            sentiment = "积极"
            confidence = positive_count / (positive_count + negative_count)
        elif negative_count > positive_count:
            sentiment = "消极"
            confidence = negative_count / (positive_count + negative_count)
        else:
            sentiment = "中性"
            confidence = 0.5

        return f"情感分析结果: {sentiment} (置信度: {confidence:.2f})"

    def _extract_keywords(self, text: str, language: str) -> str:
        """关键词提取"""
        if language == "zh":
            words = jieba.lcut(text)
            words = [w for w in words if w not in self.stop_words and len(w) > 1]
        else:
            words = re.findall(r'\b\w+\b', text.lower())

        word_freq = Counter(words)
        keywords = word_freq.most_common(5)

        return f"关键词: {', '.join([word for word, freq in keywords])}"

    def _text_summary(self, text: str) -> str:
        """文本摘要（简单实现）"""
        sentences = re.split(r'[。！？]', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) <= 2:
            return f"摘要: {text}"

        # 简单选择前两句作为摘要
        summary = '。'.join(sentences[:2]) + '。'
        return f"摘要: {summary}"

# 使用示例
text_processor = TextProcessorTool()

text_agent = Agent(
    role="文本分析专家",
    goal="分析和处理各种文本内容",
    backstory="专业的自然语言处理专家...",
    tools=[text_processor],
    verbose=True
)
```

### 🔥 高级工具开发

#### 1. 带状态管理的工具

```python
# 🔄 带状态管理的高级工具
import json
import os
from datetime import datetime
from typing import Type, Dict, Any, Optional

class StatefulToolInput(BaseModel):
    """状态工具输入模型"""
    action: str = Field(description="操作类型：save, load, update, delete, list")
    key: str = Field(description="数据键名", default="")
    value: Any = Field(description="数据值", default=None)
    namespace: str = Field(description="命名空间", default="default")

class StatefulDataTool(BaseTool):
    """带状态管理的数据工具"""
    name: str = "状态数据工具"
    description: str = "管理持久化数据状态，支持保存、加载、更新数据"
    args_schema: Type[BaseModel] = StatefulToolInput

    def __init__(self, storage_path: str = "tool_data"):
        super().__init__()
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
        self._memory_cache = {}

    def _get_file_path(self, namespace: str) -> str:
        """获取存储文件路径"""
        return os.path.join(self.storage_path, f"{namespace}.json")

    def _load_namespace(self, namespace: str) -> Dict[str, Any]:
        """加载命名空间数据"""
        if namespace in self._memory_cache:
            return self._memory_cache[namespace]

        file_path = self._get_file_path(namespace)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self._memory_cache[namespace] = data
                return data
            except Exception:
                pass

        self._memory_cache[namespace] = {}
        return {}

    def _save_namespace(self, namespace: str, data: Dict[str, Any]) -> bool:
        """保存命名空间数据"""
        try:
            file_path = self._get_file_path(namespace)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self._memory_cache[namespace] = data
            return True
        except Exception:
            return False

    def _run(self, action: str, key: str = "", value: Any = None, namespace: str = "default") -> str:
        """执行状态操作"""
        try:
            data = self._load_namespace(namespace)

            if action == "save":
                if not key:
                    return "错误: 保存操作需要指定key"
                data[key] = {
                    "value": value,
                    "timestamp": datetime.now().isoformat(),
                    "type": type(value).__name__
                }
                if self._save_namespace(namespace, data):
                    return f"成功保存: {key} = {value}"
                else:
                    return "保存失败"

            elif action == "load":
                if not key:
                    return "错误: 加载操作需要指定key"
                if key in data:
                    item = data[key]
                    return f"加载成功: {key} = {item['value']} (保存时间: {item['timestamp']})"
                else:
                    return f"未找到数据: {key}"

            elif action == "update":
                if not key:
                    return "错误: 更新操作需要指定key"
                if key in data:
                    data[key]["value"] = value
                    data[key]["timestamp"] = datetime.now().isoformat()
                    if self._save_namespace(namespace, data):
                        return f"成功更新: {key} = {value}"
                    else:
                        return "更新失败"
                else:
                    return f"未找到数据: {key}"

            elif action == "delete":
                if not key:
                    return "错误: 删除操作需要指定key"
                if key in data:
                    del data[key]
                    if self._save_namespace(namespace, data):
                        return f"成功删除: {key}"
                    else:
                        return "删除失败"
                else:
                    return f"未找到数据: {key}"

            elif action == "list":
                if not data:
                    return f"命名空间 '{namespace}' 中没有数据"

                result = f"命名空间 '{namespace}' 中的数据:\n"
                for k, v in data.items():
                    result += f"- {k}: {v['value']} ({v['type']}, {v['timestamp']})\n"
                return result

            else:
                return f"不支持的操作: {action}"

        except Exception as e:
            return f"操作失败: {str(e)}"

# 使用示例
stateful_tool = StatefulDataTool()

memory_agent = Agent(
    role="数据管理专家",
    goal="管理和维护持久化数据状态",
    backstory="专业的数据管理和状态维护专家...",
    tools=[stateful_tool],
    verbose=True
)
```

#### 2. 异步处理工具

```python
# ⚡ 异步处理工具
import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Type, List, Dict, Any

class AsyncTaskInput(BaseModel):
    """异步任务输入模型"""
    task_type: str = Field(description="任务类型：batch_request, parallel_process, background_task")
    urls: List[str] = Field(description="URL列表", default=[])
    data: List[Dict[str, Any]] = Field(description="数据列表", default=[])
    timeout: int = Field(description="超时时间（秒）", default=30)

class AsyncProcessingTool(BaseTool):
    """异步处理工具"""
    name: str = "异步处理工具"
    description: str = "执行异步任务，支持批量请求、并行处理等"
    args_schema: Type[BaseModel] = AsyncTaskInput

    def __init__(self, max_workers: int = 10):
        super().__init__()
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    async def _batch_http_requests(self, urls: List[str], timeout: int) -> List[Dict[str, Any]]:
        """批量HTTP请求"""
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
            tasks = []
            for url in urls:
                tasks.append(self._single_request(session, url))

            results = await asyncio.gather(*tasks, return_exceptions=True)

            formatted_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    formatted_results.append({
                        "url": urls[i],
                        "status": "error",
                        "error": str(result)
                    })
                else:
                    formatted_results.append(result)

            return formatted_results

    async def _single_request(self, session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
        """单个HTTP请求"""
        try:
            async with session.get(url) as response:
                content = await response.text()
                return {
                    "url": url,
                    "status": "success",
                    "status_code": response.status,
                    "content_length": len(content),
                    "headers": dict(response.headers)
                }
        except Exception as e:
            return {
                "url": url,
                "status": "error",
                "error": str(e)
            }

    def _parallel_data_processing(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """并行数据处理"""
        def process_item(item):
            # 模拟数据处理
            time.sleep(0.1)  # 模拟处理时间
            processed_item = item.copy()
            processed_item['processed'] = True
            processed_item['process_time'] = time.time()
            return processed_item

        # 使用线程池并行处理
        futures = [self.executor.submit(process_item, item) for item in data]
        results = [future.result() for future in futures]

        return results

    def _run(self, task_type: str, urls: List[str] = None, data: List[Dict[str, Any]] = None, timeout: int = 30) -> str:
        """执行异步任务"""
        try:
            start_time = time.time()

            if task_type == "batch_request":
                if not urls:
                    return "错误: 批量请求需要提供URL列表"

                # 运行异步批量请求
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    results = loop.run_until_complete(self._batch_http_requests(urls, timeout))
                finally:
                    loop.close()

                success_count = sum(1 for r in results if r.get('status') == 'success')
                error_count = len(results) - success_count

                return f"批量请求完成:\n成功: {success_count}\n失败: {error_count}\n耗时: {time.time() - start_time:.2f}秒"

            elif task_type == "parallel_process":
                if not data:
                    return "错误: 并行处理需要提供数据列表"

                results = self._parallel_data_processing(data)

                return f"并行处理完成:\n处理项目数: {len(results)}\n耗时: {time.time() - start_time:.2f}秒"

            elif task_type == "background_task":
                # 提交后台任务
                future = self.executor.submit(self._background_task, data or [])
                return f"后台任务已提交，任务ID: {id(future)}"

            else:
                return f"不支持的任务类型: {task_type}"

        except Exception as e:
            return f"异步任务执行失败: {str(e)}"

    def _background_task(self, data: List[Dict[str, Any]]) -> str:
        """后台任务处理"""
        time.sleep(5)  # 模拟长时间处理
        return f"后台任务完成，处理了 {len(data)} 个项目"

# 使用示例
async_tool = AsyncProcessingTool(max_workers=5)

async_agent = Agent(
    role="异步处理专家",
    goal="执行高效的异步和并行任务",
    backstory="专业的异步编程和性能优化专家...",
    tools=[async_tool],
    verbose=True
)
```

---

## 5.4 工具链设计和优化🎯

### 🎮 游戏化理解：技能组合系统

工具链设计就像游戏中的技能组合：

- **⚡ 连击技能**：工具的顺序调用
- **🔄 循环技能**：工具的循环使用
- **🌟 终极技能**：多工具协同作战
- **🎯 精准技能**：针对特定场景的工具组合

### 📊 工具链设计原则

```mermaid
graph TD
    A[工具链设计原则] --> B[🎯 单一职责]
    A --> C[🔗 松耦合]
    A --> D[⚡ 高性能]
    A --> E[🛡️ 容错性]
    A --> F[📈 可扩展]

    B --> B1[每个工具专注一个功能]
    B --> B2[避免功能重叠]
    B --> B3[清晰的输入输出]

    C --> C1[工具间独立运行]
    C --> C2[标准化接口]
    C --> C3[最小依赖]

    D --> D1[缓存机制]
    D --> D2[异步处理]
    D --> D3[资源复用]

    E --> E1[优雅降级]
    E --> E2[错误恢复]
    E --> E3[超时处理]

    F --> F1[插件化架构]
    F --> F2[配置驱动]
    F --> F3[版本兼容]
```

### 🔗 工具链组合模式

#### 1. 管道模式（Pipeline Pattern）

```python
# 🔄 管道模式工具链
from typing import List, Any, Callable
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class PipelineInput(BaseModel):
    """管道输入模型"""
    data: Any = Field(description="输入数据")
    pipeline_name: str = Field(description="管道名称", default="default")

class ToolPipeline(BaseTool):
    """工具管道"""
    name: str = "工具管道"
    description: str = "按顺序执行多个工具，前一个工具的输出作为下一个工具的输入"
    args_schema: Type[BaseModel] = PipelineInput

    def __init__(self, tools: List[BaseTool], name: str = "default"):
        super().__init__()
        self.tools = tools
        self.pipeline_name = name
        self.execution_log = []

    def _run(self, data: Any, pipeline_name: str = "default") -> str:
        """执行管道"""
        try:
            current_data = data
            self.execution_log = []

            for i, tool in enumerate(self.tools):
                step_start = time.time()

                try:
                    # 执行工具
                    if hasattr(tool, '_run'):
                        result = tool._run(current_data)
                    else:
                        result = tool.run(current_data)

                    # 记录执行日志
                    step_log = {
                        "step": i + 1,
                        "tool": tool.name,
                        "input": str(current_data)[:100],  # 限制日志长度
                        "output": str(result)[:100],
                        "duration": time.time() - step_start,
                        "status": "success"
                    }
                    self.execution_log.append(step_log)

                    # 更新数据
                    current_data = result

                except Exception as e:
                    step_log = {
                        "step": i + 1,
                        "tool": tool.name,
                        "input": str(current_data)[:100],
                        "error": str(e),
                        "duration": time.time() - step_start,
                        "status": "error"
                    }
                    self.execution_log.append(step_log)

                    # 错误处理：可以选择中断或继续
                    return f"管道执行失败在步骤 {i+1}: {str(e)}"

            # 返回最终结果和执行日志
            return f"管道执行完成:\n最终结果: {current_data}\n执行日志: {json.dumps(self.execution_log, ensure_ascii=False, indent=2)}"

        except Exception as e:
            return f"管道执行错误: {str(e)}"

# 创建具体的管道工具
class DataProcessingPipeline:
    """数据处理管道"""

    def __init__(self):
        # 创建管道中的工具
        self.text_processor = TextProcessorTool()
        self.calculator = AdvancedCalculatorTool()

        # 创建管道
        self.pipeline = ToolPipeline([
            self.text_processor,
            self.calculator
        ], name="数据处理管道")

    def create_content_analysis_pipeline(self) -> ToolPipeline:
        """创建内容分析管道"""
        tools = [
            TextProcessorTool(),  # 文本处理
            # 可以添加更多工具
        ]
        return ToolPipeline(tools, name="内容分析管道")

# 使用示例
data_pipeline = DataProcessingPipeline()

pipeline_agent = Agent(
    role="管道处理专家",
    goal="使用工具管道高效处理复杂任务",
    backstory="专业的流程设计和自动化专家...",
    tools=[data_pipeline.pipeline],
    verbose=True
)
```

#### 2. 分支模式（Branch Pattern）

```python
# 🌳 分支模式工具链
class BranchInput(BaseModel):
    """分支输入模型"""
    data: Any = Field(description="输入数据")
    condition: str = Field(description="分支条件")
    branch_type: str = Field(description="分支类型", default="conditional")

class ConditionalToolBranch(BaseTool):
    """条件分支工具"""
    name: str = "条件分支工具"
    description: str = "根据条件选择不同的工具执行路径"
    args_schema: Type[BaseModel] = BranchInput

    def __init__(self, branches: Dict[str, List[BaseTool]]):
        super().__init__()
        self.branches = branches
        self.default_branch = "default"

    def _run(self, data: Any, condition: str, branch_type: str = "conditional") -> str:
        """执行分支逻辑"""
        try:
            # 根据条件选择分支
            selected_branch = self._evaluate_condition(condition, data)

            if selected_branch not in self.branches:
                selected_branch = self.default_branch

            if selected_branch not in self.branches:
                return f"错误: 未找到分支 '{selected_branch}'"

            # 执行选中分支的工具
            tools = self.branches[selected_branch]
            results = []

            for tool in tools:
                try:
                    if hasattr(tool, '_run'):
                        result = tool._run(data)
                    else:
                        result = tool.run(data)
                    results.append(f"{tool.name}: {result}")
                except Exception as e:
                    results.append(f"{tool.name}: 错误 - {str(e)}")

            return f"分支 '{selected_branch}' 执行结果:\n" + "\n".join(results)

        except Exception as e:
            return f"分支执行错误: {str(e)}"

    def _evaluate_condition(self, condition: str, data: Any) -> str:
        """评估条件"""
        # 简单的条件评估逻辑
        if "文本" in str(data) or "text" in condition.lower():
            return "text_processing"
        elif "数字" in str(data) or "number" in condition.lower():
            return "number_processing"
        elif "数据" in str(data) or "data" in condition.lower():
            return "data_processing"
        else:
            return "default"

# 创建分支工具
text_tools = [TextProcessorTool()]
number_tools = [AdvancedCalculatorTool()]
data_tools = [StatefulDataTool()]

branch_tool = ConditionalToolBranch({
    "text_processing": text_tools,
    "number_processing": number_tools,
    "data_processing": data_tools,
    "default": text_tools + number_tools
})

branch_agent = Agent(
    role="智能分支专家",
    goal="根据数据类型智能选择处理工具",
    backstory="专业的智能决策和路径选择专家...",
    tools=[branch_tool],
    verbose=True
)
```

---

## 5.5 工具安全和权限管理🛡️

### 🎮 游戏化理解：权限系统

工具安全管理就像游戏中的权限系统：

- **🔐 访问控制**：谁可以使用什么工具
- **🛡️ 安全沙箱**：限制工具的执行环境
- **📊 审计日志**：记录所有工具使用情况
- **⚠️ 风险评估**：评估工具操作的风险等级

### 📊 安全架构设计

```mermaid
graph TD
    A[工具安全架构] --> B[🔐 身份认证]
    A --> C[🛡️ 权限控制]
    A --> D[🏰 安全沙箱]
    A --> E[📊 审计监控]
    A --> F[⚠️ 风险管理]

    B --> B1[用户身份验证]
    B --> B2[Agent身份验证]
    B --> B3[API密钥管理]

    C --> C1[基于角色的访问控制]
    C --> C2[资源级权限]
    C --> C3[操作级权限]

    D --> D1[执行环境隔离]
    D --> D2[资源使用限制]
    D --> D3[网络访问控制]

    E --> E1[操作日志记录]
    E --> E2[性能监控]
    E --> E3[异常检测]

    F --> F1[风险等级评估]
    F --> F2[自动风险响应]
    F --> F3[安全策略更新]
```

### 🔐 权限控制系统

#### 1. 基于角色的访问控制（RBAC）

```python
# 🔐 基于角色的访问控制系统
from enum import Enum
from typing import Set, Dict, List, Optional
import hashlib
import time
from dataclasses import dataclass

class Permission(Enum):
    """权限枚举"""
    READ_FILE = "read_file"
    WRITE_FILE = "write_file"
    EXECUTE_CODE = "execute_code"
    NETWORK_ACCESS = "network_access"
    DATABASE_ACCESS = "database_access"
    SYSTEM_ADMIN = "system_admin"
    API_CALL = "api_call"
    DATA_EXPORT = "data_export"

class RiskLevel(Enum):
    """风险等级"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class Role:
    """角色定义"""
    name: str
    permissions: Set[Permission]
    risk_level: RiskLevel
    description: str

@dataclass
class User:
    """用户定义"""
    username: str
    roles: Set[str]
    api_key: str
    created_at: float
    last_active: float

class SecurityManager:
    """安全管理器"""

    def __init__(self):
        self.roles: Dict[str, Role] = {}
        self.users: Dict[str, User] = {}
        self.audit_log: List[Dict] = []
        self._init_default_roles()

    def _init_default_roles(self):
        """初始化默认角色"""
        self.roles = {
            "guest": Role(
                name="guest",
                permissions={Permission.READ_FILE},
                risk_level=RiskLevel.LOW,
                description="访客用户，只能读取文件"
            ),
            "user": Role(
                name="user",
                permissions={Permission.READ_FILE, Permission.WRITE_FILE, Permission.API_CALL},
                risk_level=RiskLevel.MEDIUM,
                description="普通用户，可以读写文件和调用API"
            ),
            "developer": Role(
                name="developer",
                permissions={
                    Permission.READ_FILE, Permission.WRITE_FILE,
                    Permission.EXECUTE_CODE, Permission.API_CALL,
                    Permission.NETWORK_ACCESS
                },
                risk_level=RiskLevel.HIGH,
                description="开发者，可以执行代码和网络访问"
            ),
            "admin": Role(
                name="admin",
                permissions=set(Permission),  # 所有权限
                risk_level=RiskLevel.CRITICAL,
                description="管理员，拥有所有权限"
            )
        }

    def create_user(self, username: str, roles: List[str]) -> str:
        """创建用户"""
        api_key = self._generate_api_key(username)
        user = User(
            username=username,
            roles=set(roles),
            api_key=api_key,
            created_at=time.time(),
            last_active=time.time()
        )
        self.users[username] = user

        self._log_audit("CREATE_USER", username, {"roles": roles})
        return api_key

    def _generate_api_key(self, username: str) -> str:
        """生成API密钥"""
        timestamp = str(time.time())
        raw_key = f"{username}:{timestamp}:secret_salt"
        return hashlib.sha256(raw_key.encode()).hexdigest()

    def authenticate(self, api_key: str) -> Optional[User]:
        """认证用户"""
        for user in self.users.values():
            if user.api_key == api_key:
                user.last_active = time.time()
                return user
        return None

    def check_permission(self, user: User, permission: Permission) -> bool:
        """检查权限"""
        for role_name in user.roles:
            if role_name in self.roles:
                role = self.roles[role_name]
                if permission in role.permissions:
                    return True
        return False

    def get_user_risk_level(self, user: User) -> RiskLevel:
        """获取用户风险等级"""
        max_risk = RiskLevel.LOW
        for role_name in user.roles:
            if role_name in self.roles:
                role = self.roles[role_name]
                if role.risk_level.value > max_risk.value:
                    max_risk = role.risk_level
        return max_risk

    def _log_audit(self, action: str, username: str, details: Dict):
        """记录审计日志"""
        log_entry = {
            "timestamp": time.time(),
            "action": action,
            "username": username,
            "details": details
        }
        self.audit_log.append(log_entry)

# 全局安全管理器实例
security_manager = SecurityManager()
```

#### 2. 安全工具包装器

```python
# 🛡️ 安全工具包装器
class SecureToolWrapper(BaseTool):
    """安全工具包装器"""

    def __init__(self, wrapped_tool: BaseTool, required_permission: Permission,
                 risk_level: RiskLevel = RiskLevel.MEDIUM):
        super().__init__()
        self.wrapped_tool = wrapped_tool
        self.required_permission = required_permission
        self.risk_level = risk_level
        self.name = f"Secure_{wrapped_tool.name}"
        self.description = f"安全包装的{wrapped_tool.description}"
        self.args_schema = wrapped_tool.args_schema

    def _run(self, *args, **kwargs) -> str:
        """安全执行工具"""
        # 获取当前用户（这里简化处理，实际应该从上下文获取）
        api_key = kwargs.pop('api_key', None)
        if not api_key:
            return "错误: 需要提供API密钥"

        user = security_manager.authenticate(api_key)
        if not user:
            return "错误: 身份认证失败"

        # 检查权限
        if not security_manager.check_permission(user, self.required_permission):
            security_manager._log_audit("PERMISSION_DENIED", user.username, {
                "tool": self.wrapped_tool.name,
                "permission": self.required_permission.value
            })
            return f"错误: 权限不足，需要 {self.required_permission.value} 权限"

        # 风险评估
        user_risk = security_manager.get_user_risk_level(user)
        if self.risk_level.value > user_risk.value:
            security_manager._log_audit("RISK_BLOCKED", user.username, {
                "tool": self.wrapped_tool.name,
                "required_risk": self.risk_level.value,
                "user_risk": user_risk.value
            })
            return f"错误: 风险等级不足，需要 {self.risk_level.name} 等级"

        # 记录工具使用
        security_manager._log_audit("TOOL_USAGE", user.username, {
            "tool": self.wrapped_tool.name,
            "args": str(args)[:200],  # 限制日志长度
            "kwargs": str(kwargs)[:200]
        })

        try:
            # 执行原始工具
            result = self.wrapped_tool._run(*args, **kwargs)

            security_manager._log_audit("TOOL_SUCCESS", user.username, {
                "tool": self.wrapped_tool.name,
                "result_length": len(str(result))
            })

            return result

        except Exception as e:
            security_manager._log_audit("TOOL_ERROR", user.username, {
                "tool": self.wrapped_tool.name,
                "error": str(e)
            })
            return f"工具执行错误: {str(e)}"

# 创建安全工具
def create_secure_tool(tool: BaseTool, permission: Permission,
                      risk_level: RiskLevel = RiskLevel.MEDIUM) -> SecureToolWrapper:
    """创建安全工具"""
    return SecureToolWrapper(tool, permission, risk_level)

# 使用示例
calculator_tool = AdvancedCalculatorTool()
secure_calculator = create_secure_tool(
    calculator_tool,
    Permission.EXECUTE_CODE,
    RiskLevel.MEDIUM
)

text_processor = TextProcessorTool()
secure_text_processor = create_secure_tool(
    text_processor,
    Permission.READ_FILE,
    RiskLevel.LOW
)

# 创建用户
admin_key = security_manager.create_user("admin", ["admin"])
user_key = security_manager.create_user("john", ["user"])
guest_key = security_manager.create_user("guest", ["guest"])

# 安全Agent
secure_agent = Agent(
    role="安全计算专家",
    goal="在安全环境中执行计算任务",
    backstory="专业的安全计算专家，严格遵守安全规范...",
    tools=[secure_calculator, secure_text_processor],
    verbose=True
)
```

---

## 5.6 工具性能监控📊

### 🎮 游戏化理解：性能仪表盘

工具性能监控就像游戏中的性能仪表盘：

- **⚡ 速度表**：工具执行时间监控
- **💾 内存表**：资源使用情况监控
- **📊 成功率表**：工具执行成功率统计
- **🔥 热度表**：工具使用频率分析

### 📊 性能监控架构

```mermaid
graph TD
    A[性能监控系统] --> B[📊 指标收集]
    A --> C[📈 数据分析]
    A --> D[⚠️ 告警系统]
    A --> E[📋 报告生成]

    B --> B1[执行时间]
    B --> B2[内存使用]
    B --> B3[成功率]
    B --> B4[错误率]
    B --> B5[并发数]

    C --> C1[趋势分析]
    C --> C2[异常检测]
    C --> C3[性能基线]
    C --> C4[瓶颈识别]

    D --> D1[阈值告警]
    D --> D2[异常告警]
    D --> D3[容量告警]

    E --> E1[实时仪表盘]
    E --> E2[定期报告]
    E --> E3[性能优化建议]
```

### 📈 性能监控实现

#### 1. 性能指标收集器

```python
# 📊 性能指标收集器
import psutil
import threading
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import statistics

@dataclass
class PerformanceMetrics:
    """性能指标"""
    tool_name: str
    execution_time: float
    memory_usage: float
    cpu_usage: float
    success: bool
    error_message: Optional[str] = None
    timestamp: float = field(default_factory=time.time)
    input_size: int = 0
    output_size: int = 0

class PerformanceCollector:
    """性能收集器"""

    def __init__(self, max_history: int = 1000):
        self.max_history = max_history
        self.metrics_history: Dict[str, deque] = defaultdict(lambda: deque(maxlen=max_history))
        self.real_time_stats: Dict[str, Dict] = defaultdict(dict)
        self._lock = threading.Lock()

    def record_metric(self, metric: PerformanceMetrics):
        """记录性能指标"""
        with self._lock:
            self.metrics_history[metric.tool_name].append(metric)
            self._update_real_time_stats(metric)

    def _update_real_time_stats(self, metric: PerformanceMetrics):
        """更新实时统计"""
        tool_name = metric.tool_name

        if tool_name not in self.real_time_stats:
            self.real_time_stats[tool_name] = {
                "total_calls": 0,
                "success_calls": 0,
                "total_time": 0,
                "avg_time": 0,
                "min_time": float('inf'),
                "max_time": 0,
                "avg_memory": 0,
                "error_rate": 0
            }

        stats = self.real_time_stats[tool_name]
        stats["total_calls"] += 1

        if metric.success:
            stats["success_calls"] += 1

        stats["total_time"] += metric.execution_time
        stats["avg_time"] = stats["total_time"] / stats["total_calls"]
        stats["min_time"] = min(stats["min_time"], metric.execution_time)
        stats["max_time"] = max(stats["max_time"], metric.execution_time)

        # 计算平均内存使用
        recent_metrics = list(self.metrics_history[tool_name])[-10:]  # 最近10次
        if recent_metrics:
            stats["avg_memory"] = statistics.mean([m.memory_usage for m in recent_metrics])

        stats["error_rate"] = 1 - (stats["success_calls"] / stats["total_calls"])

    def get_tool_stats(self, tool_name: str) -> Dict:
        """获取工具统计信息"""
        with self._lock:
            return self.real_time_stats.get(tool_name, {})

    def get_all_stats(self) -> Dict[str, Dict]:
        """获取所有工具统计信息"""
        with self._lock:
            return dict(self.real_time_stats)

    def get_performance_report(self, tool_name: Optional[str] = None) -> str:
        """生成性能报告"""
        if tool_name:
            stats = self.get_tool_stats(tool_name)
            if not stats:
                return f"工具 '{tool_name}' 没有性能数据"

            return self._format_tool_report(tool_name, stats)
        else:
            all_stats = self.get_all_stats()
            if not all_stats:
                return "没有性能数据"

            report = "=== 性能监控报告 ===\n\n"
            for tool_name, stats in all_stats.items():
                report += self._format_tool_report(tool_name, stats) + "\n"

            return report

    def _format_tool_report(self, tool_name: str, stats: Dict) -> str:
        """格式化工具报告"""
        return f"""
工具: {tool_name}
- 总调用次数: {stats.get('total_calls', 0)}
- 成功次数: {stats.get('success_calls', 0)}
- 成功率: {(1 - stats.get('error_rate', 0)) * 100:.1f}%
- 平均执行时间: {stats.get('avg_time', 0):.3f}秒
- 最快执行时间: {stats.get('min_time', 0):.3f}秒
- 最慢执行时间: {stats.get('max_time', 0):.3f}秒
- 平均内存使用: {stats.get('avg_memory', 0):.2f}MB
"""

# 全局性能收集器
performance_collector = PerformanceCollector()
```

#### 2. 性能监控装饰器

```python
# 🔍 性能监控装饰器
import functools
import tracemalloc

class PerformanceMonitorTool(BaseTool):
    """性能监控工具包装器"""

    def __init__(self, wrapped_tool: BaseTool, enable_memory_profiling: bool = True):
        super().__init__()
        self.wrapped_tool = wrapped_tool
        self.enable_memory_profiling = enable_memory_profiling
        self.name = f"Monitored_{wrapped_tool.name}"
        self.description = f"性能监控的{wrapped_tool.description}"
        self.args_schema = wrapped_tool.args_schema

    def _run(self, *args, **kwargs) -> str:
        """监控执行工具"""
        start_time = time.time()
        start_memory = 0

        # 开始内存监控
        if self.enable_memory_profiling:
            tracemalloc.start()
            process = psutil.Process()
            start_memory = process.memory_info().rss / 1024 / 1024  # MB

        success = False
        error_message = None
        result = None

        try:
            # 执行原始工具
            result = self.wrapped_tool._run(*args, **kwargs)
            success = True

        except Exception as e:
            error_message = str(e)
            result = f"工具执行失败: {error_message}"

        finally:
            # 计算性能指标
            execution_time = time.time() - start_time

            memory_usage = 0
            if self.enable_memory_profiling:
                try:
                    current_memory = process.memory_info().rss / 1024 / 1024
                    memory_usage = current_memory - start_memory
                    tracemalloc.stop()
                except:
                    memory_usage = 0

            # 计算输入输出大小
            input_size = len(str(args) + str(kwargs))
            output_size = len(str(result)) if result else 0

            # 记录性能指标
            metric = PerformanceMetrics(
                tool_name=self.wrapped_tool.name,
                execution_time=execution_time,
                memory_usage=memory_usage,
                cpu_usage=psutil.cpu_percent(),
                success=success,
                error_message=error_message,
                input_size=input_size,
                output_size=output_size
            )

            performance_collector.record_metric(metric)

        return result

def monitor_performance(tool: BaseTool, enable_memory_profiling: bool = True) -> PerformanceMonitorTool:
    """为工具添加性能监控"""
    return PerformanceMonitorTool(tool, enable_memory_profiling)

# 性能报告工具
class PerformanceReportTool(BaseTool):
    """性能报告工具"""
    name: str = "性能报告工具"
    description: str = "生成工具性能监控报告"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, tool_name: str = None) -> str:
        """生成性能报告"""
        return performance_collector.get_performance_report(tool_name)

# 使用示例
# 为现有工具添加性能监控
monitored_calculator = monitor_performance(AdvancedCalculatorTool())
monitored_text_processor = monitor_performance(TextProcessorTool())
performance_report_tool = PerformanceReportTool()

performance_agent = Agent(
    role="性能监控专家",
    goal="监控和分析工具性能，提供优化建议",
    backstory="专业的性能分析和优化专家...",
    tools=[monitored_calculator, monitored_text_processor, performance_report_tool],
    verbose=True
)
```

---

## 5.7 高级工具开发技巧🚀

### 🎮 游戏化理解：技能进阶系统

高级工具开发就像游戏中的技能进阶：

- **🌟 技能升级**：从基础工具到智能工具
- **🔮 技能融合**：多种技术的组合应用
- **⚡ 技能特化**：针对特定场景的深度优化
- **🎯 技能精通**：掌握工具开发的最佳实践

### 📊 高级技巧体系

```mermaid
graph TD
    A[高级工具开发技巧] --> B[🧠 智能化技巧]
    A --> C[⚡ 性能优化技巧]
    A --> D[🔧 扩展性技巧]
    A --> E[🛡️ 可靠性技巧]

    B --> B1[自适应参数调整]
    B --> B2[机器学习集成]
    B --> B3[上下文感知]
    B --> B4[智能缓存策略]

    C --> C1[异步并发处理]
    C --> C2[内存优化]
    C --> C3[计算优化]
    C --> C4[网络优化]

    D --> D1[插件化架构]
    D --> D2[配置驱动设计]
    D --> D3[版本兼容性]
    D --> D4[API设计原则]

    E --> E1[错误恢复机制]
    E --> E2[超时和重试]
    E --> E3[资源清理]
    E --> E4[状态一致性]
```

### 🧠 智能化工具开发

#### 1. 自适应工具

```python
# 🧠 自适应智能工具
from typing import Any, Dict, List, Tuple
import pickle
import os

class AdaptiveToolInput(BaseModel):
    """自适应工具输入"""
    data: Any = Field(description="输入数据")
    context: Dict[str, Any] = Field(description="上下文信息", default={})
    learning_mode: bool = Field(description="是否启用学习模式", default=True)

class AdaptiveProcessingTool(BaseTool):
    """自适应处理工具"""
    name: str = "自适应处理工具"
    description: str = "根据历史数据和上下文自动调整处理策略"
    args_schema: Type[BaseModel] = AdaptiveToolInput

    def __init__(self, model_path: str = "adaptive_model.pkl"):
        super().__init__()
        self.model_path = model_path
        self.performance_history = []
        self.strategy_weights = {
            "fast_processing": 0.3,
            "accurate_processing": 0.4,
            "balanced_processing": 0.3
        }
        self._load_model()

    def _load_model(self):
        """加载自适应模型"""
        if os.path.exists(self.model_path):
            try:
                with open(self.model_path, 'rb') as f:
                    saved_data = pickle.load(f)
                    self.strategy_weights = saved_data.get('weights', self.strategy_weights)
                    self.performance_history = saved_data.get('history', [])
            except Exception:
                pass

    def _save_model(self):
        """保存自适应模型"""
        try:
            with open(self.model_path, 'wb') as f:
                pickle.dump({
                    'weights': self.strategy_weights,
                    'history': self.performance_history[-100:]  # 只保存最近100条记录
                }, f)
        except Exception:
            pass

    def _select_strategy(self, data: Any, context: Dict[str, Any]) -> str:
        """选择处理策略"""
        # 分析数据特征
        data_size = len(str(data))
        complexity = self._estimate_complexity(data)

        # 分析上下文
        time_constraint = context.get('time_limit', 30)  # 默认30秒
        accuracy_requirement = context.get('accuracy_level', 'medium')

        # 计算策略得分
        scores = {}

        # 快速处理策略
        scores['fast_processing'] = (
            self.strategy_weights['fast_processing'] *
            (1.0 if time_constraint < 10 else 0.5) *
            (1.0 if data_size < 1000 else 0.3)
        )

        # 精确处理策略
        scores['accurate_processing'] = (
            self.strategy_weights['accurate_processing'] *
            (1.0 if accuracy_requirement == 'high' else 0.6) *
            (1.0 if complexity > 0.7 else 0.4)
        )

        # 平衡处理策略
        scores['balanced_processing'] = (
            self.strategy_weights['balanced_processing'] *
            (0.8 if accuracy_requirement == 'medium' else 0.5) *
            (0.8 if 10 <= time_constraint <= 60 else 0.4)
        )

        # 选择得分最高的策略
        return max(scores, key=scores.get)

    def _estimate_complexity(self, data: Any) -> float:
        """估算数据复杂度"""
        if isinstance(data, str):
            # 文本复杂度：基于长度和特殊字符
            length_factor = min(len(data) / 1000, 1.0)
            special_chars = sum(1 for c in data if not c.isalnum() and not c.isspace())
            special_factor = min(special_chars / len(data), 0.5) if data else 0
            return length_factor * 0.7 + special_factor * 0.3
        elif isinstance(data, (list, dict)):
            # 结构化数据复杂度
            return min(len(str(data)) / 5000, 1.0)
        else:
            return 0.5  # 默认中等复杂度

    def _process_fast(self, data: Any) -> str:
        """快速处理策略"""
        # 简化处理逻辑
        return f"快速处理结果: {str(data)[:100]}..."

    def _process_accurate(self, data: Any) -> str:
        """精确处理策略"""
        # 详细处理逻辑
        time.sleep(0.5)  # 模拟复杂计算
        return f"精确处理结果: 详细分析了 {len(str(data))} 字符的数据"

    def _process_balanced(self, data: Any) -> str:
        """平衡处理策略"""
        # 平衡处理逻辑
        time.sleep(0.2)  # 模拟中等复杂度计算
        return f"平衡处理结果: 高效分析了数据，复杂度评估为中等"

    def _update_strategy_weights(self, strategy: str, performance: float):
        """更新策略权重"""
        # 简单的强化学习更新
        learning_rate = 0.1
        reward = performance  # 性能作为奖励

        # 更新选中策略的权重
        self.strategy_weights[strategy] += learning_rate * reward

        # 归一化权重
        total_weight = sum(self.strategy_weights.values())
        for key in self.strategy_weights:
            self.strategy_weights[key] /= total_weight

    def _run(self, data: Any, context: Dict[str, Any] = None, learning_mode: bool = True) -> str:
        """执行自适应处理"""
        if context is None:
            context = {}

        start_time = time.time()

        # 选择处理策略
        strategy = self._select_strategy(data, context)

        # 执行处理
        try:
            if strategy == "fast_processing":
                result = self._process_fast(data)
            elif strategy == "accurate_processing":
                result = self._process_accurate(data)
            else:
                result = self._process_balanced(data)

            # 计算性能指标
            execution_time = time.time() - start_time
            performance = 1.0 / (1.0 + execution_time)  # 时间越短性能越好

            # 学习模式下更新策略
            if learning_mode:
                self.performance_history.append({
                    'strategy': strategy,
                    'performance': performance,
                    'execution_time': execution_time,
                    'data_size': len(str(data))
                })

                self._update_strategy_weights(strategy, performance)
                self._save_model()

            return f"策略: {strategy}\n结果: {result}\n执行时间: {execution_time:.3f}秒"

        except Exception as e:
            return f"处理失败: {str(e)}"

# 使用示例
adaptive_tool = AdaptiveProcessingTool()

adaptive_agent = Agent(
    role="自适应处理专家",
    goal="根据数据特征和上下文自动选择最优处理策略",
    backstory="具有机器学习能力的智能处理专家...",
    tools=[adaptive_tool],
    verbose=True
)
```

#### 2. 上下文感知工具

```python
# 🔮 上下文感知工具
class ContextAwareInput(BaseModel):
    """上下文感知输入"""
    query: str = Field(description="查询内容")
    context_type: str = Field(description="上下文类型", default="general")
    previous_results: List[str] = Field(description="之前的结果", default=[])

class ContextAwareTool(BaseTool):
    """上下文感知工具"""
    name: str = "上下文感知工具"
    description: str = "根据上下文信息提供智能化的处理结果"
    args_schema: Type[BaseModel] = ContextAwareInput

    def __init__(self):
        super().__init__()
        self.context_memory = {}
        self.session_history = []

    def _analyze_context(self, query: str, context_type: str, previous_results: List[str]) -> Dict[str, Any]:
        """分析上下文"""
        context_info = {
            "query_intent": self._detect_intent(query),
            "context_type": context_type,
            "has_history": len(previous_results) > 0,
            "complexity_level": self._assess_complexity(query),
            "domain": self._detect_domain(query)
        }

        # 分析历史结果的模式
        if previous_results:
            context_info["result_pattern"] = self._analyze_result_pattern(previous_results)

        return context_info

    def _detect_intent(self, query: str) -> str:
        """检测查询意图"""
        query_lower = query.lower()

        if any(word in query_lower for word in ['计算', '算', '数学', '公式']):
            return "calculation"
        elif any(word in query_lower for word in ['分析', '统计', '数据']):
            return "analysis"
        elif any(word in query_lower for word in ['搜索', '查找', '寻找']):
            return "search"
        elif any(word in query_lower for word in ['创建', '生成', '制作']):
            return "creation"
        else:
            return "general"

    def _detect_domain(self, query: str) -> str:
        """检测领域"""
        query_lower = query.lower()

        if any(word in query_lower for word in ['金融', '投资', '股票', '财务']):
            return "finance"
        elif any(word in query_lower for word in ['技术', '编程', '代码', '开发']):
            return "technology"
        elif any(word in query_lower for word in ['医疗', '健康', '医学']):
            return "healthcare"
        elif any(word in query_lower for word in ['教育', '学习', '培训']):
            return "education"
        else:
            return "general"

    def _assess_complexity(self, query: str) -> str:
        """评估复杂度"""
        word_count = len(query.split())

        if word_count < 5:
            return "simple"
        elif word_count < 15:
            return "medium"
        else:
            return "complex"

    def _analyze_result_pattern(self, previous_results: List[str]) -> Dict[str, Any]:
        """分析结果模式"""
        if not previous_results:
            return {}

        # 分析结果长度趋势
        lengths = [len(result) for result in previous_results]
        avg_length = sum(lengths) / len(lengths)

        # 分析结果类型
        result_types = []
        for result in previous_results:
            if result.startswith("计算结果"):
                result_types.append("calculation")
            elif "分析" in result:
                result_types.append("analysis")
            else:
                result_types.append("general")

        return {
            "avg_length": avg_length,
            "result_types": result_types,
            "trend": "increasing" if lengths[-1] > lengths[0] else "decreasing"
        }

    def _generate_contextual_response(self, query: str, context_info: Dict[str, Any]) -> str:
        """生成上下文相关的响应"""
        intent = context_info["query_intent"]
        domain = context_info["domain"]
        complexity = context_info["complexity_level"]

        # 根据上下文调整响应策略
        if intent == "calculation":
            if complexity == "simple":
                return f"简单计算: {query} 的结果是..."
            else:
                return f"复杂计算分析: 对于 {query}，需要考虑多个因素..."

        elif intent == "analysis":
            if domain == "finance":
                return f"金融分析: 基于 {query} 的财务数据分析显示..."
            elif domain == "technology":
                return f"技术分析: 关于 {query} 的技术评估结果..."
            else:
                return f"数据分析: {query} 的分析结果..."

        elif intent == "search":
            return f"搜索结果: 关于 {query} 找到以下相关信息..."

        else:
            return f"基于上下文的智能回复: {query}"

    def _run(self, query: str, context_type: str = "general", previous_results: List[str] = None) -> str:
        """执行上下文感知处理"""
        if previous_results is None:
            previous_results = []

        # 分析上下文
        context_info = self._analyze_context(query, context_type, previous_results)

        # 生成响应
        response = self._generate_contextual_response(query, context_info)

        # 更新会话历史
        self.session_history.append({
            "query": query,
            "context_info": context_info,
            "response": response,
            "timestamp": time.time()
        })

        # 限制历史记录长度
        if len(self.session_history) > 50:
            self.session_history = self.session_history[-50:]

        return f"""
上下文分析:
- 查询意图: {context_info['query_intent']}
- 领域: {context_info['domain']}
- 复杂度: {context_info['complexity_level']}
- 有历史记录: {context_info['has_history']}

智能响应:
{response}
"""

# 使用示例
context_aware_tool = ContextAwareTool()

context_agent = Agent(
    role="上下文感知专家",
    goal="基于上下文信息提供智能化的个性化服务",
    backstory="具有强大上下文理解能力的智能助手...",
    tools=[context_aware_tool],
    verbose=True
)
```

---

## 5.8 实战案例分析🎪

### 🎮 游戏化理解：副本挑战

实战案例就像游戏中的副本挑战：

- **🏰 新手副本**：基础工具集成案例
- **⚔️ 进阶副本**：复杂工具链设计案例
- **🐉 专家副本**：企业级工具系统案例
- **👑 传说副本**：创新工具开发案例

### 📊 案例分析框架

```mermaid
graph TD
    A[实战案例分析] --> B[📋 需求分析]
    A --> C[🎯 解决方案设计]
    A --> D[🔧 实现过程]
    A --> E[📈 效果评估]
    A --> F[💡 经验总结]

    B --> B1[业务需求]
    B --> B2[技术需求]
    B --> B3[性能需求]
    B --> B4[安全需求]

    C --> C1[架构设计]
    C --> C2[工具选择]
    C --> C3[集成策略]
    C --> C4[优化方案]

    D --> D1[开发阶段]
    D --> D2[测试阶段]
    D --> D3[部署阶段]
    D --> D4[维护阶段]

    E --> E1[性能指标]
    E --> E2[用户反馈]
    E --> E3[业务价值]
    E --> E4[技术收益]
```

### 🏰 案例一：智能客服系统

#### 需求分析
构建一个智能客服系统，能够：
- 理解用户问题并提供准确回答
- 处理多种类型的查询（产品信息、技术支持、投诉处理）
- 与现有系统集成（CRM、知识库、工单系统）
- 提供多语言支持

#### 解决方案设计

```python
# 🤖 智能客服系统实现
class CustomerServiceInput(BaseModel):
    """客服输入模型"""
    user_message: str = Field(description="用户消息")
    user_id: str = Field(description="用户ID")
    session_id: str = Field(description="会话ID")
    language: str = Field(description="语言", default="zh")

class IntelligentCustomerServiceTool(BaseTool):
    """智能客服工具"""
    name: str = "智能客服系统"
    description: str = "提供智能客服服务，包括问题理解、知识检索、回答生成"
    args_schema: Type[BaseModel] = CustomerServiceInput

    def __init__(self):
        super().__init__()
        # 集成多个工具
        self.text_processor = TextProcessorTool()
        self.search_tool = SerperDevTool()
        self.context_tool = ContextAwareTool()

        # 知识库
        self.knowledge_base = {
            "产品信息": {
                "价格": "我们的产品价格从99元到999元不等，具体价格请查看官网。",
                "功能": "我们的产品具有AI智能分析、数据可视化、自动报告等功能。",
                "使用方法": "产品使用非常简单，只需三步：注册账号、导入数据、生成报告。"
            },
            "技术支持": {
                "安装问题": "如果遇到安装问题，请确保系统满足最低要求，并以管理员权限运行。",
                "使用问题": "使用过程中如有问题，可以查看帮助文档或联系技术支持。",
                "故障排除": "常见故障可以通过重启应用、清除缓存、更新版本来解决。"
            },
            "投诉处理": {
                "服务投诉": "我们非常重视您的反馈，会在24小时内安排专人处理您的投诉。",
                "产品投诉": "对于产品问题，我们提供7天无理由退换货服务。",
                "其他投诉": "其他问题请详细描述，我们会认真对待并及时回复。"
            }
        }

        # 会话历史
        self.session_history = {}

    def _classify_intent(self, message: str) -> Tuple[str, str]:
        """分类用户意图"""
        message_lower = message.lower()

        # 产品相关
        if any(word in message_lower for word in ['价格', '多少钱', '费用', '收费']):
            return "产品信息", "价格"
        elif any(word in message_lower for word in ['功能', '特点', '能做什么']):
            return "产品信息", "功能"
        elif any(word in message_lower for word in ['怎么用', '如何使用', '使用方法']):
            return "产品信息", "使用方法"

        # 技术支持
        elif any(word in message_lower for word in ['安装', '安装不了', '装不上']):
            return "技术支持", "安装问题"
        elif any(word in message_lower for word in ['不会用', '怎么操作', '使用问题']):
            return "技术支持", "使用问题"
        elif any(word in message_lower for word in ['故障', '错误', '不工作', '坏了']):
            return "技术支持", "故障排除"

        # 投诉处理
        elif any(word in message_lower for word in ['投诉', '不满意', '差评']):
            if any(word in message_lower for word in ['服务', '态度', '客服']):
                return "投诉处理", "服务投诉"
            elif any(word in message_lower for word in ['产品', '质量', '功能']):
                return "投诉处理", "产品投诉"
            else:
                return "投诉处理", "其他投诉"

        return "其他", "通用"

    def _get_knowledge_answer(self, category: str, subcategory: str) -> str:
        """从知识库获取答案"""
        if category in self.knowledge_base and subcategory in self.knowledge_base[category]:
            return self.knowledge_base[category][subcategory]
        return None

    def _generate_personalized_response(self, base_answer: str, user_id: str, context: Dict) -> str:
        """生成个性化回复"""
        # 根据用户历史和上下文个性化回复
        if user_id in self.session_history:
            history = self.session_history[user_id]
            if len(history) > 0:
                base_answer += f"\n\n根据您之前的咨询记录，我还想提醒您..."

        return base_answer

    def _escalate_to_human(self, message: str, user_id: str) -> str:
        """升级到人工客服"""
        return f"您的问题比较复杂，我已经为您转接到人工客服，工单号：CS{int(time.time())}"

    def _run(self, user_message: str, user_id: str, session_id: str, language: str = "zh") -> str:
        """处理客服请求"""
        try:
            # 初始化会话历史
            if user_id not in self.session_history:
                self.session_history[user_id] = []

            # 分类用户意图
            category, subcategory = self._classify_intent(user_message)

            # 从知识库获取答案
            knowledge_answer = self._get_knowledge_answer(category, subcategory)

            if knowledge_answer:
                # 生成个性化回复
                response = self._generate_personalized_response(
                    knowledge_answer, user_id, {"category": category}
                )
            else:
                # 使用上下文感知工具处理复杂问题
                context_response = self.context_tool._run(
                    user_message,
                    context_type="customer_service",
                    previous_results=[item["response"] for item in self.session_history[user_id][-3:]]
                )

                if "复杂" in context_response or "不确定" in context_response:
                    response = self._escalate_to_human(user_message, user_id)
                else:
                    response = f"基于智能分析：{context_response}"

            # 记录会话历史
            self.session_history[user_id].append({
                "message": user_message,
                "response": response,
                "category": category,
                "subcategory": subcategory,
                "timestamp": time.time()
            })

            # 限制历史记录长度
            if len(self.session_history[user_id]) > 20:
                self.session_history[user_id] = self.session_history[user_id][-20:]

            return f"""
🤖 智能客服回复：

分类：{category} - {subcategory}
回复：{response}

如果您还有其他问题，请随时告诉我！
"""

        except Exception as e:
            return f"客服系统暂时遇到问题，请稍后再试。错误：{str(e)}"

# 客服系统集成示例
customer_service_tool = IntelligentCustomerServiceTool()

customer_service_agent = Agent(
    role="智能客服专家",
    goal="提供高质量的客户服务，解决用户问题",
    backstory="经验丰富的客服专家，具备强大的问题解决能力...",
    tools=[customer_service_tool],
    verbose=True
)
```

### ⚔️ 案例二：数据分析工作流

#### 需求分析
构建一个自动化数据分析工作流，能够：
- 从多个数据源获取数据
- 自动清洗和预处理数据
- 执行统计分析和可视化
- 生成分析报告

```python
# 📊 数据分析工作流实现
class DataAnalysisWorkflow:
    """数据分析工作流"""

    def __init__(self):
        # 集成多个工具
        self.file_reader = FileReadTool()
        self.csv_search = CSVSearchTool("data/sample.csv")
        self.code_interpreter = CodeInterpreterTool()
        self.text_processor = TextProcessorTool()
        self.stateful_data = StatefulDataTool()

        # 创建工作流管道
        self.analysis_pipeline = ToolPipeline([
            self.file_reader,
            self.code_interpreter,
            self.text_processor
        ], name="数据分析管道")

    def create_comprehensive_analysis_agent(self) -> Agent:
        """创建综合分析Agent"""
        return Agent(
            role="数据分析专家",
            goal="执行全面的数据分析，从数据获取到报告生成",
            backstory="资深的数据科学家，擅长端到端的数据分析流程...",
            tools=[
                self.analysis_pipeline,
                self.csv_search,
                self.stateful_data,
                monitor_performance(self.code_interpreter)  # 添加性能监控
            ],
            verbose=True
        )

# 使用示例
workflow = DataAnalysisWorkflow()
analysis_agent = workflow.create_comprehensive_analysis_agent()
```

### 💡 经验总结和最佳实践

#### 🎯 工具开发最佳实践

1. **设计原则**
   - 单一职责：每个工具专注一个功能
   - 接口一致：统一的输入输出格式
   - 错误处理：优雅的错误处理和恢复
   - 性能优化：考虑缓存、异步、并发

2. **安全考虑**
   - 输入验证：严格验证所有输入参数
   - 权限控制：实现细粒度的权限管理
   - 审计日志：记录所有重要操作
   - 资源限制：防止资源滥用

3. **可维护性**
   - 代码规范：遵循编码标准和最佳实践
   - 文档完善：提供详细的API文档
   - 测试覆盖：编写全面的单元测试和集成测试
   - 版本管理：合理的版本控制策略

4. **扩展性**
   - 插件化：支持插件式扩展
   - 配置驱动：通过配置文件控制行为
   - 接口抽象：定义清晰的抽象接口
   - 向后兼容：保持API的向后兼容性

---

## 🎯 第5章总结

### 🏆 学习成果

通过本章学习，你已经掌握了：

✅ **工具生态系统**：深入了解CrewAI内置工具和第三方工具集成
✅ **自定义开发**：能够开发满足特定需求的自定义工具
✅ **工具链设计**：掌握工具链的设计模式和优化策略
✅ **安全管理**：实现工具的安全控制和权限管理
✅ **性能监控**：建立完善的工具性能监控体系
✅ **高级技巧**：掌握智能化、自适应的高级工具开发技巧
✅ **实战应用**：通过实际案例学会解决复杂的业务问题

### 🚀 进阶方向

1. **深度集成**：探索更多第三方服务和API的集成
2. **AI增强**：将机器学习能力集成到工具中
3. **云原生**：开发支持云原生架构的工具
4. **微服务**：将工具设计为微服务架构
5. **实时处理**：开发支持实时数据处理的工具

### 🎪 实践练习

1. **基础练习**：开发一个简单的数据转换工具
2. **进阶练习**：创建一个带缓存机制的API调用工具
3. **高级练习**：设计一个自适应的智能推荐工具
4. **综合练习**：构建一个完整的业务流程自动化工具链

### 📚 延伸阅读

- CrewAI Tools官方文档
- LangChain工具开发指南
- 微服务架构设计模式
- API设计最佳实践
- 性能监控和优化技术

---

**下一章预告**：第6章将深入探讨Flow工作流的高级应用，包括事件驱动、条件分支、状态管理等企业级功能。让我们继续这个精彩的CrewAI学习之旅！ 🚀
