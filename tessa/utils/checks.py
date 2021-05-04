import subprocess


def in_call():
    data = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.read().splitlines()
    for i in data:
        line = i.decode("utf-8").lower()
        if 'zoom' in line and line.split(' ')[-2] == '-key' and line.split(' ')[-1] != 'rpc':
            return True
