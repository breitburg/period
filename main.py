from core import *
from time import sleep
from random import randint

device = Device()

while True:
    with Canvas(device) as draw:
        draw.question()
