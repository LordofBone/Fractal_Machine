from turtles.base_turtle import BaseTurtle

"""
Sierpiński triangle turtle, thanks to:
http://www.lpb-riannetrujillo.com/blog/python-fractal/
"""


class TriangleTurtle(BaseTurtle):

    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, depth=4):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.depth = depth
        self.points = [[-175, -125], [0, 175], [175, -125]]  # size of triangle

    def get_mid(self, p1, p2):
        return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2  # find midpoint

    def triangle(self, points, depth):
        if self.stamp:
            self.t.stamp()
        self.t.up()
        self.t.goto(points[0][0], points[0][1])
        self.t.down()
        self.t.goto(points[1][0], points[1][1])
        self.t.goto(points[2][0], points[2][1])
        self.t.goto(points[0][0], points[0][1])

        if depth > 0:
            self.triangle([points[0],
                           self.get_mid(points[0], points[1]),
                           self.get_mid(points[0], points[2])],
                          depth - 1)
            self.triangle([points[1],
                           self.get_mid(points[0], points[1]),
                           self.get_mid(points[1], points[2])],
                          depth - 1)
            self.triangle([points[2],
                           self.get_mid(points[2], points[1]),
                           self.get_mid(points[0], points[2])],
                          depth - 1)
        self.colour_change()

    def step(self):
        self.points = [[self.start_pos_x - 175, self.start_pos_y - 125], [self.start_pos_x, self.start_pos_y + 175],
                       [self.start_pos_x + 175, self.start_pos_y - 125]]
        self.triangle(self.points, self.depth)
