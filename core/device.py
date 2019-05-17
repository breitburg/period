from luma.emulator.device import pygame


# from luma.oled.device import sh1106
# spi(device=0, port=0, bus_speed_hz=8000000, transfer_size=4096, gpio_DC=24, gpio_RST=25)

class Device(pygame):
    def __init__(self):
        super(Device, self).__init__(mode='1', scale=2)
        self.__brightness = 255

    def set_brightness(self, level: int) -> bool:
        assert level >= 0 and level <= 100
        self.__brightness = round(level * 2.55)
        return True

    def get_brightness(self) -> int:
        return round(self.__brightness / 2.55)
