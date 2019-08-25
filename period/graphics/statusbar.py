from period.core.draw import draw
from period.core.font import icons
from datetime import datetime


def status_bar(bar_height=9):
    for pixel in range(draw.device.size[0]):
        if pixel % 2 == 0: draw.point(xy=(pixel, bar_height), fill=True)

    time = datetime.now()
    text = f'{time.hour}:{time.minute}'
    padding = (draw.device.size[0] - draw.textsize(text=text)[0]) / 2

    draw.text(xy=(padding, -2), text=text, fill=True)

    # When real physical device will have a battery with the ability to
    # get current voltage, we will display small battery icon at the right side in status bar
    # draw.icon(xy=(117, 0), icon=icons.get('battery-full'), size=8, fill=True)
