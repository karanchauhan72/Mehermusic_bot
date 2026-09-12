class VoiceCallManager:
    """Manages music playback voice calls."""

    def __init__(self):
        self.active_calls = {}

    async def join(self, chat_id):
        """Join a voice chat."""
        self.active_calls[chat_id] = True

    async def leave(self, chat_id):
        """Leave a voice chat."""
        self.active_calls.pop(chat_id, None)

    def is_active(self, chat_id):
        return self.active_calls.get(chat_id, False)
