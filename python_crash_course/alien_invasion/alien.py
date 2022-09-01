"""Modules required from libraries for making the aliens attributes and behaviours"""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Create class for the alien ships that will be shot down."""

    def __init__(self, ai_settings, screen) -> None:
        super().__init__()
        """Initialize the alien."""
        self.screen = screen
        self.ai_settings = ai_settings

        # --- LOAD THE ALIEN SHIP AND GET THE IMAGE RECTANGLES --- #
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # --- START EACH NEW ALIEN NEAR THE TOP LEFT OF THE SCREEN --- #
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # --- STORE THE ALIEN'S EXACT LOCATION --- #
        self.x = float(self.rect.x)


    def update(self) -> None:
        """Move the alien right."""
        # --- UPDATE THE POSITION OF THE BULLET --- #
        self.rect.x += (float(self.ai_settings.alien_speed_factor) * self.ai_settings.fleet_direction)


    def check_edge(self):
        """Return True if alien is at the edge of the screen."""
        if (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0):
            return True
        return None


    def blitme(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)
