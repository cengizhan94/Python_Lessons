class MusicPlayer:
    def play(self):
        raise NotImplementedError("Subclass must implement play method")

class Spotify(MusicPlayer):
    def play(self):
        return "Playing music on spotify"

class AppleMusic(MusicPlayer):
    def play(self):
        return "Playing music on apple music"
    
class YouTubeMusic(MusicPlayer):
    def play(self):
        return "Playing music on youtube music"

def play_music(music_player):
    print(music_player.play())
    
spotify = Spotify()
apple_music = AppleMusic()
youtube_music = YouTubeMusic()

play_music(spotify)
play_music(apple_music)
play_music(youtube_music)