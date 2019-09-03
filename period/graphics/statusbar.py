from period.core.draw import draw
from period.core.font import icons
from period.core.config import __configuration
from datetime import datetime


def status_bar(bar_height=__configuration['bar_height'], title=None):
    for pixel in range(draw.device.size[0]):
        if pixel % 3 == 0: draw.point(xy=(pixel, bar_height), fill=True)

    time = datetime.now()
    title = f'{time.hour}:{time.minute}' if title is None else title
    horizontal_padding = (draw.device.size[0] - draw.textsize(text=title)[0]) / 2

    draw.text(xy=(horizontal_padding, (bar_height - draw.textsize(text=title)[1]) / 2 - 1), text=title, fill=True)

    # When real physical device will have a battery with the ability to
    # get current voltage, we will display small battery icon at the right side in status bar
    draw.icon(xy=(draw.device.size[0] - 11, (bar_height - 6) / 2 - 1), icon=icons.get('battery-full'), size=8, fill=True)
