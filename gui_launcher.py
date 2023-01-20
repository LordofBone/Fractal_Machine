import datetime
import json
import os
import sys
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from _tkinter import TclError

from config.directories import *
from functions.json_download_convert import convert_b64_to_image
from gui.gui_items import Items
from gui.tkinter_setup import TkinterBaseAccess
from ml.openai_api import get_variants
from turtles import *
from utils.gradient_generator import Colours

"""
The main GUI launcher
"""


class TurtleManager:

    def __init__(self, max_turtles=100, random_bg=False, turtle_queueing=False, live_draw=False,
                 random_positions=False):
        """
        Call base tkinter setup class, configure default variables and canvas settings.
        """
        self.screen = TkinterBaseAccess.screen
        self.width = TkinterBaseAccess.width
        self.height = TkinterBaseAccess.height

        self.master = TkinterBaseAccess.master

        self.style = ttk.Style(self.master)

        self.turtle_queueing = turtle_queueing
        self.live_draw = live_draw
        self.random_positions = random_positions

        self.screen.colormode(255)

        self.gui_locked = False

        self.live_draw_checker()

        self.max_turtles = max_turtles
        self.turtles = []

        self.turtle_count = 0
        self.branch_count = 0
        self.fibo_count = 0
        self.honey_count = 0
        self.h_count = 0
        self.koch_count = 0
        self.carp_count = 0
        self.tri_count = 0
        self.snow_count = 0
        self.star_count = 0

        self.items = Items(self)

        self.turtle_configs_reset()

        self.turtle_reset()

        self.canvas_colour = Colours(gradient_step=0)
        if random_bg:
            self.random_background()

    def element_config(self, element, button_state):
        """
        Configure the element, also handles if the element cannot be disabled and if so, skips it.
        """
        try:
            element.configure(state=button_state)
        except TclError:
            pass

    def lock_unlock_gui(self):
        """
        Lock/unlock the GUI.
        """
        if self.gui_locked:
            button_state = NORMAL
            self.gui_locked = False
        else:
            button_state = DISABLED
            self.gui_locked = True

        for frame in self.items.main_ui.master.winfo_children():
            for element in frame.winfo_children():
                self.element_config(element, button_state)
                for sub_element in element.winfo_children():
                    self.element_config(sub_element, button_state)
                    for sub_sub_element in sub_element.winfo_children():
                        self.element_config(sub_sub_element, button_state)

    def live_draw_checker(self):
        """
        Check if live drawing has been set and turn trace on/off accordingly.
        """
        if not self.live_draw:
            TkinterBaseAccess.screen.tracer(0, 0)
        else:
            TkinterBaseAccess.screen.tracer(1)

    def change_theme(self):
        """
        Change the canvas theme with theme selected from the dropdown.
        """
        self.style.theme_use(self.items.theme_variable.get())

    def random_background(self):
        """
        Set a random background to the canvas.
        """
        self.canvas_colour.random()
        color_val = "#%02x%02x%02x" % (self.canvas_colour.R, self.canvas_colour.G, self.canvas_colour.B)
        TkinterBaseAccess.canvas.create_rectangle(-400, -300, 400, 300, fill=color_val, outline=color_val)

    def init_ml(self):
        """
        Initialise the machine learning algorithm to get variants of the generated image using DALL-E 2.
        """

        # todo: move all this to a separate class?
        self.lock_unlock_gui()

        self.items.button_init_ml.config(text="ML Generating...")
        self.items.button_init_ml.update()

        self.progress_bar_step()

        self.screen.update()

        self.progress_bar_step()

        TkinterBaseAccess.canvas.postscript(file=data_dir / "canvas.eps")

        self.progress_bar_step()

        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        with Image.open(data_dir / "canvas.eps") as canvas:
            new_size = (600, 600)
            im1 = canvas.resize(new_size)
            # save the resized image for compatibility with DALL-E
            im1.save(images_dir / "canvas.png", "png")

            # save the original canvas for 1:1 comparison with the newly generated image
            file_name = f"canvas_{current_time}.png"
            file_path = images_dir / file_name
            canvas.save(file_path, "png")

        self.progress_bar_step()

        os.remove(data_dir / "canvas.eps")

        self.progress_bar_step()

        response = get_variants()

        os.remove(images_dir / "canvas.png")

        self.progress_bar_step()

        new_file_name = f"variation-{response['created']}.json"

        self.progress_bar_step()

        with open(data_dir / new_file_name, mode="w", encoding="utf-8") as file:
            json.dump(response, file)

        self.progress_bar_step()

        ml_img = convert_b64_to_image(new_file_name, response)

        self.progress_bar_step()

        img = ImageTk.PhotoImage(Image.open(ml_img))

        self.progress_bar_step()

        self.clear_screen()

        TkinterBaseAccess.canvas.create_image(0, 0, image=img)

        self.items.progress_bar.config(value=0)
        self.items.button_init_ml.config(text="ML Generation")
        self.screen.update()

        self.lock_unlock_gui()

        self.screen.update()

        self.screen.mainloop()

    def button_config_refresh(self):
        """
        Reset all turtle counts on the GUI buttons.
        """
        self.items.branch_button.config(text="Add Branching Tree (%a)" % self.branch_count)

        self.items.fibo_button.config(text="Add Fibonacci Spiral (%a)" % self.fibo_count)

        self.items.honey_button.config(text="Add Honeycomb (%a)" % self.honey_count)

        self.items.h_button.config(text="Add H-Tree (%a)" % self.h_count)

        self.items.koch_button.config(text="Add Koch Curve (%a)" % self.koch_count)

        self.items.carp_button.config(text="Add Sierpiński Carpet (%a)" % self.carp_count)

        self.items.tri_button.config(text="Add Sierpiński Triangle (%a)" % self.tri_count)

        self.items.snow_button.config(text="Add Snowflake (%a)" % self.snow_count)

        self.items.button_star.config(text="Add Star (%a)" % self.star_count)

        self.items.turtle_count_label.config(text='Total turtles: %a' % self.turtle_count)

        self.items.button_queue.config(text="Queuing: %a" % self.turtle_queueing)

        self.items.turtle_count_label.config(text=' Total turtles: %a' % self.turtle_count)

        self.items.button_rand.config(text="Random Positions: %a" % self.random_positions)

        self.items.button_live.config(text="Live Drawing: %a" % self.live_draw)

        self.items.progress_bar.config(value=0)

    def turtle_configs_reset(self):
        """
        Reset all turtle configurations to defaults.
        """
        self.items.branch_shortenby.set(5)
        self.items.branch_angle.set(30)
        self.items.branch_length.set(50)
        self.items.branch_min.set(5)
        self.items.fibo_maxmoves.set(100)
        self.items.honey_size.set(20)
        self.items.honey_circles.set(20)
        self.items.htree_fractal.set(3)
        self.items.carp_box_size.set(400)
        self.items.carp_box_depth.set(4)
        self.items.koch_iterations.set(4)
        self.items.koch_length.set(200)
        self.items.koch_angle.set(60)
        self.items.koch_short_factor.set(3)
        self.items.koch_loops.set(3)
        self.items.koch_langle.set(120)
        self.items.striangle_depth.set(4)
        self.items.snow_size.set(4)
        self.items.star_size.set(360)
        self.items.star_divider.set(5)
        self.items.star_root_length.set(216)

    def add_turtle(self, new_turtle):
        """
        Add a turtle into the pipeline
        """
        if not self.turtle_count >= self.max_turtles:
            new_turtle.goto(new_turtle.start_pos_x, new_turtle.start_pos_y)

            self.turtles.append(new_turtle)

            self.turtle_count += 1

        self.button_config_refresh()

    def progress_bar_step(self):
        """
        Increment the progress bar by 10.
        """
        if self.items.progress_bar['value'] < 100:
            self.items.progress_bar.step(10)
            self.screen.update()

    def percentage(self, number_in):
        """
        Calculate a percentage - used for the loading bar (currently not implemented).
        """
        return number_in / self.turtle_count * 100

    def draw_sequence(self):
        """
        Runs draw on all un-rendered turtles, when rendered sets the rendered status
        to 'True' so that they are not rendered again. This also has
        the loading bar code, this currently does not work as the loading bar refresh
        refreshes the entire canvas per move; slowing up the rendering.
        """
        self.lock_unlock_gui()

        self.items.button_draw.config(text="Drawing...")
        self.items.button_draw.update()

        for i in range(self.turtle_count):
            self.items.progress_bar.config(value=self.percentage(i))
            self.screen.update()
            self.turtles[i].run()
            self.turtles[i].rendered = True

        self.items.progress_bar.config(value=0)
        self.items.button_draw.config(text="Draw")
        self.button_config_refresh()

        self.lock_unlock_gui()

        self.screen.update()

        self.screen.mainloop()

    def turtle_reset(self):
        """
        Removes all turtles from the pipeline and resets all counts to 0.
        """
        self.turtles = []

        self.turtle_count = 0
        self.branch_count = 0
        self.fibo_count = 0
        self.honey_count = 0
        self.h_count = 0
        self.koch_count = 0
        self.carp_count = 0
        self.tri_count = 0
        self.snow_count = 0
        self.star_count = 0

        self.button_config_refresh()

    def clear_screen(self):
        """
        Clears the screen, resets the background colour and resets all turtles and config.
        """
        self.items.clear_button.config(text="Clearing...")
        self.items.clear_button.update()
        self.turtle_reset()
        self.turtle_configs_reset()

        TkinterBaseAccess.screen.clear()
        if not self.live_draw:
            TkinterBaseAccess.screen.tracer(0, 0)

        self.screen.colormode(255)

        self.items.clear_button.config(text="Clear")

    def queue_setter(self):
        """
        Switches queuing on or off; this allows the pipeline to be filled with
        turtles without rendering until user clicks 'Draw'.
        """
        self.turtle_queueing = not self.turtle_queueing
        self.button_config_refresh()

    def random_position_setter(self):
        """
        Sets whether patterns are drawn in random areas or in the center of the canvas.
        """
        self.random_positions = not self.random_positions
        self.button_config_refresh()

    def live_drawing_setter(self):
        """
        Sets live drawing on or off. When on the user can see the turtle draw the patterns.
        Cool visual, but slower to render.
        """
        self.live_draw = not self.live_draw

        self.live_draw_checker()

        self.button_config_refresh()

    def exit(self):
        self.screen.clear()
        sys.exit()

    """
    Here all the turtle classes are called and inserted into the pipeline
    along with their configurations set by the user from the GUI.
    """

    def add_branch(self):
        self.branch_count += 1
        self.add_turtle(BranchTree(shorten_by=self.items.branch_shortenby.get(), angle=self.items.branch_angle.get(),
                                   branch_length=self.items.branch_length.get(), min_branch=self.items.branch_min.get(),
                                   rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_fibonacci(self):
        self.fibo_count += 1
        self.add_turtle(FibonacciSpiral(max_moves=self.items.fibo_maxmoves.get(), rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_honeycomb(self):
        self.honey_count += 1
        self.add_turtle(HoneycombTurtle(size=self.items.honey_size.get(), circles=self.items.honey_circles.get(),
                                        rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_htree(self):
        self.h_count += 1
        self.add_turtle(HTurtle(fractal_depth=self.items.htree_fractal.get(), rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_koch(self):
        self.koch_count += 1
        self.add_turtle(KochCurve(iterations=self.items.koch_iterations.get(), length=self.items.koch_length.get(),
                                  angle=self.items.koch_angle.get(),
                                  shortening_factor=self.items.koch_short_factor.get(),
                                  loops=self.items.koch_loops.get(), last_angle=self.items.koch_langle.get(),
                                  rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_scarpet(self):
        self.carp_count += 1
        self.add_turtle(CarpetTurtle(box_size=self.items.carp_box_size.get(), box_depth=self.items.carp_box_depth.get(),
                                     rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_striangle(self):
        self.tri_count += 1
        self.add_turtle(TriangleTurtle(depth=self.items.striangle_depth.get(), rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_snowflake(self):
        self.snow_count += 1
        self.add_turtle(SnowflakeTurtle(star_size=self.items.snow_size.get(), rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()

    def add_star(self):
        self.star_count += 1
        self.add_turtle(StarTurtle(size=self.items.star_size.get(), size_divider=self.items.star_divider.get(),
                                   root_length=self.items.star_root_length.get(), rand_pos=self.random_positions))

        if not self.turtle_queueing:
            self.draw_sequence()


"""
Instantiates the GUI Turtle manager.
"""
TurtleManagerAccess = TurtleManager()

if __name__ == "__main__":
    TurtleManagerAccess.draw_sequence()
