import asyncio
from agents.collector import CollectorAgent
from agents.analyst import AnalystAgent
from agents.strategist import StrategistAgent

async def main():
    print("--- 启动全栈数字员工系统 ---")

    # 1. 采集数据
    collector = CollectorAgent()
    raw_data = await collector.fetch_data()

    # 2. 分析风险
    analyst = AnalystAgent()
    analysis_report = await analyst.analyze(raw_data)

    # 3. 生成决策
    strategist = StrategistAgent()
    final_output = await strategist.generate_action(analysis_report)

    print("\n[最终执行方案]:")
    print(final_output)

if __name__ == "__main__":
    asyncio.run(main())
