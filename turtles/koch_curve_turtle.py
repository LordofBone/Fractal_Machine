from turtles.base_turtle import BaseTurtle

"""
Koch curve turtle, thanks to:
https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
"""


class KochCurve(BaseTurtle):

    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, iterations=4, length=200,
                 angle=60, shortening_factor=3,
                 loops=3, last_angle=120):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.loops = loops
        self.angle = angle
        self.last_angle = last_angle
        self.length = length
        self.iterations = iterations
        self.shortening_factor = shortening_factor

    def koch_curve(self, iterations, length, shortening_factor, angle):
        if self.stamp:
            self.t.stamp()
        if iterations == 0:
            self.t.forward(length)
        else:
            iterations = iterations - 1
            length = length / shortening_factor
            self.koch_curve(iterations, length, shortening_factor, angle)
            self.t.left(angle)
            self.koch_curve(iterations, length, shortening_factor, angle)
            self.t.right(angle * 2)
            self.koch_curve(iterations, length, shortening_factor, angle)
            self.t.left(angle)
            self.koch_curve(iterations, length, shortening_factor, angle)
        self.colour_change()

    def step(self):
        for i in range(self.loops):
            self.koch_curve(self.iterations, self.length, self.shortening_factor, self.angle)
            self.t.right(self.last_angle)
