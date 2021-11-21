from turtles.base_turtle import BaseTurtle

"""
Honey comb fractal turtle, thanks to:
Lasse Kosiol
https://gist.github.com/utstikkar/3618027
"""


class HoneycombTurtle(BaseTurtle):
    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, size=20,
                 circles=20):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.size = size
        self.circles = circles

    def move(self, length, angle):
        self.t.right(angle)
        self.t.forward(length)

    def hex(self):
        self.t.pendown()
        self.colour_change()
        self.t.begin_fill()
        for i in range(6):
            self.move(self.size, -60)
        self.t.end_fill()
        self.t.penup()

    def step(self):
        self.t.penup()

        for circle in range(self.circles):
            if circle == 0:
                self.hex()
                self.move(self.size, -60)
                self.move(self.size, -60)
                self.move(self.size, -60)
                self.move(0, 180)
            for i in range(6):
                self.move(0, 60)
                for j in range(circle + 1):
                    self.hex()
                    self.move(self.size, -60)
                    self.move(self.size, 60)
                self.move(-self.size, 0)
            self.move(-self.size, 60)
            self.move(self.size, -120)
            self.move(0, 60)
