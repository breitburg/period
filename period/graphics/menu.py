from period.core.draw import draw
from period.core.util import delay
from period.graphics.statusbar import status_bar
from period.core.config import __configuration


def menu(items):
    selected = 0

    # TODO: Implement menu

    while True:
        status_bar()
        draw.rectangle(xy=(0, __configuration['bar_height'] + 1, draw.device.size[0], (draw.device.size[1] + 1 - __configuration['bar_height'])), fill=True)
        draw.device.apply_actions()
        draw.clear()