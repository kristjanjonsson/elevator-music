import re
import os

song_pattern = re.compile('\w+.mp3')


def _get_songs(dir):
    files = os.listdir(dir)
    return (f for f in files if song_pattern.search(f))


class Playlist:
    """Class for handling the playlist logic.
    Current implementation handles only mp3."""

    def __init__(self):
        self.music_dir = 'music/'
        self.song_catalog = set(_get_songs(self.music_dir))
        self.songstack = list(self.song_catalog)

    def next_song(self):
        """Returns the next song to play and handles the logic."""

        # Add songs to playlist that have been added to the folder since last call.
        new_music = (song for song in _get_songs(self.music_dir) if song not in self.song_catalog)
        for song in new_music:
            self.songstack.append(song)
            self.song_catalog.add(song)

        # If playlist empty start all over again.
        if not self.songstack:
            self.songstack = list(self.song_catalog)

        song = self.songstack.pop()
        return os.path.join(self.music_dir, song)
