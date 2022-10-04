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

        # --- hero car settings
        self.hero_car_speed = 10

        # --- villian car settings
        self.villian_car_drop_speed = 5
        self.cars_allowed = 1

        # --- background settings
        self.timer = pygame.time.Clock()
        self.fps = 60
