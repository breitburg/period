from core import *
from time import sleep

device = Device()
progress = 0

while True:
    with Canvas(device) as draw:
        progress = progress + 1 if progress < 100 else 0
        draw.progress_bar(text=f'{progress}%', value=progress)
        sleep(progress / 500)
