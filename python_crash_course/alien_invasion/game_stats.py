class GameStats(object):
    """Track all the statistics of Alien Invasions game."""

    def __init__(self, ai_settings) -> None:
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
