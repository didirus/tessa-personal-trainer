from jsonargparse import ArgumentParser, ActionPath, Path, ActionYesNo, ActionOperators, ActionConfigFile
from pathlib import Path as libPath
import os
import time
import easygui
from datetime import datetime
import random

from utils.speech import Speech
from utils.music import Music


def exercise_round():
    speech.give_option()
    if easygui.buttonbox("Time for an exercise right now?", 'Personal Trainer', ('Yes', 'No')) != 'Yes':
        return False
    else: speech.no_delay()
    speech.start_round()
    time.sleep(max(0, args.warn_before - 5))

    speech.count_down()

    music.play_song()

    now = time.time()
    time.sleep((args.duration_exercise - 5) / 2)
    speech.motivation()

    time.sleep((args.duration_exercise - 5 - (time.time() - now) - 2))
    speech.almost_done()

    time.sleep(args.duration_exercise - (time.time() - now))
    speech.well_done()

    return True


def random_pause():
    time.sleep(args.duration_breath)
    pause = 5 * round(random.randint(args.min_pause, args.max_pause)/5)
    if pause == 0:
        pause = 5
    speech.next_exercise(pause)
    time.sleep(pause * 60)


def main():

    speech.greetings()
    speech.intro()

    # Only during working hours
    if int(datetime.now().strftime("%H")) < args.finished_work_at - 1:
        speech.explanations()
        time.sleep(30)
        exercise_round()

        # Start exercise round
        for round in range(args.max_times):
            if int(datetime.now().strftime("%H")) > args.finished_work_at - 1:
                break

            random_pause()

            if not exercise_round():
                random_pause()
                exercise_round()

    speech.closing()


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('--cfg', action=ActionConfigFile)
    parser.add_argument('--lang', choices=['eng', 'nl'], nargs='?', default='nl', help='The language you want to hear.')
    parser.add_argument('--duration_breath', type=int, default=0, help='Number of seconds that Tessa takes a breath before announcing the next exercise.')
    parser.add_argument('--max_times', type=int, default=3, help='The number of exercises per day.')
    parser.add_argument('--warn_before', type=int, default=6, help='Seconds, before exercise starts, you get a warning.')
    parser.add_argument('--duration_exercise', type=int, action=ActionOperators(expr=('>', 15)), default=20, help='Seconds, duration of exercise.')
    parser.add_argument('--music.dir', action=ActionPath(mode='dr'), default=Path(os.path.join(str(libPath.home()), 'Music/iTunes/iTunes Media/Music'), mode='dr'), help='The root folder of your music files.')
    parser.add_argument('--music.vol', type=float, default=0.19, help='The volume of the music (exponential scale, where 0 is silent, 1 is normal, up to 255 for very loud.')
    parser.add_argument('--finished_work_at', type=int, default=19, help='When are you finished with work and want to stop exercises.')
    parser.add_argument('--min_pause', type=int, default=0, help='Minutes, minimum how long your break between exercises takes.')
    parser.add_argument('--max_pause', type=int, default=0, help='Minutes, maximum how long your break between exercises takes.')
    parser.add_argument('--silent', action=ActionYesNo, default=False, help='Wether you want to run Tessa in silent mode. Music is played anyway.')
    parser.add_argument('--skip_intro', action=ActionYesNo, default=True, help='If you want to restart Tessa and skip the intro.')
    args = parser.parse_args()

    speech = Speech(args)
    music = Music(args)
    main()