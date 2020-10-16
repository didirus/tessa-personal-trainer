import subprocess
import random
from datetime import datetime, timedelta

from utils import logger


class Speech():

    def __init__(self, cfg):
        self.cfg = cfg

    def say(self, sentence):
        logger.info(f"Saying '{sentence}'.")
        if not self.cfg.silent:
            subprocess.call(['say', sentence])

    def greetings(self):
        self.say(random.choice([
            'Good morning, you.',
            'Konnichiwa.',
            'Hey, how is it going?',
            'Goede middag!'
        ]))

    def intro(self):
        self.say(random.choice([
            "It's me: Tessa, your personal trainer."
        ]))

    def explanations(self):
        self.say(random.choice([
            f"Today, we'll do {self.cfg.max_times} exercises.",
        ]))

    def startlines(self):
        self.say(random.choice([
            f'Allright ladies, in {self.cfg.warn_before} seconds, we will plank for {self.cfg.duration} seconds!',
            f'In {self.cfg.warn_before} seconds, let us all find a piece of wall, and do {self.cfg.duration} seconds of wall sitting',
            f'In {self.cfg.warn_before} seconds, we will stand up and do {self.cfg.duration} seconds of shoulder and arm stretching',
            f'Yes yes yes, in {self.cfg.warn_before} seconds, face the ground, and give me a strong plank for {self.cfg.duration} seconds!',
        ]))

    def next_exercise(self, pause):
        next_exercise = datetime.now() + timedelta(minutes=pause)
        self.say(random.choice([
            f"Next exercise starts at {int(next_exercise.strftime('%M'))} past {int(next_exercise.strftime('%H')) if int(next_exercise.strftime('%H')) < 12 else int(next_exercise.strftime('%H')) - 12} (in {int(pause)} minute{'s' if pause != 1 else ''})...",
        ]))

    def motivation(self):
        self.say(random.choice([
            'GO GO GO GO GO!',
            'I cannot believe my eyes!',
            'Well done guys, keep it up!',
            'Come on, My mother can do a better job then you!',
        ]))

    def almost_done(self):
        self.say(random.choice([
            '5 seconds left. Almost done',
            '5 seconds left. Come on, only a little bit more!',
            '5 seconds left. That is the spirit',
            '5 seconds left. You almost make me proud',
            '5 seconds left. Feel those muscles',
            '5 seconds left. Breathe in, breathe out',

        ]))

    def well_done(self):
        self.say(random.choice([
            'Nice. Thank you for your contribution.',
            'Great job! Cardiovascular exercise helps create new brain cells.',
            'Awesome.'
        ]))

    def closing(self):
        self.say(random.choice([
            "You're done! That was it for todays exercises. Tschusie tschusie.",

        ]))