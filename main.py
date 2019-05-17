from core import *
from time import sleep
from random import randint

device = Device()

try:
    intager = 1
    while True:
        with Canvas(device) as draw:
            intager += 1
            if intager >= 500: intager = '1'
            draw.rectangle([
                randint(0, 64),
                randint(0, 128),
                randint(0, 64),
                randint(0, 128)
            ], fill=255)
except Exception as ex:
    with Canvas(device) as draw:
        draw.alert(text=str(ex), duration=5)
