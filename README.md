# Tessa, your personal trainer
If you are spending a lot of time on your computer, either home or in an office, Tessa helps you do small exercises to relax your muscles. 

NOTE: only compatible for Mac user for now.

## Author
Diede Rusticus (diede.rusticus@gmail.com)

## How to use

1. Install requirements (optionally: inside a virtual environment).

    ```
    virtualenv venv  # optional
    source venv/bin/activate  # optional
    pip install -r requirements.txt
    ```
2. Adjust the `config.yaml` file to your needs. For more information about the options, run the command `python tessa/main.py --help`.

    ```
    # config.yaml
    
    max_times: 5
    warn_before: 30  # seconds
    duration_exercise: 60  # seconds
    duration_breath: 120  # seconds
    music:
    #  dir: /path/to/your/music/directory
      vol: 0.17
    finished_work_at: 19  # o'clock
    min_pause: 30  # minutes
    max_pause: 60  # minutes
    silent: no

   ```
3. Run Tessa.

    ```
   python tessa/main.py --cfg config.yaml
   ```
