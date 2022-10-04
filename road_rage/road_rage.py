"""
The main program for the road rage game.
"""

import pygame
from pygame.sprite import Group
from datetime import datetime


from background import GameBackground
from settings import Settings
from car import HeroCar
from game_stats import GameStats
import game_functions as gf

start_time = datetime.now()


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
    stats = GameStats(settings)

    # clock = pygame.time.Clock()
    # start = 500

    # --- create background instance
    background = GameBackground(screen, settings.screen_width, settings.screen_height, settings.timer, settings.fps)

    # --- start the main loop for the game
    while True:
        gf.check_events(hero_car)

        if stats.game_active:
            # gf.stop_game(settings, clock, start)
            background.blitme()
            gf.new_car(villian_cars, screen, settings)
            hero_car.update()
            villian_cars.update()
            gf.update_cars(hero_car, villian_cars, settings, stats, screen, background)
            # gf.stop_game(start_time, settings, clock, start)

        gf.update_screen(hero_car, villian_cars)


run_game()
