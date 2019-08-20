from luma.oled.device import sh1106
import RPi.GPIO as GPIO


class Hardware(sh1106):
    def __init__(self, serial):
        super().__init__(serial, rotate=2)
        self.__pins = [6, 19, 5, 26, 13, 21, 20, 16]
        self.gpio_init()

    def gpio_init(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.__pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def apply_actions(self):
        self.__pressed_buttons.clear()
        for button in self.__pins:
            if not GPIO.input(button):
                self.__pressed_buttons.append(button)

    def get_pressed(self):
        return self.__pressed_buttons

    def display(self, image):
        assert(image.mode == self.mode)
        assert(image.size == self.size)
        self.apply_actions()

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
