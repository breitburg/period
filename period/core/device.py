from platform import processor
from PIL import ImageDraw
from period.core.config import __configuration as config
is_emulator = processor() in ['x86_64', 'i386']
device = 0


class BaseDevice:
    frame_rate = start_time = 0

    def show_fps(self, image):
        if not config['show_fps']: return
        # Adding frame rate to image
        text = f'{self.frame_rate} fps'

        draw = ImageDraw.Draw(image)
        size = draw.textsize(text=text)
        draw.rectangle(xy=(0, 0) + size, fill=False)
        draw.text(xy=(0, -2), text=text, fill=True)


if is_emulator:
    from os import environ
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
    from period.core.emulator import Emulator
    device = Emulator(mode='1', scale=2, frame_rate=20)
else:
    from luma.core.interface.serial import spi
    from period.core.hardware import Hardware
    serial = spi(device=0, port=0, bus_speed_hz=8000000, transfer_size=4096, gpio_DC=24, gpio_RST=25)
    device = Hardware(serial=serial)
