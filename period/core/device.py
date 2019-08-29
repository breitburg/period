from platform import processor
from time import time
from period.core.config import __configuration as config
is_emulator = processor() in ['x86_64', 'i386']
device = 0


class BaseDevice:
    last_buttons_pressed_time = time()
    __pressed_buttons = []

    def dim_contrast(self):
        print('Dimming')
        if config.get('auto_dim'):
            if not self.__pressed_buttons:
                if self.last_buttons_pressed_time + 2 <= self.start_time:
                    print('Setting dim')
                    self.contrast(80)
                    print('Set')
            else:
                self.last_buttons_pressed_time = self.start_time
                self.contrast(255)


if is_emulator:
    from os import environ
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
    from period.core.emulator import Emulator
    device = Emulator(mode='1', scale=8, frame_rate=16)
else:
    from luma.core.interface.serial import spi
    from period.core.hardware import Hardware
    serial = spi(device=0, port=0, bus_speed_hz=8000000, transfer_size=4096, gpio_DC=24, gpio_RST=25)
    device = Hardware(serial=serial)
