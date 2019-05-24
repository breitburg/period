from PIL import ImageDraw
from luma.core.render import canvas
from drawing.question import QuestionButton


class AdvancedDraw(ImageDraw.ImageDraw):
    def __init__(self, image, device):
        super(AdvancedDraw, self).__init__(image, mode='1')
        self.device = device

        from PIL import ImageFont
        self.text_font = ImageFont.truetype('fonts/text.ttf', 9)
        self.caption_font = ImageFont.truetype('fonts/caption.ttf', 9)

    def alert(self, text='An error has occurred', font=None, icon='error', duration=5, progress_bar=True,
              move_step=1.5):
        font = font if font else self.text_font
        from PIL import Image
        from time import time

        start_time = None
        pixels_step = round(self.device.size[0] / duration)
        elements_positions = 0 - self.textsize(text=text, font=font)[0]
        assert move_step <= 10

        while True:
            with canvas(self.device) as draw:
                left_time = None
                in_animation = elements_positions < 10
                if in_animation: elements_positions += move_step

                if not in_animation:
                    if not start_time: start_time = time()
                    left_time = start_time + duration - time()
                    if left_time <= 0: break

                if progress_bar and left_time:
                    draw.line([0,
                               self.device.size[1] - 1,
                               self.device.size[0] - round(left_time * pixels_step),
                               self.device.size[1] - 1], fill=255)
                    # draw.bitmap((0, 0), Image.open('icons/arrow_right.png'), fill=255)

                draw.bitmap((elements_positions, 15), Image.open('icons/{icon}.png'.format(icon=icon)), fill=255)
                draw.text((elements_positions, 35), text=str(text), font=font, fill=255)

                # TODO: Check performance on real hardware
                for i in range(1, 4):
                    for pixel in range(0, self.device.size[1]):
                        if pixel % i != 0: continue
                        draw.point((self.device.size[0] - i, pixel), fill=0)

    def question(self, text='Apply changes?', font=None, icon='question', actions=[
        QuestionButton(text='Yes', icon='ok', ), QuestionButton(text='No', icon='close')
    ], auto_select=None, auto_duration=15) -> int:
        assert len(actions) == 2
        font = font if font else self.text_font

        from PIL import Image
        from time import time

        start_time = time()
        pixels_step = round(self.device.size[0] / auto_duration)

        if auto_select != None: line_position = self.device.size[1] - 1 if auto_select == 1 else 0

        while True:
            with canvas(self.device) as draw:
                left_time = start_time + auto_duration - time()
                if left_time <= 0 and auto_select != None: return auto_select

                if left_time and auto_select != None:
                    draw.line([0, line_position,
                               self.device.size[0] - round(left_time * pixels_step),
                               line_position], fill=255)

                for button in actions:
                    draw.bitmap((114, (actions.index(button) + 1) * 40 - 32),
                                Image.open('icons/small/{icon}.png'.format(icon=button.icon)), fill=255)

                # TODO: Return physical button press result
                draw.bitmap((10, 15), Image.open('icons/{icon}.png'.format(icon=icon)), fill=255)
                draw.text((10, 35), text=str(text), font=font, fill=255)

    def progress_bar(self, text='Waiting...', font=None, icon='arrow_down', max_value=100, value=50):
        # TODO: Add icon displaying

        font = font if font else self.text_font

        assert max_value < self.device.size[0]
        assert value <= max_value

        assert self.textsize(text=text, font=font)[0] <= self.device.size[0]

        with canvas(self.device) as draw:
            draw.text(xy=((self.device.size[0] - self.textsize(text=text, font=font)[0]) / 2, 18), text=text, fill=255,
                      font=font, anchor='center')

            notches = round((self.device.size[0] - max_value) / 2)
            draw.rectangle(xy=[notches, 35, self.device.size[0] - notches, 45], fill=0, outline=255)
            draw.rectangle(xy=[notches, 35, notches + value, 45], fill=255)
