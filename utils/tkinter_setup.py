import _tkinter
import turtle
import tkinter as tk

"""
Main tkinter stuff is setup here, the GUI launcher grabs the canvas from here
and base turtle grabs the width and height 
from here in order to set random positions within the canvas.
"""


class TkinterBase:
    def __init__(self, title="Fractal Machine", width=800, height=600):
        self.width = width
        self.height = height
        self.master = tk.Tk()
        # linux (Raspberry Pi OS) does not like this 'zoomed' setting, on exception will set to 'normal' to workaround
        try:
            self.master.state('zoomed')
        except _tkinter.TclError:
            self.master.state('normal')
        self.canvas = tk.Canvas(self.master)
        self.master.title(title)
        self.canvas.config(width=self.width, height=self.height)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)


TkinterBaseAccess = TkinterBase()
