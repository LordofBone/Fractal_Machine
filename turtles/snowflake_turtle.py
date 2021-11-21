from turtles.base_turtle import BaseTurtle

"""
Snowflake turtle, thanks to:
https://www.geeksforgeeks.org/snowflakes-fractal-using-python/
"""


class SnowflakeTurtle(BaseTurtle):
    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, star_size=4):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.star_size = star_size

    # create a function to create different size snowflakes
    def snowflake(self):
        # move the pen into starting position
        self.t.penup()
        self.t.forward(10 * self.star_size)
        self.t.left(45)
        self.t.pendown()

        # draw branch 8 times to make a snowflake
        for i in range(8):
            self.branch()
            self.t.left(45)

            # create one branch of the snowflake

    def branch(self):

        for i in range(3):

            for j in range(3):
                self.t.forward(10.0 * self.star_size / 3)
                self.t.backward(10.0 * self.star_size / 3)
                self.t.right(45)
                self.colour_change()
            self.t.left(90)
            self.t.backward(10.0 * self.star_size / 3)
            self.t.left(45)
            self.colour_change()

        self.t.right(90)
        self.t.forward(10.0 * self.star_size)
        self.colour_change()

    def step(self):
        self.snowflake()
