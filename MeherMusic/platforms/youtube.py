import yt_dlp


class YouTube:
    def search(self, query):
        options = {
            "quiet": True,
            "skip_download": True,
            "extract_flat": True,
            "default_search": "ytsearch",
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            result = ydl.extract_info(query, download=False)

        entries = result.get("entries", [])

        if not entries:
            return None

        video = entries[0]

        return {
            "title": video.get("title"),
            "url": video.get("url"),
            "webpage_url": video.get("webpage_url"),
        }
