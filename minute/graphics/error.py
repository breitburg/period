from minute.core.draw import draw
from minute.core.fonts import icons
from time import sleep
from textwrap import wrap


def error(exception):
    exception_range = 1
    draw.text(xy=(10, 10), text='\uf071 ' * exception_range, fill=True, font=icons)
    draw.text(xy=(10 + exception_range * 11, 10), text=type(exception).__name__, fill=True)

    text = wrap(text=exception.args[0], width=25)
    draw.text(xy=(10, 26), text='\n'.join(text), fill=True)

    draw.apply()
    sleep(5)
