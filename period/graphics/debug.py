from period.core.draw import draw


def fps(fps):
    text = f'{fps}fps'

    size = draw.textsize(text=text)
    draw.rectangle(xy=(0, 0) + size, fill=False)
    draw.text(xy=(0, -2), text=text, fill=True)