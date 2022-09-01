"""Modules required from python libraries for making the game functional."""
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
        y_coordinates = [self.screen_rect.bottom]

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
        # --- IF THE SHIP COORDINATES IS MORE THAN MAX SCREEN SIZE, STOP MOVING SO SHIP DOES NOT LEAVE THE SCREEN --- #
        # --- SAME FOR ALL DIRECTIONS CONSIDERING THE 0,0 AXIS IS THE TOP-LEFT CORNER --- #
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_settings.ship_speed_factor

    def center_ship(self):
        """Center the ship after every respawn."""
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = float(self.screen_rect.bottom)


    def blitme(self):
        """Draw the shooter ship on the screen."""
        self.screen.blit(self.image, self.rect)
