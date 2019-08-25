from period.core.draw import draw
from period.core.font import icons
from period.core.util import delay
from textwrap import wrap


def error(exception):
    exception_range = 1
    draw.icon(xy=(10, 10), icon=icons.get('exclamation-triangle'), size=9)
    draw.text(xy=(10 + exception_range * 11, 10), text=type(exception).__name__, fill=True)

    text = wrap(text=exception.args[0], width=25)
    draw.text(xy=(10, 26), text='\n'.join(text), fill=True)

    draw.apply()
    delay(5)
