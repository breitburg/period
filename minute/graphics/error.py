from minute.core.draw import draw
from minute.core.fonts import icons
from time import sleep
from textwrap import wrap


def error(exception):
    # TODO: Dynamic exception range
    exception_range = 2

    for offset in range(exception_range):
        draw.text(xy=(10 + offset * 12, 10), text='\uf071', fill=True, font=icons)

    draw.text(xy=(22 + offset * 12, 10), text=type(exception).__name__, fill=True)

    text = wrap(text=exception.args[0], width=30)
    draw.text(xy=(10, 30), text='\n'.join(text), fill=True)

    draw.apply()
    sleep(5)
