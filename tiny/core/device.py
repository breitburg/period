from platform import processor
is_emulator = processor() in ['x86_64', 'i386']

if is_emulator: from luma.emulator.device import pygame
else: from luma.oled.device import sh1106


class Device(pygame if is_emulator else sh1106):
    def __init__(self):
        if is_emulator:
            super(Device, self).__init__(mode='1', scale=2)
        else:
            from luma.core.interface.serial import spi
            serial = spi(device=0, port=0, bus_speed_hz=8000000, transfer_size=4096, gpio_DC=24, gpio_RST=25)
            super(Device, self).__init__(serial, rotate=2)


# Создание инстанса устройства
device: Device = Device()
