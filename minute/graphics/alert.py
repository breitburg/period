from minute.core.draw import draw


def alert(text='Hello, world!', animation_offset=3, xy=(10, 10)):
    tokens = text.split()
    for token in tokens:
        for height in range(animation_offset):
            draw.text(xy=xy, text=' '.join(tokens[:tokens.index(token)]), fill=True)

            offset = draw.textsize(text=' '.join(tokens[:tokens.index(token)]) + ' ')[0]
            draw.text(xy=(xy[0] + offset, xy[1] + (animation_offset - height) - 1), text=token, fill=True)
            draw.clear()