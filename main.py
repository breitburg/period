from core import *
from time import sleep

device = Device()

while True:
    with Canvas(device) as draw:
        for i in range(0, 101):
            draw.progress_bar(text=f'{i}%', value=i)