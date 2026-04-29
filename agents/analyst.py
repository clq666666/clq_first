from .base import BaseAgent

class AnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Expert")

    async def analyze(self, data: dict):
        # 模拟长上下文逻辑推理
        return f"分析结果: 项目进度正常，但 {data['im']} 指出的文档问题可能导致联调延期。"
