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
            'Goede middag!',
            'Hello there!'
        ]))

    def intro(self):
        self.say(random.choice([
            "It's me: Tessa, your personal trainer."
        ]))

    def explanations(self):
        self.say(random.choice([
            f"Today, we'll do {self.cfg.max_times} exercises.",
            f"I have {self.cfg.max_times} exercises in store for you today.",
        ]))

    def startlines(self):
        self.say(random.choice([
            f'Allright ladies, in {self.cfg.warn_before} seconds, we will plank for {self.cfg.duration} seconds!',

            f"In {self.cfg.warn_before} seconds, let's find a piece of wall, and do {self.cfg.duration} seconds "
            f"of wall sitting",

            f'In {self.cfg.warn_before} seconds, we will do {self.cfg.duration} seconds of shoulder and '
            f'arm stretching',

            f'Yes, in {self.cfg.warn_before} seconds, face the ground, and give me a strong plank for '
            f'{self.cfg.duration} seconds!',

            f"Get ready. In {self.cfg.warn_before} seconds, we are doing deep squats for {self.cfg.duration} seconds.",

            f"{self.cfg.warn_before} seconds left before we will stand up, close our eyes, and roll your neck around in your shoulders. "

        ]))

    def give_option(self):
        self.say(random.choice([
            "Do you have time right now? Yes or No?",
            "Are you up for it? Yes or No?",

        ]))

    def delay(self):
        self.say(random.choice([
            "No worries, I will postpone it.",
            "That's okay.",
            "I won't take it personally.",
            "Lazy you."
        ]))

    def no_delay(self):
        self.say(random.choice([
            "Great.",
            "That's the spirit.",
            "Allrighty then.",
            "You go girl!"
        ]))

    def next_exercise(self, pause):
        next_exercise = datetime.now() + timedelta(minutes=pause)
        self.say(random.choice([
            f"Next exercise starts at {int(next_exercise.strftime('%M'))} past "
            f"{int(next_exercise.strftime('%H')) if int(next_exercise.strftime('%H')) < 12 else int(next_exercise.strftime('%H')) - 12} "
            f"(in {int(pause)} minute{'s' if pause != 1 else ''})...",
        ]))

    def motivation(self):
        self.say(random.choice([
            'GO GO GO GO GO!',
            'I cannot believe my eyes!',
            'Well done guys, keep it up!',
            'Come on, my mother even does a better job!',
        ]))

    def almost_done(self):
        self.say(random.choice([
            '5 seconds left. Almost done',
            '5 seconds left. Come on, only a little bit more!',
            '5 seconds left. That is the spirit',
            '5 seconds left. You almost make me proud',
            '5 seconds left. Feel those muscles',
            '5 seconds left. Breathe in, breathe out',
            '5 seconds left. Enjoy the feeling in your nerves',

        ]))

    def well_done(self):
        self.say(random.choice([
            'Nice. Thank you for your contribution.',
            'Great job! Cardiovascular exercise helps create new brain cells.',
            'Awesome.'
            'Proud is what I am.'
        ]))

    def closing(self):
        self.say(random.choice([
            "You're done! That was it for todays exercises. Tschusie tschusie.",

        ]))
