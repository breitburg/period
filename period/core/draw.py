from PIL import ImageDraw, Image, ImageFont
from period.core.font import text_font
from period.core.device import device


class Draw(ImageDraw.ImageDraw):
    def __init__(self, device):
        self.image = Image.new(device.mode, device.size)
        self.device = device

        super(Draw, self).__init__(self.image, mode=self.device.mode)
        self.font = text_font

    def apply(self):
        self.device.display(self.image.convert(self.device.mode))

    def icon(self, xy, icon, fill=None, size=8):
        self.text(xy=xy, text=icon, font=ImageFont.truetype('fonts/icons.ttf', size), fill=fill)

    def rounded_rectangle(self, xy, corner_radius, fill=None, outline=None):
        upper_left_point = xy[0]
        bottom_right_point = xy[1]
        self.rectangle(
            [
                (upper_left_point[0], upper_left_point[1] + corner_radius),
                (bottom_right_point[0], bottom_right_point[1] - corner_radius)
            ],
            fill=fill,
            outline=outline
        )
        self.rectangle(
            [
                (upper_left_point[0] + corner_radius, upper_left_point[1]),
                (bottom_right_point[0] - corner_radius, bottom_right_point[1])
            ],
            fill=fill,
            outline=outline
        )
        self.pieslice(
            [upper_left_point, (upper_left_point[0] + corner_radius * 2, upper_left_point[1] + corner_radius * 2)],
            180,
            270,
            fill=fill,
            outline=outline
            )
        self.pieslice([(bottom_right_point[0] - corner_radius * 2, bottom_right_point[1] - corner_radius * 2),
                       bottom_right_point],
                      0,
                      90,
                      fill=fill,
                      outline=outline
                      )
        self.pieslice([(upper_left_point[0], bottom_right_point[1] - corner_radius * 2),
                       (upper_left_point[0] + corner_radius * 2, bottom_right_point[1])],
                      90,
                      180,
                      fill=fill,
                      outline=outline
                      )
        self.pieslice([(bottom_right_point[0] - corner_radius * 2, upper_left_point[1]),
                       (bottom_right_point[0], upper_left_point[1] + corner_radius * 2)],
                      270,
                      360,
                      fill=fill,
                      outline=outline
                      )

    def clear(self):
        self.apply()
        self.rectangle(xy=(0, 0, self.device.size[0], self.device.size[1]), fill=0)


# Создание инстанса дравера
draw = Draw(device)
