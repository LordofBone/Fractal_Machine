from turtles.base_turtle import BaseTurtle

"""
Branching tree fractal turtle, thanks to:
https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
"""


class BranchTree(BaseTurtle):

    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, shorten_by=5, angle=30,
                 branch_length=50, min_branch=5):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.branch_length = branch_length
        self.shorten_by = shorten_by
        self.angle = angle
        self.min_branch = min_branch

    def branch(self, branch_length, shorten_by, angle):
        if branch_length > self.min_branch:
            if self.stamp:
                self.t.stamp()
            self.t.forward(branch_length)
            new_length = branch_length - shorten_by
            self.t.left(angle)
            self.branch(new_length, shorten_by, angle)
            self.t.right(angle * 2)
            self.branch(new_length, shorten_by, angle)
            self.t.left(angle)
            self.t.backward(branch_length)
            self.colour_change()

    def step(self):
        self.branch(self.branch_length, self.shorten_by, self.angle)
