from turtles.base_turtle import BaseTurtle

"""
Star turtle, thanks to:
https://www.geeksforgeeks.org/star-fractal-printing-using-turtle-in-python/
"""


class StarTurtle(BaseTurtle):

    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, size=360,
                 size_divider=3, root_length=216):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.size = size
        self.size_divider = size_divider
        self.root_length = root_length

    # function to draw stars
    def star(self, size):
        if size <= 10:
            return
        else:
            for i in range(5):
                self.colour_change()
                self.t.forward(size)
                self.star(size / self.size_divider)
                self.t.left(self.root_length)

    def step(self):
        self.star(self.size)
