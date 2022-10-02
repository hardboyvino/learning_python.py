"""
A file containing all things relating to the cars.
"""

import pygame


class HeroCar(object):
    """A class for the hero car."""

    def __init__(self, screen) -> None:
        """Initialize the hero car."""
        self.screen = screen

        # --- load the ship image and its rectangles (rect)
        self.image = pygame.image.load("images/hero_car.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # --- set the colorkey of the image's white background to be transparent
        self.image.set_colorkey((255, 255, 255))

        # --- start the new car at the middle-bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # --- set a movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's movement."""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        """Draw the car at its current starting position."""
        self.screen.blit(self.image, self.rect)
