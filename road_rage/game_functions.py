"""
All the game functions.
"""

import sys
import pygame
from time import sleep

from car import VillianCar


def check_events(hero_car):
    """Check for keyboard and mouse events."""
    # --- watch for keyboard and mouse events.
    for event in pygame.event.get():
        # --- if a key is pressed down, check what the response should be
        if event.type == pygame.KEYDOWN:
            check_keydown_events(hero_car, event)
        # --- if a key is released, check what the response should be
        elif event.type == pygame.KEYUP:
            check_keyup_events(hero_car, event)


def check_keyup_events(hero_car, event):
    """Check event reaction when keys are released."""
    if event.key == pygame.K_RIGHT:
        hero_car.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero_car.moving_left = False
    elif event.key == pygame.K_UP:
        hero_car.moving_up = False
    elif event.key == pygame.K_DOWN:
        hero_car.moving_down = False


def check_keydown_events(hero_car, event):
    """Check event reaction when keys are pressed down."""
    if event.key == pygame.K_RIGHT:
        hero_car.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero_car.moving_left = True
    elif event.key == pygame.K_UP:
        hero_car.moving_up = True
    elif event.key == pygame.K_DOWN:
        hero_car.moving_down = True

    # --- quit the game when the escape key is pressed
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def new_car(villian_cars, screen, settings):
    """Create a new villian car and add it to the villian group."""
    if len(villian_cars) < settings.cars_allowed:
        new_car = VillianCar(screen, settings)
        villian_cars.add(new_car)


def update_screen(settings, screen, hero_car, villian_cars):
    """Update the screen with required images and background colours."""
    # --- fill the screen with specific background colour
    # --- draw the car to screen
    # screen.fill(settings.background_colour)
    hero_car.blitme()

    # --- draw each villian car in the group onscreen
    for villian_car in villian_cars.sprites():
        villian_car.blitme()

    # --- make the most recently drawn screen visible
    pygame.display.flip()
