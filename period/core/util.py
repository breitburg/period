from period.core.draw import draw
from time import time


def delay(seconds):
    end_time = time() + seconds
    buttons = list()

    while time() <= end_time:
        draw.device.apply_actions()

        for button in draw.device.get_pressed():
            if button not in buttons:
                buttons.append(button)

    draw.device.pressed_buttons = buttons
