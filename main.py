from core import *
device = Device()

while True:
    with Canvas(device) as draw:
        from random import randint
        from time import sleep
        for progress in range(0, 101):
            draw.progress_bar(text=f'Downloading data... {progress}%', value=progress)
            sleep(randint(0, 10) / 100)