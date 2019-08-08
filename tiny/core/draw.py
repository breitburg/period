from PIL import ImageDraw
from PIL import Image
from tiny.core.device import device
from tiny.core.fonts import text_font


class Draw(ImageDraw.ImageDraw):
    def __init__(self, device):
        self.image = Image.new(device.mode, device.size)
        self.device = device

        super(Draw, self).__init__(self.image, mode=self.device.mode)
        self.font = text_font

    def update(self):
        self.device.display(self.image.convert(self.device.mode))

    def cleanup(self):
        self.device.display(self.image.convert(self.device.mode))
        self.rectangle(xy=(0, 0, self.device.size[0], self.device.size[1]), fill=0)


# Создание инстанса дравера
draw = Draw(device)
