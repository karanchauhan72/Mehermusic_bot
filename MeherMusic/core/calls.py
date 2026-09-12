from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream


class VoiceCallManager:
    def __init__(self, app):
        self.calls = PyTgCalls(app)

    async def start(self):
        await self.calls.start()

    async def play(self, chat_id, stream_url):
        await self.calls.play(
            chat_id,
            MediaStream(stream_url)
        )

    async def leave(self, chat_id):
        await self.calls.leave_call(chat_id)
