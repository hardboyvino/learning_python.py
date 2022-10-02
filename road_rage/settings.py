"""
A file containing all the settings required by the game.
"""


class Settings(object):
    """A class to store all the settings for the Road Rage game."""

    def __init__(self) -> None:
        """Initialize the game's settings class."""
        # --- screen settings
        self.screen_width = 540
        self.screen_height = 960
        self.background_colour = (255, 255, 255)

        # --- villian car settings
        self.villian_car_drop_speed = 1.3
        self.cars_allowed = 1
