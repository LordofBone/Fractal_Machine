from turtles.base_turtle import BaseTurtle

"""
H-Tree fractal turtle, thanks to:
Robin Andrews
https://compucademy.net/
"""


class HTurtle(BaseTurtle):

    def __init__(self, speed=0, pensize=2, stamp=False, gradient_step=0.001, rand_pos=False,
                 drawing_width=700, drawing_height=700, fractal_depth=3):
        """
        Call base turtle class, setup and configure a turtles defaults.
        """
        super().__init__(speed, pensize, stamp, gradient_step, rand_pos)
        self.drawing_width = drawing_width
        self.drawing_height = drawing_height
        self.fractal_depth = fractal_depth

    def draw_line(self, pos1, pos2):
        self.colour_change()
        self.goto(pos1[0], pos1[1])
        self.t.goto(pos2[0], pos2[1])

    def recursive_draw(self, x, y, width, height, count):
        self.draw_line(
            [x + width * 0.25, height // 2 + y],
            [x + width * 0.75, height // 2 + y],
        )
        self.draw_line(
            [x + width * 0.25, (height * 0.5) // 2 + y],
            [x + width * 0.25, (height * 1.5) // 2 + y],
        )
        self.draw_line(
            [x + width * 0.75, (height * 0.5) // 2 + y],
            [x + width * 0.75, (height * 1.5) // 2 + y],
        )

        if count <= 0:  # The base case
            return
        else:  # The recursive step
            count -= 1
            # Top left
            self.recursive_draw(x, y, width // 2, height // 2, count)
            # Top right
            self.recursive_draw(x + width // 2, y, width // 2, height // 2, count)
            # Bottom left
            self.recursive_draw(x, y + width // 2, width // 2, height // 2, count)
            # Bottom right
            self.recursive_draw(x + width // 2, y + width // 2, width // 2, height // 2, count)

    def step(self):
        self.recursive_draw(- self.drawing_width / 2, - self.drawing_height / 2, self.drawing_width,
                            self.drawing_height, self.fractal_depth)
