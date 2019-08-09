from minute.core.draw import draw


def alert(text='An error has occurred', font=None, duration=5, progress_bar=True, move_step=1.5):
    font = font if font else draw.font
    from time import time

    start_time = None

    pixels_step = round(draw.device.size[0] / duration)
    elements_positions = 0 - draw.textsize(text=text, font=font)[0]

    assert move_step <= 10

    while True:
        left_time = None
        in_animation = elements_positions < 10
        if in_animation: elements_positions += move_step

        if not in_animation:
            if not start_time: start_time = time()
            left_time = start_time + duration - time()
            if left_time <= 0: break

        if progress_bar and left_time:
            draw.line([0,
                       draw.device.size[1] - 1,
                       draw.device.size[0] - round(left_time * pixels_step),
                       draw.device.size[1] - 1], fill=255)

        # draw.bitmap((elements_positions, 15), icon, fill=255)
        draw.text((elements_positions, 35), text=str(text), font=font, fill=255)

        for i in range(1, 4):
            for pixel in range(0, draw.device.size[1]):
                if pixel % i != 0: continue
                draw.point((draw.device.size[0] - i, pixel), fill=0)
        draw.cleanup()