"""
A document for all things background.
"""

import pygame
import math

from settings import Settings

class GameBackground(object):
    """A class for the background."""
    def __init__(self, screen, screen_width, screen_height, timer, fps, scroll = 0) -> None:
        """Initialize the background properties."""
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scroll = scroll
        self.fps = fps
        self.timer = timer

        # --- load the image to be used for the background
        self.background = pygame.image.load("images/road_2lane.bmp")

        # --- get the height of the image for the infinite scrolling
        self.background_height = self.background.get_height()

        # --- scale the image to fit on the screen properly
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.background_height))

        # --- number panels to be drawn at every single point in time
        # --- the magic number 2 is ensure there is always a panel to be displayed before and after the current panel
        self.panels = math.ceil(self.screen_height / self.background_height) + 2

    def blitme(self):
        """Draw the scrolling background unto the screen."""
        self.timer.tick(self.fps)

        for i in range(self.panels):
            # --- draw first image off the screen to the bottom and another ready offscreen ontop
            self.screen.blit(self.background, (0, i * self.background_height + self.scroll - self.background_height))

        # --- speed at which the background moves down the screen
        self.scroll += 1
        if abs(self.scroll) > self.background_height:
            self.scroll = 0
