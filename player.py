from trollius import From, Return
import trollius as asyncio

from playlist import Playlist


class Player:

    def __init__(self):
        self.current_song_proc = None
        self.playlist = Playlist()

    def is_playing(self):
        return self.current_song_proc and not self.current_song_proc.returncode

    def stop(self):
        if self.is_playing():
            self.current_song_proc.terminate()

    @asyncio.coroutine
    def play_song(self, song):
        self.current_song_proc = yield From(asyncio.create_subprocess_exec(*['mpg321', song]))

    @asyncio.coroutine
    def play(self):
        """Plays the playlist forever!!!"""
        while True:
            song = self.playlist.next_song()
            yield From(self.play_song(song))
            yield From(self.current_song_proc.wait())
