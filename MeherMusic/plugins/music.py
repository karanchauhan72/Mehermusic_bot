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

        msg = await message.reply_text(
            f"🔎 Searching for **{query}**..."
        )

        try:
            song = youtube.get_stream(query)

            if not song or not song.get("url"):
                await msg.edit_text(
                    "❌ Song nahi mila."
                )
                return

            music_queue.add(message.chat.id, song)

            await msg.edit_text(
                f"🎵 **Added to queue**\n\n"
                f"**{song['title']}**\n\n"
                f"📋 Queue: `{len(music_queue.get(message.chat.id))}`"
            )

        except Exception as error:
            print(f"Play error: {error}")

            await msg.edit_text(
                "❌ Song process karte waqt error aa gaya."
            )
