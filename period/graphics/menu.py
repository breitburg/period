from period.core.draw import draw
from period.core.util import delay
from period.graphics.statusbar import status_bar
from period.core.config import __configuration
from period.core.button import get_pressed, up, down, center

offset = __configuration['bar_height'] + 1
height = (draw.device.size[1] - offset) / 3


def menu(items):
    selected = 0

    while True:
        delay(0.1)
        display_items = [selected - 1, selected, selected + 1]
        draw.rectangle(xy=(
            0,
            offset + height,
            draw.device.size[0],
            offset + height * 2
        ), fill=True)

        for item in display_items :
            if item < 0 or item > len(items) - 1 : continue
            draw.text(xy=(
                0,
                offset + (height * (display_items.index(item) + 1)) - height
            ), text=items[item], fill=item != selected)

        buttons_pressed = get_pressed()
        if up in buttons_pressed :
            if selected > 0 : selected -= 1
        if down in buttons_pressed :
            if selected < len(items) - 1 : selected += 1
        if center in buttons_pressed :
            return selected

        status_bar()
        draw.device.apply_actions()
        draw.clear()
