import tkinter as tk
from tkinter import ttk
from tkinter import *

"""
All GUI items are setup here to be used by the main launcher
"""


class Items:
    def __init__(self, main_ui):
        """
        Initialise tkinter variables and set up labels and buttons for the GUI.
        """
        self.items_side = "top"
        self.subitems_side = "left"

        self.branch_shortenby = tk.IntVar()
        self.branch_angle = tk.IntVar()
        self.branch_length = tk.IntVar()
        self.branch_min = tk.IntVar()
        self.fibo_maxmoves = tk.IntVar()
        self.honey_size = tk.IntVar()
        self.honey_circles = tk.IntVar()
        self.htree_fractal = tk.IntVar()
        self.koch_iterations = tk.IntVar()
        self.koch_length = tk.IntVar()
        self.koch_angle = tk.IntVar()
        self.koch_short_factor = tk.IntVar()
        self.koch_loops = tk.IntVar()
        self.koch_langle = tk.IntVar()
        self.carp_box_size = tk.IntVar()
        self.carp_box_depth = tk.IntVar()
        self.striangle_depth = tk.IntVar()
        self.snow_size = tk.IntVar()
        self.star_size = tk.IntVar()
        self.star_divider = tk.IntVar()
        self.star_root_length = tk.IntVar()

        self.selected_theme = tk.StringVar()

        """
        Screen controls.
        """

        self.screen_labelframe = ttk.LabelFrame(main_ui.master, text="Screen Controls")
        self.screen_labelframe.pack(side=self.items_side, fill="both", expand="yes")

        self.turtle_count_label = ttk.Label(self.screen_labelframe)
        self.turtle_count_label.pack(side=self.subitems_side)

        # todo: figure out a way for a progress bar to move independently of the turtles
        # self.render_progress = ttk.Progressbar(self.screen_labelframe, orient=HORIZONTAL, length=100, mode='determinate')
        # self.render_progress.pack()

        self.button_draw = ttk.Button(self.screen_labelframe, text="Draw", command=main_ui.draw_sequence)
        self.button_draw.pack(side=self.subitems_side)

        self.clear_button = ttk.Button(self.screen_labelframe, text="Clear", command=main_ui.clear_screen)
        self.clear_button.pack(side=self.subitems_side)

        """
        Turtle controls.
        """

        self.turtles_labelframe = ttk.LabelFrame(main_ui.master, text="turtles")
        self.turtles_labelframe.pack(side=self.items_side, fill="both", expand="yes")

        """
        Branch controls.
        """

        self.branch_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.branch_labelframe.pack(side=self.items_side)

        self.branch_button = ttk.Button(self.branch_labelframe, command=main_ui.add_branch)
        self.branch_button.pack(side=self.subitems_side)

        self.sub_1_branch_labelframe = ttk.LabelFrame(self.branch_labelframe)
        self.sub_1_branch_labelframe.pack(side="top")

        self.branch_shortenby_label = ttk.Label(self.sub_1_branch_labelframe, text="Shorten by:")
        self.branch_shortenby_label.pack(side=self.subitems_side)

        self.branch_shortenby_text_entry = ttk.Entry(self.sub_1_branch_labelframe, textvariable=self.branch_shortenby)
        self.branch_shortenby_text_entry.pack(side=self.subitems_side)

        self.branch_angle_label = ttk.Label(self.sub_1_branch_labelframe, text="Angle:")
        self.branch_angle_label.pack(side=self.subitems_side)

        self.branch_angle_text_entry = ttk.Entry(self.sub_1_branch_labelframe, textvariable=self.branch_angle)
        self.branch_angle_text_entry.pack(side=self.subitems_side)

        self.sub_2_branch_labelframe = ttk.LabelFrame(self.branch_labelframe)
        self.sub_2_branch_labelframe.pack(side="bottom")

        self.branch_angle_label = ttk.Label(self.sub_2_branch_labelframe, text="Length:")
        self.branch_angle_label.pack(side=self.subitems_side)

        self.branch_length_text_entry = ttk.Entry(self.sub_2_branch_labelframe, textvariable=self.branch_length)
        self.branch_length_text_entry.pack(side=self.subitems_side)

        self.branch_minbranch_label = ttk.Label(self.sub_2_branch_labelframe, text="Min branch:")
        self.branch_minbranch_label.pack(side=self.subitems_side)

        self.branch_minbranch_text_entry = ttk.Entry(self.sub_2_branch_labelframe, textvariable=self.branch_min)
        self.branch_minbranch_text_entry.pack(side=self.subitems_side)

        """
        Fibonacci controls.
        """

        self.fibo_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.fibo_labelframe.pack(side=self.items_side)

        self.fibo_button = ttk.Button(self.fibo_labelframe, command=main_ui.add_fibonacci)
        self.fibo_button.pack(side=self.subitems_side)

        self.fibo_maxmoves_label = ttk.Label(self.fibo_labelframe, text="Max moves:")
        self.fibo_maxmoves_label.pack(side=self.subitems_side)

        self.fibo_maxmoves_text_entry = ttk.Entry(self.fibo_labelframe, textvariable=self.fibo_maxmoves)
        self.fibo_maxmoves_text_entry.pack(side=self.subitems_side)

        """
        Honeycomb controls.
        """

        self.honey_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.honey_labelframe.pack(side=self.items_side)

        self.honey_button = ttk.Button(self.honey_labelframe, command=main_ui.add_honeycomb)
        self.honey_button.pack(side=self.subitems_side)

        self.honey_size_label = ttk.Label(self.honey_labelframe, text="Size:")
        self.honey_size_label.pack(side=self.subitems_side)

        self.honey_size_text_entry = ttk.Entry(self.honey_labelframe, textvariable=self.honey_size)
        self.honey_size_text_entry.pack(side=self.subitems_side)

        self.honey_circles_label = ttk.Label(self.honey_labelframe, text="Circles:")
        self.honey_circles_label.pack(side=self.subitems_side)

        self.honey_circles_text_entry = ttk.Entry(self.honey_labelframe, textvariable=self.honey_circles)
        self.honey_circles_text_entry.pack(side=self.subitems_side)

        """
        H-Tree controls.
        """

        self.htree_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.htree_labelframe.pack(side=self.items_side)

        self.h_button = ttk.Button(self.htree_labelframe, command=main_ui.add_htree)
        self.h_button.pack(side=self.subitems_side)

        self.htree_depth_label = ttk.Label(self.htree_labelframe, text="Depth:")
        self.htree_depth_label.pack(side=self.subitems_side)

        self.htree_depth_text_entry = ttk.Entry(self.htree_labelframe, textvariable=self.htree_fractal)
        self.htree_depth_text_entry.pack(side=self.subitems_side)

        """
        Koch controls.
        """

        self.koch_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.koch_labelframe.pack(side=self.items_side)

        self.koch_button = ttk.Button(self.koch_labelframe, command=main_ui.add_koch)
        self.koch_button.pack(side=self.subitems_side)

        self.sub_1_koch_labelframe = ttk.LabelFrame(self.koch_labelframe)
        self.sub_1_koch_labelframe.pack(side="top")

        self.koch_iterations_label = ttk.Label(self.sub_1_koch_labelframe, text="Iterations:")
        self.koch_iterations_label.pack(side=self.subitems_side)

        self.koch_iterations_text_entry = ttk.Entry(self.sub_1_koch_labelframe, textvariable=self.koch_iterations)
        self.koch_iterations_text_entry.pack(side=self.subitems_side)

        self.koch_length_label = ttk.Label(self.sub_1_koch_labelframe, text="Length:")
        self.koch_length_label.pack(side=self.subitems_side)

        self.koch_length_text_entry = ttk.Entry(self.sub_1_koch_labelframe, textvariable=self.koch_length)
        self.koch_length_text_entry.pack(side=self.subitems_side)

        self.sub_2_koch_labelframe = ttk.LabelFrame(self.koch_labelframe)
        self.sub_2_koch_labelframe.pack(side="bottom")

        self.koch_angle_label = ttk.Label(self.sub_2_koch_labelframe, text="Angle:")
        self.koch_angle_label.pack(side=self.subitems_side)

        self.koch_angle_text_entry = ttk.Entry(self.sub_2_koch_labelframe, textvariable=self.koch_angle)
        self.koch_angle_text_entry.pack(side=self.subitems_side)

        self.koch_short_factor_label = ttk.Label(self.sub_2_koch_labelframe, text="Shorten factor:")
        self.koch_short_factor_label.pack(side=self.subitems_side)

        self.koch_short_factor_text_entry = ttk.Entry(self.sub_2_koch_labelframe, textvariable=self.koch_short_factor)
        self.koch_short_factor_text_entry.pack(side=self.subitems_side)

        self.koch_loops_label = ttk.Label(self.sub_2_koch_labelframe, text="Loops:")
        self.koch_loops_label.pack(side=self.subitems_side)

        self.koch_loops_text_entry = ttk.Entry(self.sub_2_koch_labelframe, textvariable=self.koch_loops)
        self.koch_loops_text_entry.pack(side=self.subitems_side)

        self.sub_3_koch_labelframe = ttk.LabelFrame(self.koch_labelframe)
        self.sub_3_koch_labelframe.pack(side="bottom")

        self.koch_langle_label = ttk.Label(self.sub_3_koch_labelframe, text="Last angle:")
        self.koch_langle_label.pack(side=self.subitems_side)

        self.koch_langle_text_entry = ttk.Entry(self.sub_3_koch_labelframe, textvariable=self.koch_langle)
        self.koch_langle_text_entry.pack(side=self.subitems_side)

        """
        Sierpiński Carpet controls.
        """

        self.carp_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.carp_labelframe.pack(side=self.items_side)

        self.carp_button = ttk.Button(self.carp_labelframe, command=main_ui.add_scarpet)
        self.carp_button.pack(side=self.subitems_side)

        self.carp_size_label = ttk.Label(self.carp_labelframe, text="Size:")
        self.carp_size_label.pack(side=self.subitems_side)

        self.carp_size_text_entry = ttk.Entry(self.carp_labelframe, textvariable=self.carp_box_size)
        self.carp_size_text_entry.pack(side=self.subitems_side)

        self.carp_depth_label = ttk.Label(self.carp_labelframe, text="Depth:")
        self.carp_depth_label.pack(side=self.subitems_side)

        self.carp_depth_text_entry = ttk.Entry(self.carp_labelframe, textvariable=self.carp_box_depth)
        self.carp_depth_text_entry.pack(side=self.subitems_side)

        """
        Sierpiński Triangle controls.
        """

        self.tri_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.tri_labelframe.pack(side=self.items_side)

        self.tri_button = ttk.Button(self.tri_labelframe, command=main_ui.add_striangle)
        self.tri_button.pack(side=self.subitems_side)

        self.striangle_depth_label = ttk.Label(self.tri_labelframe, text="Depth:")
        self.striangle_depth_label.pack(side=self.subitems_side)

        self.striangle_depth_text_entry = ttk.Entry(self.tri_labelframe, textvariable=self.striangle_depth)
        self.striangle_depth_text_entry.pack(side=self.subitems_side)

        """
        Snowflake controls.
        """

        self.snow_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.snow_labelframe.pack(side=self.items_side)

        self.snow_button = ttk.Button(self.snow_labelframe, command=main_ui.add_snowflake)
        self.snow_button.pack(side=self.subitems_side)

        self.snow_size_label = ttk.Label(self.snow_labelframe, text="Size:")
        self.snow_size_label.pack(side=self.subitems_side)

        self.snow_size_text_entry = ttk.Entry(self.snow_labelframe, textvariable=self.snow_size)
        self.snow_size_text_entry.pack(side=self.subitems_side)

        """
        Star Triangle controls.
        """

        self.star_labelframe = ttk.LabelFrame(self.turtles_labelframe)
        self.star_labelframe.pack(side=self.items_side)

        self.button_star = ttk.Button(self.star_labelframe, command=main_ui.add_star)
        self.button_star.pack(side=self.subitems_side)

        self.star_size_label = ttk.Label(self.star_labelframe, text="Size:")
        self.star_size_label.pack(side=self.subitems_side)

        self.star_size_text_entry = ttk.Entry(self.star_labelframe, textvariable=self.star_size)
        self.star_size_text_entry.pack(side=self.subitems_side)

        self.star_size_divider_label = ttk.Label(self.star_labelframe, text="Divider:")
        self.star_size_divider_label.pack(side=self.subitems_side)

        self.star_size_divider_text_entry = ttk.Entry(self.star_labelframe, textvariable=self.star_divider)
        self.star_size_divider_text_entry.pack(side=self.subitems_side)

        self.star_root_length_label = ttk.Label(self.star_labelframe, text="Length:")
        self.star_root_length_label.pack(side=self.subitems_side)

        self.star_root_length_text_entry = ttk.Entry(self.star_labelframe, textvariable=self.star_root_length)
        self.star_root_length_text_entry.pack(side=self.subitems_side)

        """
        Canvas controls.
        """

        self.turtle_config_labelframe = ttk.LabelFrame(main_ui.master, text="Canvas Config")
        self.turtle_config_labelframe.pack(side=self.items_side, fill="both", expand="yes")

        self.button_queue = ttk.Button(self.turtle_config_labelframe, command=main_ui.queue_setter)
        self.button_queue.pack(side=self.subitems_side)

        self.button_rand = ttk.Button(self.turtle_config_labelframe, command=main_ui.random_position_setter)
        self.button_rand.pack(side=self.subitems_side)

        self.button_live = ttk.Button(self.turtle_config_labelframe, command=main_ui.live_drawing_setter)
        self.button_live.pack(side=self.subitems_side)

        self.button_random_bg = ttk.Button(self.turtle_config_labelframe, text="Random Background",
                                           command=main_ui.random_background)
        self.button_random_bg.pack(side=self.subitems_side)

        """
        Window controls.
        """

        self.theme_frame = ttk.LabelFrame(main_ui.master, text='GUI Theme')
        self.theme_frame.pack(side=self.items_side, expand="yes")

        self.theme_labelframe = ttk.LabelFrame(main_ui.master, text="GUI Theme")
        self.theme_labelframe.pack(side=self.subitems_side, fill="both", expand="yes")

        self.theme_options = []

        for theme_name in main_ui.style.theme_names():
            self.theme_options.append(theme_name)

        self.variable = StringVar(self.theme_labelframe)
        self.variable.set(self.theme_options[0])  # default value

        self.theme_option_drop = ttk.OptionMenu(self.theme_labelframe, self.variable, *self.theme_options)
        self.theme_option_drop.pack(side=self.subitems_side)

        self.theme_apply_button = ttk.Button(self.theme_labelframe, text="Apply", command=main_ui.change_theme)
        self.theme_apply_button.pack(side=self.subitems_side)

        self.button_exit = ttk.Button(main_ui.master, text="Exit", command=main_ui.exit)
        self.button_exit.pack(side=self.subitems_side)
