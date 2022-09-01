import pygame


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # --- GET THE FULLSCREEN DISPLAY DESCRIPTION AS A VARIABLE --- #
        resolution = pygame.display.Info()

        # --- SCREEN SETTINGS (RESOLUTION AND COLOR) --- #
        self.screen_width = resolution.current_w
        self.screen_height = resolution.current_h
        self.background_colour = (230, 230, 230)

        # --- SHIP SPEED SETTINGS --- #
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # --- BULLET SETTINGS
        # --- HAVE THE BULLETS TRAVEL AT HALF THE SPEED OF THE SHIP --- #
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 214, 34, 34
        self.bullets_allowed = 10

        # --- ALIEN SETTINGS --- #
        # --- FLEET DIRECTION OF 1 REPRESENTS RIGHT; -1 REPRESENTS LEFT --- #
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 15
        self.fleet_direction = 1
