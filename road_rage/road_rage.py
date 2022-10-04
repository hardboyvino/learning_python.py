"""
The main program for the road rage game.
"""

import pygame
from pygame.sprite import Group
import math


from background import GameBackground
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
    hero_car = HeroCar(screen, settings.hero_car_speed)
    villian_cars = Group()

    # --- create background instance
    background = GameBackground(screen, settings.screen_width, settings.screen_height, settings.timer, settings.fps)


    # --- start the main loop for the game
    while True:
        background.blitme()
        gf.check_events(hero_car)
        gf.new_car(villian_cars, screen, settings)
        hero_car.update()
        villian_cars.update()

        # --- get rid of cars that are offscreen
        for villian_car in villian_cars.copy():
            if villian_car.rect.top > settings.screen_height:
                villian_cars.remove(villian_car)

        gf.update_screen(settings, screen, hero_car, villian_cars)


run_game()
