import random

import pygame


class Ship():
    """Create class for the Alien Invasion shooter ship."""

    def __init__(self, screen) -> None:
        """Initialise the ship and set the starting position."""
        self.screen = screen

        # --- LOAD THE SHIP IMAGE AND GET ITS RECTANGLE SURFACE --- #
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # --- START EACH NEW SHIP AT THE BOTTOM CENTER OF THE SCREEN --- #
        # --- FORM LISTS OF POSSIBLE STARTING POSITIONS --- #
        y_coordinates = [self.screen_rect.centery, self.screen_rect.bottom]

        # --- FROM THE LIST SELECT A RANDOM STARTING POSITION FOR BOTH X AND Y COORDINATES --- #
        y_start = random.choice(y_coordinates)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = y_start

    def blitme(self):
        """Draw the shooter ship on the screen."""
        self.screen.blit(self.image, self.rect)
