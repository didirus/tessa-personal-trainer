import os
import random
import subprocess

from utils import logger


class Music():

    def __init__(self, cfg):
        self.cfg = cfg
        self.songs = self._get_songs()

    def _get_songs(self):
        songs = [os.path.join(d, song) for d, _, f in os.walk(self.cfg.music.dir()) for song in f if '.mp3' in song]
        return songs

    def play_song(self):
        song = random.choice(self.songs)
        logger.info(f"Playing song: '{song.split('/')[-1].split('.mp3')[0]}'")
        subprocess.Popen(["timeout", '{}s'.format(self.cfg.duration), "afplay", "-v", str(self.cfg.music.vol), song])
