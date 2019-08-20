from period.core.draw import draw
from time import sleep


def alert(text='Hello, world!', animation_offset=3, scrolling_speed=3, sleep_time=2):
    # Entry filling animation
    for height in range(round(draw.device.size[1] / scrolling_speed)):
        offset = draw.device.size[1] - height * scrolling_speed  # Calculating offsets
        draw.rectangle(xy=(0, draw.device.size[1], draw.device.size[0], offset), fill=True)  # Drawing rectangle

        # Drawing smooth transitions
        for row in range(2, 4):
            for point in range(draw.device.size[0]):
                if point % row == 0: continue
                draw.point(xy=(point, offset + row - 2), fill=False)  # Filling black point

        draw.apply()  # Applying

    # Splitting tokens
    tokens = text.split()

    text_size = draw.textsize(text=text)  # Getting text size with default fonts
    xy = (10, round((draw.device.size[1] - text_size[1]) / 2))  # Calculating middle center of the screen

    for token in tokens:  # Foreach tokens
        for height in range(animation_offset):  # Foreach animation for each token
            draw.rectangle(xy=(0, 0, draw.device.size[0], draw.device.size[1]), fill=True)  # Drawing filled rectangle
            display_text = ' '.join(tokens[:tokens.index(token)])  # Join all tokens to get display string
            offset = draw.textsize(text=f'{display_text} ')[0]  # Calculating offsets for text

            draw.text(xy=xy, text=display_text, fill=False)  # Drawing already animated text

            # Drawing new token with specified height
            draw.text(xy=((xy[0] + offset), xy[1] + (animation_offset - height) - 1), text=token, fill=False)
            draw.clear()  # Clearing screen and going to new cycle iteration

    # After all animations just relax and sleep for a sleep_time
    sleep(sleep_time)
