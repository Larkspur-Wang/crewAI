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