from platform import processor
is_emulator = processor() in ['x86_64', 'i386']

if is_emulator:
    from luma.emulator.device import pygame
    device = pygame(mode='1', scale=2, frame_rate=15)
else:
    from luma.oled.device import sh1106
    from luma.core.interface.serial import spi
    serial = spi(device=0, port=0, bus_speed_hz=8000000, transfer_size=4096, gpio_DC=24, gpio_RST=25)
    device = sh1106(serial, rotate=2)