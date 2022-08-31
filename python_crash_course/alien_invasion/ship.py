import random

import pygame


class Ship():
    """Create class for the Alien Invasion shooter ship."""

    def __init__(self, ai_settings, screen) -> None:
        """Initialise the ship and set the starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # --- LOAD THE SHIP IMAGE AND GET ITS RECTANGLE SURFACE --- #
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # --- START EACH NEW SHIP AT THE BOTTOM CENTER OF THE SCREEN --- #
        # --- FORM LISTS OF POSSIBLE STARTING POSITIONS --- #
        y_coordinates = [self.screen_rect.centery, self.screen_rect.bottom]

        # --- FROM THE LIST SELECT A RANDOM STARTING POSITION FOR BOTH X AND Y COORDINATES --- #
        # --- ALLOW THE COORDINATES TO BE FLOATS --- #
        y_start = random.choice(y_coordinates)
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = float(y_start)
        

        # --- MOVING FLAG --- #
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_movement(self):
        """Updates the movement of the ship for a smooth continous motion."""
        if self.moving_right:
            self.rect.centerx += 1.5
        elif self.moving_left:
            self.rect.centerx -= 1.5
        elif self.moving_up:
            self.rect.bottom -= 1.5
        elif self.moving_down:
            self.rect.bottom += 1.5

    def blitme(self):
        """Draw the shooter ship on the screen."""
        self.screen.blit(self.image, self.rect)
