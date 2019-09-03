from luma.emulator.device import pygame
from sys import exit
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_1, K_2, K_3, K_RSHIFT
from time import time
from period.core.device import BaseDevice


class Emulator(pygame, BaseDevice):
    def __init__(self, mode='1', scale=2, frame_rate=16):
        super(Emulator, self).__init__(mode=mode, scale=scale, frame_rate=frame_rate)
        self._pygame.display.set_caption('Period Simulator')
        self.pressed_buttons = []

    def apply_actions(self):
        keystate = self._pygame.key.get_pressed()

        if keystate[self._pygame.K_ESCAPE] or self._pygame.event.peek(self._pygame.QUIT):
            self._pygame.quit()
            exit()

        self.pressed_buttons.clear()
        for button in [K_UP, K_DOWN, K_RIGHT, K_LEFT, K_1, K_2, K_3, K_RSHIFT]:
            if keystate[button]: self.pressed_buttons.append(button)

        self.check_exit(buttons=[K_LEFT, K_1, K_2])

    def get_pressed(self):
        return self.pressed_buttons

    def display(self, image):
        self.start_time = time()
        assert (image.size == self.size)
        self._last_image = image

        self.show_fps(image=image)

        image = self.preprocess(image)
        self._clock.tick(self._fps)
        self._pygame.event.pump()
        self.apply_actions()

        surface = self.to_surface(image, alpha=self._contrast)
        if self._screen is None:
            self._screen = self._pygame.display.set_mode(surface.get_size())
        self._screen.blit(surface, (0, 0))
        self._pygame.display.flip()
        self.frame_rate = round(1 / (time() - self.start_time), 1)
