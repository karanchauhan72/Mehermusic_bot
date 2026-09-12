class Playback:
    def __init__(self):
        self.current_song = None
        self.paused = False

    async def play(self, song):
        self.current_song = song
        self.paused = False

    async def pause(self):
        if self.current_song:
            self.paused = True

    async def resume(self):
        if self.current_song:
            self.paused = False

    async def stop(self):
        self.current_song = None
        self.paused = False

    def is_playing(self):
        return self.current_song is not None and not self.paused
