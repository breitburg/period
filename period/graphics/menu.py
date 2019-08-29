from period.core.draw import draw
from period.core.util import delay
from period.graphics.statusbar import status_bar
from period.core.config import __configuration
from period.core.button import get_pressed, up, down, center

offset = __configuration['bar_height'] + 1
height = (draw.device.size[1] - offset) / 3


def menu(items):
    selected = 0
    in_animation = True
    animation_offset = 0
    animation_direction = 'up'

    while True:
        delay(0.05)
        display_items = [selected - 1, selected, selected + 1]

        if in_animation:
            if animation_offset < 2.5:
                animation_offset += 1
            else:
                animation_offset = 0
                in_animation = False

        draw.rectangle(xy=(
            0,
            offset + height - animation_offset if animation_direction == 'down' else animation_offset + offset + height,
            draw.device.size[0],
            offset + height * 2 - animation_offset if animation_direction == 'down' else animation_offset + offset + height * 2
        ), fill=True)

        for item in display_items :
            if item < 0 or item > len(items) - 1 : continue
            draw.text(xy=(
                2,
                (offset + (height * (display_items.index(item) + 1)) - height) + int((height - draw.textsize(text=items[item])[1]) / 2)
            ), text=items[item], fill=item != selected)

        buttons_pressed = get_pressed()
        if up in buttons_pressed :
            if selected > 0 : selected -= 1
            animation_direction = 'up'
            in_animation = True
        if down in buttons_pressed :
            if selected < len(items) - 1 : selected += 1
            animation_direction = 'down'
            in_animation = True
        if center in buttons_pressed :
            return selected

        status_bar()
        draw.device.apply_actions()
        draw.clear()
