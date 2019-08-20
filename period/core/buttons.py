from period.core.device import device as __device__
from pygame import K_UP as __K_UP,\
    K_DOWN as __K_DOWN, K_RIGHT as __K_RIGHT,\
    K_LEFT as __K_LEFT, K_1 as __K_1, K_2 as __K_2,\
    K_3 as __K_3


class Button:
    def __init__(self, id):
        self.id = id


right = Button(1)
left = Button(2)
up = Button(3)
down = Button(4)
first = Button(5)
second = Button(6)
third = Button(7)

__buttons_keys = {
    __K_RIGHT: right,
    __K_LEFT: left,
    __K_UP: up,
    __K_DOWN: down,
    __K_1: first,
    __K_2: second,
    __K_3: third
}


def get_pressed():
    return [__buttons_keys[button] for button in __device__.get_pressed()]
