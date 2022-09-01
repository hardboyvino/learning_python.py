"""Modules required from python libraries for making the game functional."""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage the bullets attributes and behaviours."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # --- CREATE A BULLET RECT AT (0,0) AXIS AND THEN SET THE CORRECT POSITION --- #
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # --- STORE THE BULLET'S POSITION AS A FLOAT --- #
        self.y = float(self.rect.y)

        # --- SET THE COLOR AND BULLET SPEED --- #
        self.colour = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullets up the screen."""
        # --- UPDATE THE POSITION OF THE BULLET --- #
        self.y -= self.speed_factor

        # --- UPDATE THE RECTANGLE POSITION OF THE BULLET --- #
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
