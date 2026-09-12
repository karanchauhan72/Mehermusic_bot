class MusicQueue:
    def __init__(self):
        self.queues = {}

    def add(self, chat_id, song):
        self.queues.setdefault(chat_id, []).append(song)

    def get(self, chat_id):
        return self.queues.get(chat_id, [])

    def next(self, chat_id):
        queue = self.queues.get(chat_id, [])

        if queue:
            return queue.pop(0)

        return None

    def clear(self, chat_id):
        self.queues.pop(chat_id, None)

    def is_empty(self, chat_id):
        return not self.queues.get(chat_id)
