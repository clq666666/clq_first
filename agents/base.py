class BaseAgent:
    def __init__(self, role: str):
        self.role = role
    
    async def process(self, input_data: str):
        raise NotImplementedError
