from PIL import ImageDraw
from luma.core.render import canvas


class AdvancedDraw(ImageDraw.ImageDraw):
    def __init__(self, image):
        super(AdvancedDraw, self).__init__(image, mode='1')

    def alert(self, text='Welcome', icon='error', duration=5):
        from PIL import ImageFont, Image
        from time import time

        text_font = ImageFont.truetype('fonts/text.ttf', 9)

        start_time = time()
        while True:
            if time() > start_time + duration: return

            self.bitmap((10, 10), Image.open('icons/{icon}.png'.format(icon=icon)), fill=255)
            self.text((10, 34), text=str(text), font=text_font, fill=255)


class Canvas(canvas):
    def __init__(self, device):
        super(Canvas, self).__init__(device=device)

    def __enter__(self):
        self.draw = AdvancedDraw(self.image)
        return self.draw
