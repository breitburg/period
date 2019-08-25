from period.core.draw import draw
from period.core.font import icons
from datetime import datetime


def status_bar(bar_height=8):
    for pixel in range(draw.device.size[0]):
        if pixel % 2 == 0: draw.point(xy=(pixel, bar_height), fill=True)

    draw.text(xy=(0, -2), text=f'{datetime.now().hour}:{datetime.now().minute}', fill=True)
    draw.icon(xy=(117, 0), icon=icons.get('battery-full'), size=8, fill=True)