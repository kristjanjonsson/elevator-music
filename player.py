from trollius import From, Return
import trollius as asyncio

from playlist import Playlist


@asyncio.coroutine
def play_song(song):
    """Plays a song and returns the process that's playing it."""
    proc = yield From(asyncio.create_subprocess_exec(*['mpg321', song]))
    raise Return(proc)


@asyncio.coroutine
def play():
    """Plays the playlist forever!!!"""
    playlist = Playlist()
    while True:
        song = playlist.next_song()
        song_proc = yield From(play_song(song))

        yield From(song_proc.wait())

        # This is how we stopz it. We killz it.
        # yield From(song_proc.kill())


loop = asyncio.get_event_loop()
loop.run_until_complete(play())
