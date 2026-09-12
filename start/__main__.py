from pyrogram import Client, filters

from MeherMusic.config import API_ID, API_HASH, BOT_TOKEN
from MeherMusic.core.calls import VoiceCallManager
from MeherMusic.plugins.music import register_music_handlers


app = Client(
    "MeherMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

voice = VoiceCallManager(app)

register_music_handlers(app)


@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "🎵 **Meher Music Bot**\n\n"
        "Use `/play <song name>` to search music."
    )


async def main():
    await app.start()
    await voice.start()

    print("🎵 Meher Music started!")

    await app.idle()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
