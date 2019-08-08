from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
from tiny.core.device import device


class Draw(ImageDraw.ImageDraw):
    def __init__(self, device):
        self.image = Image.new(device.mode, device.size)
        self.device = device
        super(Draw, self).__init__(self.image, mode=self.device.mode)

        # self.text = ImageFont.truetype('fonts/text.ttf', 9)
        # self.caption_font = ImageFont.truetype('fonts/caption.ttf', 9)

    def update(self):
        self.device.display(self.image.convert(self.device.mode))
        self.rectangle(xy=(0, 0, self.device.size[0], self.device.size[1]), fill=0)


# Создание инстанса дравера
draw: Draw = Draw(device)
