from luma.oled.device import sh1106
import RPi.GPIO as GPIO
from time import time
from period.core.device import BaseDevice

pins = [6, 19, 5, 26, 13, 21, 20, 16]

GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class Hardware(sh1106, BaseDevice):
    pressed_buttons = []

    def __init__(self, serial):
        super(Hardware, self).__init__(serial, rotate=2)

    def apply_actions(self):
        self.pressed_buttons.clear()
        for button in pins:
            if GPIO.input(button) == 0:
                self.pressed_buttons.append(button)

        self.check_exit(buttons=[5, 21, 20])

    def get_pressed(self):
        return self.pressed_buttons

    def display(self, image):
        self.start_time = time()
        assert(image.mode == self.mode)
        assert(image.size == self.size)
        self.apply_actions()
        self.show_fps(image=image)

        image = self.preprocess(image)

        set_page_address = 0xB0
        image_data = image.getdata()
        pixels_per_page = self.width * 8
        buf = bytearray(self.width)

        for y in range(0, int(self._pages * pixels_per_page), pixels_per_page):
            self.command(set_page_address, 0x02, 0x10)
            set_page_address += 1
            offsets = [y + self.width * i for i in range(8)]

            for x in range(self.width):
                buf[x] = \
                    (image_data[x + offsets[0]] and 0x01) | \
                    (image_data[x + offsets[1]] and 0x02) | \
                    (image_data[x + offsets[2]] and 0x04) | \
                    (image_data[x + offsets[3]] and 0x08) | \
                    (image_data[x + offsets[4]] and 0x10) | \
                    (image_data[x + offsets[5]] and 0x20) | \
                    (image_data[x + offsets[6]] and 0x40) | \
                    (image_data[x + offsets[7]] and 0x80)

            self.data(list(buf))
        self.frame_rate = round(1 / (time() - self.start_time), 1)
