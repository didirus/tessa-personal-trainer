# Tessa, your personal trainer
If you are spending a lot of time on your computer, either home or in an office, Tessa helps you do small exercises to relax your muscles. 

NOTE: only compatible for Mac user for now.

## Author
Diede Rusticus(diede.rusticus@gmail.com)

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
    
    max_times: 3
    warn_before: 30
    duration: 60
    music:
      dir: <path_to_your_music_directory>
      vol: 0.17
    finished_work_at: 19
    min_pause: 45
    max_pause: 120
    silent: no
   ```
3. Run Tessa.

    ```
   python tessa/main.py --cfg config.yaml
   ```
