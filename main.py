from core import *
from random import randint
from time import sleep

device = Device()

while True:
    with Canvas(device) as draw:
        draw.question(auto_select=True)
        sleep(5)