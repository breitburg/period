from PIL import ImageDraw
from luma.core.render import canvas


class AdvancedDraw(ImageDraw.ImageDraw):
    def __init__(self, image, device):
        super(AdvancedDraw, self).__init__(image, mode='1')
        self.device = device

        from PIL import ImageFont
        self.text_font = ImageFont.truetype('fonts/text.ttf', 9)
        self.caption_font = ImageFont.truetype('fonts/caption.ttf', 9)

    def alert(self, text='An error has occurred', font=None, icon='error', duration=5, progress_bar=True,
              move_stap=1.5):
        font = font if font else self.text_font
        from PIL import Image
        from time import time

        start_time = None
        pixels_step = round(self.device.size[0] / duration)
        elements_positions = 0 - self.textsize(text=text, font=font)[0]
        assert move_stap <= 10

        while True:
            with canvas(self.device) as draw:
                left_time = None
                in_animation = elements_positions < 10
                if in_animation: elements_positions += move_stap

                if not in_animation:
                    if not start_time: start_time = time()
                    left_time = start_time + duration - time()
                    if left_time <= 0: break

                if progress_bar and left_time:
                    draw.line([0,
                               self.device.size[1] - 1,
                               self.device.size[0] - round(left_time * pixels_step),
                               self.device.size[1] - 1], fill=255)
                    draw.bitmap((0, 0), Image.open('icons/arrow_right.png'), fill=255)

                draw.bitmap((elements_positions, 15), Image.open('icons/{icon}.png'.format(icon=icon)), fill=255)
                draw.text((elements_positions, 35), text=str(text), font=font, fill=255)
