from period.core.draw import draw


def fps(fps):
    draw.text(xy=(0, -2), text=f'{fps}fps', fill=True)