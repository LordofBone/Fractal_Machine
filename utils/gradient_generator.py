import colorsys
import random
from dataclasses import dataclass

"""
This is the class that all turtles call to calculate colour gradient changes
Thanks to:
https://www.programcreek.com/python/example/4618/colorsys.hsv_to_rgb
"""


@dataclass
class Colours:
    gradient_step: float
    R: int = 0
    G: int = 0
    B: int = 0
    hue: float = 0.0

    def __post_init__(self):
        self.random()

    def step_gradient(self):
        """
        Step the gradient forward by the gradient step.
        """
        if self.hue < 1.0:
            self.hue += self.gradient_step
        else:
            self.hue = 0.0
        self.colour()

    def colour(self):
        """
        Return RGB colours from converted hue
        https://docs.python.org/2/library/colorsys.html
        """
        (r, g, b) = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0)
        self.R, self.G, self.B = int(255 * r), int(255 * g), int(255 * b)

    def random(self):
        """
        Set a random colour.
        """
        self.hue = random.uniform(0.0, 1.0)
        self.colour()
