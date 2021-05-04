import subprocess
import random

from utils import logger
from utils.checks import in_call


class Speech():

    def __init__(self, cfg):
        self.cfg = cfg
        self.task = None
        logger.info("Speech loaded.")

    def say(self, sentence):
        logger.info(f"Saying '{sentence[self.cfg.lang]}'.")
        if not self.cfg.silent and not in_call():
            subprocess.call(['afplay', './tessa/files/silence.wav'])
            subprocess.call(['say', '-v', f'{"Moira" if self.cfg.lang == "eng" else "Claire"}',  sentence[self.cfg.lang]])

    def greetings(self):
        if self.cfg.skip_intro:
            return
        self.say(random.choice([
            {"eng": "Good morning you.",
             "nl": "Goeie morgen jij."},
            {"eng": "Konnichiwa.",
             "nl": "Hoi. Hoi."},
            {"eng": "Hey, how is it going?",
             "nl": "Hoi, hoe gaat het met jou?"},
            {"eng": "Goodday",
             "nl": "Goede middag!"},
            {"eng": "Hello there!",
             "nl": "Hallo daar!"}
        ]))

    def intro(self):
        if self.cfg.skip_intro:
            return
        self.say(random.choice([
            {"eng": "It's me. Roisin. Your personal trainer.",
             "nl": "Ik ben het. Claire. Jouw persoonlijke trainer"}
        ]))

    def explanations(self):
        if self.cfg.skip_intro:
            return
        self.say(random.choice([
            {"eng": f"Today, we'll do {self.cfg.max_times} exercises.",
             "nl": f"Vandaag, doen we {self.cfg.max_times} oefeningen."},
            {"eng": f"I have {self.cfg.max_times} exercises in store for you today.",
             "nl": f"Ik heb {self.cfg.max_times} oefeningen voor jou vandaag."}
        ]))

    def start_round(self):
        self.task = random.choice([
            [{"eng": "wall-sit",
              "nl": "muur-zitten"},
             {
                 "eng": f"In {self.cfg.warn_before} seconds, let's find a piece of wall, "
                        f"and do {self.cfg.duration_exercise} "
                        f"seconds "f"of wall sitting",
                 "nl": f"In {self.cfg.warn_before} seconden, zoek een stukje muur voor {self.cfg.duration_exercise} "
                       f"seconden muur-zitten."}],

            [{"eng": "stretch the upperbody",
              "nl": "het bovenlichaam stretchen"},
             {
                 "eng": f"In {self.cfg.warn_before} seconds, we will do {self.cfg.duration_exercise} seconds of shoulder and "
                        f"arm stretching",
                 "nl": f"In {self.cfg.warn_before} seconden, doen we {self.cfg.duration_exercise} seconden schouder, arm en nek stretsjes."}],

            [{"eng": "plank", "nl": "planken"},
             {
                 "eng": f'Yes ladies, in {self.cfg.warn_before} seconds, face the ground, and give me a strong plank for '
                        f'{self.cfg.duration_exercise} seconds!',
                 "nl": f"Ja dames, in {self.cfg.warn_before} seconden, geef mij een stevige plank voor {self.cfg.duration_exercise} seconden!"}],

            [{"eng": 'squat', "nl": 'skwatten'},
             {
                 "eng": f"Get ready. In {self.cfg.warn_before} seconds, we are doing deep squats for "
                        f"{self.cfg.duration_exercise} seconds.",
                 "nl": f"Maak je klaar. In {self.cfg.warn_before} seconden, doen we diepe squats voor {self.cfg.duration_exercise} seconden."}],

            [{"eng": 'stretch the lowerbody', "nl": 'het onderlichaam stretsjen'},
             {
                 "eng": f"{self.cfg.warn_before} seconds left before we will stand up, and stretch those calfs, shins, and upperlegs.",
                 "nl": f"Nog {self.cfg.warn_before} seconden voordat we gaan staan, en been oefeningen gaan doen."}],

        ])
        self.say(self.task[1])
        return

    def count_down(self):
        self.say(random.choice([
            {"eng": f"Okay, let's {self.task[0][self.cfg.lang]}, in 5, 4, 3, 2, 1, go!",
             "nl": f"Oke, laten we {self.task[0][self.cfg.lang]}, in 5, 4, 3, 2, 1, go!"}]))

    def give_option(self):
        self.say(random.choice([
            {"eng": "Are you ready to move? Yes or No?", "nl": "Ben je er klaar voor? Ja of Nee."},
        ]))

    def no_delay(self):
        self.say(random.choice([
            {"eng": "Great.",
            "nl": "Goed."},
            {"eng": "That's the spirit.",
            "nl": "Dat is de spirit!"},
            {"eng": "Allrighty then.",
            "nl": "Joepie!"},
            {"eng": "You go girl!",
            "nl": "Geweldig!"},

        ]))

    def next_exercise(self, pause):
        self.say(random.choice([
            {"eng": f"Prepare for action, in {int(pause)} minute{'s' if pause != 1 else ''} ...",
            "nl": f"Bereid je voor, in {int(pause)} {'minuten' if pause != 1 else 'minuut'}",}
        ]))

    def motivation(self):
        self.say(random.choice([
            {"eng": 'GO GO GO GO GO!',
            "nl": "Ja ja ja ja!"},
            {"eng": 'I cannot believe my eyes!',
            "nl": "Ik weet niet wat ik zie!"},
            {"eng": 'Well done guys, keep it up!',
            "nl": "Goed zo meisjes, volhouden!"},
            {"eng": 'Come on, my mother even does a better job!',
            "nl": "Kom op, mijn moeder kan het beter!"},
        ]))

    def almost_done(self):
        self.say(random.choice([
            {"eng": '5 seconds left. Almost done',
            "nl": "5 seconden nog. Bijna klaar."},
            {"eng": '5 seconds left. Come on, only a little bit more!',
            "nl": "5 seconden nog. Kom op, nog een klein stukje!"},
            {"eng": '5 seconds left. That is the spirit',
            "nl": "5 seconden nog. Ziet er goed uit."},
            {"eng": '5 seconds left. You almost make me proud',
            "nl": "5 seconden nog. Ik ben bijna trots."},
            {"eng": '5 seconds left. Feel those muscles',
            "nl": "5 seconden nog. Voel die spieren"},
            {"eng": '5 seconds left. Breathe in, breathe out',
            "nl": "5 seconden nog. Adem in, adem uit."},
            {"eng": '5 seconds left. Enjoy the feeling in your nerves',
            "nl": "5 seconden nog. Geniet van de sensaties."},

        ]))

    def well_done(self):
        self.say(random.choice([
            {"eng": 'Nice. Thank you for your contribution.',
            "nl": "Super. Bedankt voor deze bijdrage."},
            {"eng": 'An mhaith!',
             "nl": 'Super.'},
            {"eng": 'Fine work.',
             "nl": 'Goedzo.'},
            {"eng": 'Great job! We just created new brain cells.',
            "nl": "Geweldig gedaan!"},
            {"eng": 'Awesome.',
            "nl": "Ongelovelijk goed."},
            {"eng": 'Proud. So proud..',
            "nl": "Trots. Zo trots."},
        ]))

    def closing(self):
        self.say(random.choice([
            {"eng": "You're done! Close your computer and do something relaxing. Toodels.",
            "nl": "Je bent klaar! Werk zit erop, sluit je computer en ga wat ontspannends doen! Doei doei."},

        ]))
