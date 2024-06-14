# Test GUI Class
# By Drew Wynne
# Commenced 14/06/2024

# To Do:
# Add Start Button
# Add Question Text
# Add
# Link to Game Later

from tkinter import *
from tkinter import ttk

from UI_Components.GameWindow import GameWindow
from UI_Components.MyWindow import MyWindow
from UI_Components.StatsWindow import StatsWindow


class StartWindow(MyWindow):
    """ Start Window Class"""
    # Constants:

    # Variables:

    # Objects:

    # UI Components:
    outer_frame: ttk.Frame  # Outer Frame
    start_button: ttk.Button  # Start Button
    show_stats_var: BooleanVar  # Show Stats Variable (Boolean)
    show_stats: ttk.Checkbutton  # show stats check button
    difficulty_selector_label: ttk.Label  # Difficulty Selector Text Label
    difficulty_selector_inp: ttk.Spinbox  # Difficulty selector spin box
    difficulty_selector_var: IntVar  # Value of Difficulty Selector
    round_number_label: ttk.Label  # Round Number Label
    round_number_var: StringVar  # Round Number String Variable

    def __init__(self):  #
        """ Start Window Constructor """
        super().__init__('Summer')
        # self.root.geometry("300x500+0+0")  # Small Window
        # Init Variables

        # Init Objects:

        # Init UI Components:
        # Root
        self.root.resizable(False, False)
        self.style.map('StartFrame.TFrame', foreground=[('active', 'cyan')])
        self.outer_frame = ttk.Frame(self.root, padding=10, style='StartFrame.TFrame')  # Outer Frame
        # Difficulty Selector
        self.difficulty_selector_var = IntVar(value=5)  # Set Default Value for difficulty selector
        self.difficulty_selector_label = ttk.Label(self.outer_frame,
                                                   text="Select Difficulty (1 to 10)",
                                                   font=self.custom_font)
        self.difficulty_selector_inp = ttk.Spinbox(self.outer_frame, from_=1, to=10, width=5,
                                                   textvariable=self.difficulty_selector_var,
                                                   font=self.custom_font)
        self.show_stats_var = BooleanVar(value=False)
        self.show_stats = ttk.Checkbutton(self.outer_frame,
                                          text="Show Stats",
                                          )  # Show Stats While Playing
        # Start Button
        self.start_button = ttk.Button(self.outer_frame,
                                       text="Start",
                                       command=self.on_press_start,
                                       style='Regular.TButton')
        self.round_number_var = StringVar(value="Round 1")  # Set Default Value for Round Number Text
        self.round_number_label = ttk.Label(self.outer_frame,
                                            textvariable=self.round_number_var,
                                            font=self.custom_font)  #
        # Pack UI Components to Grid:
        self.outer_frame.pack(side='top', fill='both', expand=True)  # Pack Outer Frame to Grid
        # Pack difficulty Selector Label to Grid
        self.difficulty_selector_label.grid(column=0, row=0,  sticky="EW", ipadx=5, ipady=5)
        # Pack difficulty Selector spinbox to Grid
        self.difficulty_selector_inp.grid(column=0, row=1,  sticky="EW", ipadx=5, ipady=5)
        # Pack Show Stats Checkbox to Grid
        self.show_stats.grid(column=0, row=2, sticky="EW", ipadx=5, ipady=5)
        self.start_button.grid(column=0, row=3, sticky="EW", ipadx=5, ipady=5)  # Pack Start Button to Grid
        # Pack Round Number Label to Grid
        self.round_number_label.grid(column=0, row=4, sticky="EW", ipadx=5, ipady=5)

    def on_press_start(self):
        """ When Start Button is Pressed """
        print("Start Button Pressed")

        game_window = GameWindow(self.root, "Summer Game Window")
        game_window.display()

        if self.show_stats_var.get():
            stats_window = StatsWindow(self.root, "Summer Stats Window")
            stats_window.display()


    def open_main_window(self):
        """ Opens Main Window """
        pass

    def open_stats_window(self):
        """ Opens Stats Window """
        pass


if __name__ == '__main__':  # Test Code
    print("Testing Start Window")
    print()

    start_window = StartWindow()
    start_window.display()
