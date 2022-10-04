"""
A file containing all the settings required by the game.
"""

import pygame


class Settings(object):
    """A class to store all the settings for the Road Rage game."""

    def __init__(self) -> None:
        """Initialize the game's settings class."""
        # --- screen settings
        self.screen_width = 540
        self.screen_height = 960
        self.background_colour = (255, 255, 255)

        # --- background settings
        self.timer = pygame.time.Clock()
        self.fps = 60

        # --- speeding up the game
        self.speed_up = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings changing throughout the game."""
        # --- hero car settings
        # --- cars limit is extra cars allowed
        self.hero_car_speed = 10.0
        self.hero_cars_limit = 1.0

        # --- villian car settings
        self.villian_car_drop_speed = 5.0
        self.cars_allowed = 1.0

    def increase_difficulty(self):
        """Make the game more difficult."""
        self.villian_car_drop_speed *= self.speed_up
        self.hero_cars_limit += 1.0
