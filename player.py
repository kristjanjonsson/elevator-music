from trollius import From, Return
import trollius as asyncio

from playlist import Playlist


class Player:

    def __init__(self):
        self.current_song_proc = None
        self.playlist_playing = False
        self.playlist = Playlist()

    def is_playing(self):
        """True if a song is playing."""
        return self.current_song_proc and not self.current_song_proc.returncode

    def stop(self):
        # We signal the playlist to stop playing
        # and press next to stop the current song.
        self.playlist_playing = False
        self.next()

    def next(self):
        # Stop the current song but keep the playlist playing.
        if self.is_playing():
            self.current_song_proc.terminate()

    @asyncio.coroutine
    def play_song(self, song):
        self.current_song_proc = yield From(asyncio.create_subprocess_exec(*['mpg321', song]))

    @asyncio.coroutine
    def play(self):
        """Plays the playlist forever!!!"""
        self.playlist_playing = True
        while self.playlist_playing:
            song = self.playlist.next_song()
            yield From(self.play_song(song))
            yield From(self.current_song_proc.wait())
