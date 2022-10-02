"""
The main program for the road rage game.
"""

import sys
import pygame

from settings import Settings
from car import HeroCar
import game_functions as gf

def run_game():
    """Initialize the game and creates a screen objects."""

    # --- create settings instance
    settings = Settings()

    # --- initialize pygame, set the screen size and window caption
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Road Rage")

    # --- create hero car instance
    hero_car = HeroCar(screen)

    # --- start the main loop for the game
    while True:
        gf.check_events(hero_car)
        hero_car.update()
        gf.update_screen(settings, screen, hero_car)
run_game()
