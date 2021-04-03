import Audio as a


class FactoryClass:

    def create_object(audioFileType, audioFileMetadata):
        if audioFileType == 'Song':
            return a.Song(audioFileMetadata)
        elif audioFileType == 'PodCast':
            return a.PodCast(audioFileMetadata)
        elif audioFileType == 'AudioBook':
            return a.AudioBook(audioFileMetadata)


    def getClass(audioFileType):
        if audioFileType == 'Song':
            return a.Song
        elif audioFileType == 'PodCast':
            return a.PodCast
        elif audioFileType == 'AudioBook':
            return a.AudioBook

