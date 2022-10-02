"""
Create a random walks class and fill a walk for a number of points (by default 5000 walk points).
"""
from random import choice


class RandomWalks(object):
    """A class for random walks."""

    def __init__(self, num_points=5000) -> None:
        """Initialize the random walks class with a default number of points as 5,000."""
        self.num_points = num_points

        # --- ALL WALKS BEGIN FROM (0, 0) COORDINATE --- #
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Fill the x-coordinates and y-coordinates lists for the number of walks specified.\n
        Default number of points is 5,000.
        """
        # --- GET ALL THE RANDOM WALK POINTS --- #
        # --- RUN THE PROGRAM UNTIL THE MAX RANDOM WALK POINTS ARE GENERATED --- #
        while len(self.x_values) < self.num_points:
            x_step = self.x_step(self)
            y_step = self.y_step(self)

            # --- IF THE STEP GOES NOWHERE, IGNORE SUCH A STEP AND RESTART THE LOOP --- #
            if y_step == 0 and x_step == 0:
                continue

            # --- WHAT IS THE NEXT ACTUAL STEP OF X AND Y --- #
            actual_x_step = self.x_values[-1] + x_step
            actual_y_step = self.y_values[-1] + y_step

            self.x_values.append(actual_x_step)
            self.y_values.append(actual_y_step)

    @staticmethod
    def y_step(self):
        """Determine the direction and distance in the y-axis."""
        # --- UP OR DOWN? --- #
        y_direction = choice([-1, 1])

        # --- HOW MUCH IN WHATEVER DIRECTION --- #
        y_distance = choice([x for x in range(0, 5)])
        y_step = y_direction * y_distance
        return y_step

    @staticmethod
    def x_step(self):
        """Determine the direction and distance in the x-axis."""
        # --- LEFT OR RIGHT? --- #
        x_direction = choice([-1, 1])

        # --- HOW MUCH IN WHATEVER DIRECTION --- #
        x_distance = choice([x for x in range(0, 5)])
        x_step = x_direction * x_distance
        return x_step
