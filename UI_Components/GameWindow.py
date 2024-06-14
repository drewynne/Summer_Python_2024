from tkinter import *
from tkinter import ttk

from UI_Components.MyToplevel import MyToplevel


class GameWindow(MyToplevel):
    """ Game Window Class """
    # Constants:

    # Variables:

    # Objects:

    # UI Objects:
    outer_frame: ttk.Frame  # Outer Frame
    top_frame: ttk.Frame  # Top Frame
    centered_frame: ttk.Frame  # Centered Frame

    end_round_button: ttk.Button  # End Round Button
    question_number_var: StringVar  # Question Number Text String Variable
    question_number_text_label: ttk.Label  # Question Number Text Label
    round_number_var: StringVar  # Round Number Text String Variable
    round_number_text_label: ttk.Label  # Round Number Text Label

    question_text_var: StringVar  # Question Text String Variable
    question_text_label: ttk.Label  # Question Text Label
    answer_text_var: StringVar  # Answer Text String Variable
    answer_text_entry: ttk.Entry  # Answer Text input Box
    submit_button: ttk.Button  # Submit Button

    def __init__(self, main_window_root, title):
        """ Game Window Constructor """
        super().__init__(main_window_root, title)  # Overload Super Constructor
        self.root.geometry("1920x1080+0+0")  # Uses up full Laptop Screen

        # Initialize GUI Components
        self.outer_frame = ttk.Frame(self.root, padding=10)
        self.outer_frame.pack(side='top', fill='both', expand=True)
        self.top_frame = ttk.Frame(self.outer_frame, padding=10)
        self.centered_frame = ttk.Frame(self.outer_frame, padding=10)

        self.end_round_button = ttk.Button(self.top_frame,
                                           text="End Round",
                                           command=self.on_end_round,
                                           style='Regular.TButton')
        self.question_number_var = StringVar(value="Question 3 of 10")
        self.question_number_text_label = ttk.Label(self.top_frame, textvariable=self.question_number_var,
                                                    font=self.custom_font)
        self.round_number_var = StringVar(value="Round 4")
        self.round_number_text_label = ttk.Label(self.top_frame, textvariable=self.round_number_var,
                                                 font=self.custom_font)

        self.question_text_var = StringVar(value="10 + 5")
        self.question_text_label = ttk.Label(self.centered_frame, textvariable=self.question_text_var,
                                             font=self.custom_font)
        self.answer_text_var = StringVar(value="Answer")
        self.answer_text_entry = ttk.Entry(self.centered_frame, textvariable=self.answer_text_var,
                                           font=self.custom_font)
        self.submit_button = ttk.Button(self.centered_frame,
                                        text="Submit",
                                        command=self.on_submit,
                                        style='Accent.TButton')
        # Pack UI Components
        #self.outer_frame.grid()
        self.top_frame.grid(column=0, row=0, sticky="EW")
        self.centered_frame.place(in_=self.outer_frame, relx=0.5, rely=0.5, anchor='center')

        self.end_round_button.grid(column=0, row=0, ipadx=10, ipady=10)
        self.question_number_text_label.grid(column=1, row=0, ipadx=10, ipady=10)
        self.round_number_text_label.grid(column=2, row=0, ipadx=10, ipady=10)

        self.question_text_label.grid(column=0, row=0, ipadx=10, ipady=10)
        self.answer_text_entry.grid(column=0, row=1, ipadx=10, ipady=10)
        self.submit_button.grid(column=1, row=1, ipadx=10, ipady=10)

    def on_end_round(self):
        """ On End Round Button Pressed """
        self.root.destroy()

    def on_submit(self):
        """ On Submit Button Pressed """
        pass


if __name__ == '__main__':
    print("Testing Game Window")
    print()

    root = Tk()
    game_window = GameWindow(root, "Summer Game Window")
    game_window.display()
