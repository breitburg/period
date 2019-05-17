from core import *
from time import sleep

while True:
    with Canvas(Device()) as draw:
        draw.alert()
        draw.line([0, 0, 127, 63], fill=255)
