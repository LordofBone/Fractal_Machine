import math

from turtles.base_turtle import BaseTurtle
from utils.fibonacci_core import FibonacciSeq

"""
Fibonacci sequence turtle, thanks to:
https://www.geeksforgeeks.org/python-plotting-fibonacci-spiral-fractal-using-turtle/
"""


class FibonacciSpiral(BaseTurtle):

    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False, max_moves=100, factor=1):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.factor = factor
        self.max_moves = max_moves
        self.sequence = FibonacciSeq()

    def fibo_plot(self):
        # Drawing the first square
        self.t.forward(self.sequence.current * self.factor)
        self.colour_change()
        self.t.left(90)
        self.t.forward(self.sequence.current * self.factor)
        self.colour_change()
        self.t.left(90)
        self.t.forward(self.sequence.current * self.factor)
        self.colour_change()
        self.t.left(90)
        self.t.forward(self.sequence.current * self.factor)
        self.colour_change()

        # Proceeding in the Fibonacci Series
        self.sequence.step()

        # Drawing the rest of the squares
        for i in range(1, self.max_moves):
            self.t.backward(self.sequence.current * self.factor)
            self.colour_change()
            self.t.right(90)
            self.t.forward(self.sequence.next * self.factor)
            self.colour_change()
            self.t.left(90)
            self.t.forward(self.sequence.next * self.factor)
            self.colour_change()
            self.t.left(90)
            self.t.forward(self.sequence.next * self.factor)
            self.colour_change()

            # Proceeding in the Fibonacci Series
            self.sequence.step()

        # Bringing the pen to starting point of the spiral plot
        self.goto(self.start_pos_x, self.start_pos_y)
        self.t.seth(0)

        self.colour_change()

        # Fibonacci Spiral Plot
        self.t.left(90)
        self.sequence.current = 0
        self.sequence.next = 1
        self.sequence.step()
        for i in range(self.max_moves):
            fdwd = math.pi * self.sequence.current * self.factor / 2
            fdwd /= 90
            for j in range(90):
                self.t.forward(fdwd)
                self.colour_change()
                self.t.left(1)
                self.colour_change()
            self.sequence.step()

    def step(self):
        self.fibo_plot()
