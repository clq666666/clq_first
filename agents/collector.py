from .base import BaseAgent

class CollectorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Information Collector")

    async def fetch_data(self):
        # 模拟从 Jira/Git 获取数据
        return {
            "jira": "Task-101: 登录模块开发 (进度 60%)",
            "git": "Recent commit: Fix bug in auth.py",
            "im": "飞书消息: 研发反馈 API 文档不全"
        }
