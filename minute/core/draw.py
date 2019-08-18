from PIL import ImageDraw
from PIL import Image
from minute.core.font import text_font
from minute.core.device import device


class Draw(ImageDraw.ImageDraw):
    def __init__(self, device):
        self.image = Image.new(device.mode, device.size)
        self.device = device

        super(Draw, self).__init__(self.image, mode=self.device.mode)
        self.font = text_font

    def apply(self):
        self.device.display(self.image.convert(self.device.mode))

    def clear(self):
        self.apply()
        self.rectangle(xy=(0, 0, self.device.size[0], self.device.size[1]), fill=0)


# Создание инстанса дравера
draw = Draw(device)
