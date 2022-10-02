from random import randint

class Die(object):
    """A class for a single die."""
    def __init__(self, num_sides=6) -> None:
        """A die with a default 6 sides."""
        self.num_sides = num_sides


    def roll_dice(self):
        """Roll the dice and return the number selected."""
        return randint(1, self.num_sides)
