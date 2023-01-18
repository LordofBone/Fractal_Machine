import turtle
from random import randrange

from utils.gradient_generator import Colours
from utils.tkinter_setup import TkinterBaseAccess

"""
The base class that all turtles call, this contains
all of the default settings that every turtle uses
as well as the step function that moves each turtle
"""


# todo: make this an ABC class?
class BaseTurtle:

    def __init__(self, speed, pensize, stamp, gradient_step, rand_pos, rendered=False):
        """
        Setup and configure a turtles defaults.
        """
        self.t = turtle.RawTurtle(TkinterBaseAccess.screen)
        self.colours = Colours(gradient_step)
        self.t.speed(speed)
        self.t.pensize(pensize)
        TkinterBaseAccess.screen.colormode(255)
        self.t.pencolor(self.colours.R, self.colours.G, self.colours.B)
        self.t.hideturtle()
        self.stamp = stamp
        self.rand_pos = rand_pos
        self.rendered = rendered
        if self.rand_pos:
            self.start_pos_x = randrange(int(-TkinterBaseAccess.width / 2), int(TkinterBaseAccess.width / 2))
            self.start_pos_y = randrange(int(-TkinterBaseAccess.height / 2), int(TkinterBaseAccess.height / 2))
        else:
            self.start_pos_x = 0
            self.start_pos_y = 0

        self.goto(self.start_pos_x, self.start_pos_y)

    def colour_change(self):
        """
        This is where the colour hue is stepped forward.
        """
        self.colours.step_gradient()
        self.t.pencolor(self.colours.R, self.colours.G, self.colours.B)

    def goto(self, x=0, y=0):
        """
        Moves the turtle to a position without leaving a trace.
        """
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    # todo: find a way to step once or multi-thread draws ?
    def run(self):
        """
        This is called by the TurtleManager under gui_launcher
        to perform the specific turtles drawing actions.
        """
        if not self.rendered:
            self.step()
