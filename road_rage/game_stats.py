"""
A file for all the game statistics.
"""

class GameStats(object):
    """Track all the game statistics."""
    
    def __init__(self, settings) -> None:
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.cars_left = self.settings.hero_cars_limit
