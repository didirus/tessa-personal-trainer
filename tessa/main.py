from jsonargparse import ArgumentParser, ActionPath, Path, ActionYesNo, ActionOperators, ActionConfigFile
from pathlib import Path as libPath
import os
import time
import select
import sys
from datetime import datetime
import random

from utils.speech import Speech
from utils.music import Music


def exercise_round():



    speech.startlines()
    speech.give_option()
    if input("Do you have time right now? [y/n]: ").lower() != 'y':
        speech.delay()
        return False
    else: speech.no_delay()
    time.sleep(max(0, args.warn_before - 5))

    speech.say('In 5, 4, 3, 2, 1, Go!')

    music.play_song()

    now = time.time()
    time.sleep((args.duration - 5) / 2)
    speech.motivation()

    time.sleep((args.duration - 5 - (time.time() - now) - 2))
    speech.almost_done()

    time.sleep(args.duration - (time.time() - now))
    speech.well_done()

    return True

def main():

    speech.greetings()
    speech.intro()
    speech.explanations()

    exercise_round()

    for round in range(args.max_times):
        if int(datetime.now().strftime("%H")) > args.finished_work_at:
            break

        pause = random.randint(args.min_pause, args.max_pause)
        speech.next_exercise(pause)
        time.sleep(pause * 60)

        if not exercise_round():
            exercise_round()

    speech.closing()


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('--cfg', action=ActionConfigFile)
    parser.add_argument('--max_times', type=int, default=3, help='The number of exercises per day.')
    parser.add_argument('--warn_before', type=int, default=6, help='Seconds, before exercise starts, you get a warning.')
    parser.add_argument('--duration', type=int, action=ActionOperators(expr=('>', 15)), default=20, help='Seconds, duration of exercise.')
    parser.add_argument('--music.dir', action=ActionPath(mode='dr'), default=Path(os.path.join(str(libPath.home()), 'Music/iTunes/iTunes Media/Music'), mode='dr'), help='The root folder of your music files.')
    parser.add_argument('--music.vol', type=float, default=0.17, help='The volume of the music (exponential scale, where 0 is silent, 1 is normal, up to 255 for very loud.')
    parser.add_argument('--finished_work_at', type=int, default=19, help='When are you finished with work and want to stop exercises.')
    parser.add_argument('--min_pause', type=int, default=0, help='Minutes, minimum how long your break between exercises takes.')
    parser.add_argument('--max_pause', type=int, default=0, help='Minutes, maximum how long your break between exercises takes.')
    parser.add_argument('--silent', action=ActionYesNo, default=False, help='Wether you want to run Tessa in silent mode. Music is played anyway.')

    args = parser.parse_args()

    speech = Speech(args)
    music = Music(args)

    main()