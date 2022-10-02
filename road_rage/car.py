"""
A file containing all things relating to the cars.
"""

import pygame
from random import choice
from pygame.sprite import Sprite


class HeroCar(object):
    """A class for the hero car."""

    def __init__(self, screen) -> None:
        """Initialize the hero car."""
        self.screen = screen

        # --- load the car's image and its rectangles (rect)
        self.image = pygame.image.load("images/hero_car.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # --- set the colorkey of the image's white background to be transparent
        self.image.set_colorkey((255, 255, 255))

        # --- start the new car at the middle-bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # --- set movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the car's position."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 5

    def blitme(self):
        """Draw the car at its current starting position."""
        self.screen.blit(self.image, self.rect)


class VillianCar(Sprite):
    """A class for the villian car."""

    def __init__(self, screen, settings) -> None:
        """Initialize the villian car."""
        super(VillianCar, self).__init__()
        self.screen = screen
        self.settings = settings

        # --- load the villian's car's image and its rectangles (rect)
        self.image = pygame.image.load("images/villian_car.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # --- set the colorkey of the image's white background to be transparent
        self.image.set_colorkey((255, 255, 255))

        # --- get the possible start positions in a list
        max_len = (self.screen_rect.right) - (self.rect.width)
        start_position = [self.screen_rect.left, max_len]

        # --- start the new car at a random position at the top of the screen
        self.rect.x = choice(start_position)
        self.rect.y = self.screen_rect.top

        # --- assign the drop speed variable from settings
        self.drop_speed = self.settings.villian_car_drop_speed

    def update(self):
        """Move the villian's car down the screen."""
        self.rect.y += self.drop_speed


    def blitme(self):
        """Draw the car at its starting position."""
        self.screen.blit(self.image, self.rect)
