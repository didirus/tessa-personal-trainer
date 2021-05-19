# Tessa, your personal trainer at your desk
If you are spending a lot of time on your computer, either home or in an office, Tessa helps you do small exercises to relax your muscles. 

<img src="tessa/files/superwoman.jpg" alt="superwoman" width="300"/>

## Author
Diede Rusticus (diede.rusticus@gmail.com)

## Prerequisites
- For Mac only 
- Make sure you have "Claire" and "Ava" downloaded as computer voices. 
  Go to `Settings > Accessibility > Spoken Content > System Voice > Customize` to download these voices. 

## How to use

1. Install requrements (optionally: inside a virtual environment).

    ```
    virtualenv venv  # optional
    source venv/bin/activate  # optional
    pip install -r requirements.txt
    ```
2. Adjust the `config.yaml` file to your needs. For more information about the options, run the command `python tessa/main.py --help`.

    ```
    # config.yaml
   
    lang: eng
    max_times: 10
    warn_before: 30  # seconds
    duration_exercise: 60  # seconds
    duration_breath: 120  # seconds
    music:
    #  dir: /path/to/your/music/directory
      vol: 0.18
    finished_work_at: 19  # o'clock
    min_pause: 30  # minutes
    max_pause: 60  # minutes
    silent: no
    skip_intro: no

   ```
   *Note: For the full experience, make sure you have access to some `mp3` files on your laptop and outcomment the `dir` line in the `config.yaml` file and set it to the path of your music directory. You can also use the parameter `--music.dir` for this. 

3. Run Tessa.

    ```
   python tessa/main.py --cfg config/config.yaml
   ```
