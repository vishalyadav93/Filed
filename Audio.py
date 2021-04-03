class Audio:
    def __init__(self,meta):
        self.id_ = None
        self.duration = meta['duration']
        self.uploadTime = meta['uploadTime']


class Song(Audio):
    def __init__(self,meta):
        self.name = meta['name']
        super().__init__(meta)



class PodCast(Audio):
    def __init__(self, meta):
        self.name = meta['name']
        self.host = meta['host']
        self.participants = meta['participants']
        super().__init__(meta)


class AudioBook(Audio):
    def __init__(self,meta):
        self.title = meta['title']
        self.author = meta['author']
        self.narrator = meta['narrator']
        super().__init__(meta)


