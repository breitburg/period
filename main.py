from core import *
from time import sleep
from random import randint

device = Device()

while True:
    with Canvas(device) as draw:
        for progress in range(0, 101):
            draw.progress_bar(text='Downloading data...', value=progress)
            sleep(randint(0, 10) / 50)
        draw.alert(text='Calculations done!', icon=icons.get('error'))