from gui_launcher import TurtleManagerAccess
from turtles import *

"""
A module for running tests without going through the GUI also 
allows for some hidden settings within turtles.
"""

if __name__ == '__main__':
    TurtleManagerAccess.max_turtles = 5000
    for i in range(1):
        # TurtleManagerAccess.add_turtle(KochCurve(stamp=True, rand_pos=True))
        # TurtleManagerAccess.add_turtle(BranchTree(branch_length=30, shorten_by=2, angle=20, rand_pos=False))
        # TurtleManagerAccess.add_turtle(BranchTree(angle=60, rand_pos=True))
        # TurtleManagerAccess.add_turtle(BranchTree(min_branch=10, angle=60, rand_pos=False))
        TurtleManagerAccess.add_turtle(FibonacciSpiral(max_moves=10, rand_pos=False))
        # TurtleManagerAccess.add_turtle(TriangleTurtle(depth=5, pensize=2, rand_pos=True))
        # TurtleManagerAccess.add_turtle(StarTurtle(root_length=100, rand_pos=True))
        # TurtleManagerAccess.add_turtle(HTurtle())
        # TurtleManagerAccess.add_turtle(CarpetTurtle(rand_pos=False))
        # TurtleManagerAccess.add_turtle(HoneycombTurtle(size=80))
    TurtleManagerAccess.draw_sequence()
