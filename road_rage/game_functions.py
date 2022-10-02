"""
All the game functions.
"""

import sys
import pygame

from settings import Settings
from car import HeroCar


def check_events(hero_car):
    """Check for keyboard and mouse events."""
    # --- watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if event.key == pygame.K_ESCAPE:
                sys.exit()

        # --- if the right key is pressed down, move the car right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero_car.moving_right = True
            elif event.key == pygame.K_LEFT:
                hero_car.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hero_car.moving_right = False
            elif event.key == pygame.K_LEFT:
                hero_car.moving_left = False


def update_screen(settings, screen, hero_car):
    """Update the screen with required images and background colours."""
    # --- fill the screen with specific background colour
    # --- draw the car to screen
    screen.fill(settings.background_colour)
    hero_car.blitme()

    # --- make the most recently drawn screen visible
    pygame.display.flip()
