from period.core.device import device
from period.core.draw import draw
from time import time


def delay(seconds):
    end_time = time() + seconds
    while time() <= end_time:
        draw.device.apply_actions()