
class Song():
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.copies = []
        
    def add_to_album(self, album):
        song_copy = Song_Copy(self, album)
        self.copies.append(song_copy)
        album.add_song(song_copy)
    
    def add_to_playlist(self, playlist):
        if len(self.copies) == 0:
           return
        else:
            song_copy = self.copies[0]
        playlist.add_song(song_copy)
        
        

class Song_Copy():
    def __init__(self, root_song, album):
        self.album = album
        self.root_song = root_song
        
class Album():
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.songs = []
    def add_song(self, song_copy):
        self.songs.append(song_copy)
        
class Artist():
    def __init__(self, *args):
        self.names = args
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)

class PlayList:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song_copy):
        self.songs.append(song_copy)
        
        
if __name__ == '__main__':
    
    marni = Artist(('Marni Nixon'))
    
    lovely_song = Song('Wouldn\'t be it lovely', marni)
    dance_song = Song('I could have danced all night', marni)
    
    album = Album('My Fair Lady Osts', marni)
    lovely_song.add_to_album(album)
    dance_song.add_to_album(album)
    
    playlist = PlayList('My favourite OSTs')
    lovely_song.add_to_album(album)
    lovely_song.add_to_playlist(album)
    