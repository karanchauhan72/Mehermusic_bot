from pyrogram import Client
from MeherMusic.config import API_ID, API_HASH, BOT_TOKEN


class MeherMusicBot(Client):
    def __init__(self):
        super().__init__(
            "MeherMusic",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
        )


app = MeherMusicBot()
