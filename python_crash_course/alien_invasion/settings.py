class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # --- SCREEN SETTINGS --- #
        self.screen_width = 1280
        self.screen_height = 720
        self.background_color = (230, 230, 230)

        # --- SHIP SETTINGS --- #
        self.ship_speed_factor = 1.5
