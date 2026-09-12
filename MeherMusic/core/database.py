class Database:
    def __init__(self):
        self.connected = False

    async def connect(self):
        self.connected = True

    async def close(self):
        self.connected = False
