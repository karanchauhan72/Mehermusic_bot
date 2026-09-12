from pyrogram import filters
from MeherMusic.platforms.youtube import YouTube
from MeherMusic.plugins.queue import MusicQueue


youtube = YouTube()
music_queue = MusicQueue()


def register_music_handlers(app):

    @app.on_message(filters.command("play"))
    async def play_command(client, message):

        if len(message.command) < 2:
            await message.reply_text(
                "🎵 **Usage:**\n/play <song name>"
            )
            return

        query = " ".join(message.command[1:])

        await message.reply_text(
            f"🔎 Searching for: **{query}**..."
        )

        song = youtube.search(query)

        if not song:
            await message.reply_text(
                "❌ Song nahi mila."
            )
            return

        music_queue.add(message.chat.id, song)

        await message.reply_text(
            f"✅ **Added to queue**\n\n"
            f"🎵 **{song['title']}**"
        )
