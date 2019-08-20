from platform import processor
is_emulator = processor() in ['x86_64', 'i386']
device = 0

if is_emulator:
    from period.core.emulator import Emulator
    device = Emulator(mode='1', scale=2, frame_rate=16)
else:
    from luma.core.interface.serial import spi
    from period.core.hardware import Hardware
    serial = spi(device=0, port=0, bus_speed_hz=8000000, transfer_size=4096, gpio_DC=24, gpio_RST=25)
    device = Hardware(serial=serial)
