from PIL import ImageDraw, ImageFont
from luma.core.render import canvas


class Canvas(canvas):
    def __init__(self, device):
        super(Canvas, self).__init__(device=device)

    def __enter__(self):
        self.draw = AdvancedDraw(self.image, self.device)
        return self.draw


class AdvancedDraw(ImageDraw.ImageDraw):
    def __init__(self, image, device):
        super(AdvancedDraw, self).__init__(image, mode='1')
        self.device = device

    def alert(self, text='Произошла ошибка', font=ImageFont.truetype('fonts/text.ttf', 9), icon='error', duration=4):
        from PIL import Image
        from time import time

        start_time = time()
        pixels_step = round(127 / duration)

        while True:
            with canvas(self.device) as draw:
                remaining_time = start_time + duration - time()
                if remaining_time <= 0: break

                draw.bitmap((10, 15), Image.open('icons/{icon}.png'.format(icon=icon)), fill=255)
                draw.text((10, 35), text=str(text), font=font, fill=255)
                draw.line([0, 63, (127 - round(remaining_time * pixels_step)), 63], fill=255)
