from period.core.device import device as __device__
from period.core.device import is_emulator
from pygame import K_UP as __K_UP,\
    K_DOWN as __K_DOWN, K_RIGHT as __K_RIGHT,\
    K_LEFT as __K_LEFT, K_1 as __K_1, K_2 as __K_2,\
    K_3 as __K_3, K_RCTRL as __K_RCTRL


class Button:
    def __init__(self, id):
        self.id = id


right = Button(1)
left = Button(2)
up = Button(3)
down = Button(4)
center = Button(5)
first = Button(6)
second = Button(7)
third = Button(8)

__buttons_keys__ = {
    __K_RIGHT: right,
    __K_LEFT: left,
    __K_UP: up,
    __K_DOWN: down,
    __K_RCTRL: center,
    __K_1: first,
    __K_2: second,
    __K_3: third
}


__hardware_keys__ = {
    6: up,
    19: down,
    5: left,
    26: right,
    13: center,
    21: first,
    20: second,
    16: third
}


def get_pressed():
    return [(__buttons_keys__ if is_emulator else __hardware_keys__)[button] for button in __device__.get_pressed()]