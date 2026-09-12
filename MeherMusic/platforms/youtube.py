import yt_dlp


class YouTube:
    def get_stream(self, query: str):
        options = {
            "format": "bestaudio/best",
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "default_search": "ytsearch1",
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(query, download=False)

        if not info:
            return None

        if "entries" in info:
            entries = info.get("entries") or []

            if not entries:
                return None

            info = entries[0]

        return {
            "title": info.get("title", "Unknown"),
            "url": info.get("url"),
            "webpage_url": info.get("webpage_url"),
            "duration": info.get("duration", 0),
        }
