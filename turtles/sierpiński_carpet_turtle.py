from turtles.base_turtle import BaseTurtle

"""
Sierpiński carpet turtle, thanks to:
https://stackoverflow.com/questions/47841025/how-to-draw-a-sierpinski-carpet-in-python-using-turtle
"""


class CarpetTurtle(BaseTurtle):

    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, box_size=400,
                 box_depth=4):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.box_size = box_size
        self.box_depth = box_depth

    def box(self, box_depth, box_size):

        self.colour_change()

        if box_depth == 0:

            self.t.begin_fill()
            for i in range(4):
                self.t.forward(box_size)
                self.t.left(90)
            self.t.end_fill()

        else:

            for i in range(4):
                self.box(box_depth - 1, box_size / 3)
                self.t.forward(box_size / 3)

                self.box(box_depth - 1, box_size / 3)
                self.t.forward(box_size / 3)

                self.t.forward(box_size / 3)
                self.t.left(90)

    def step(self):
        self.box(self.box_depth, self.box_size)
