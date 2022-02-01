import tkinter as tk
from player2 import Player2
from helpers import clear_input

class Player1:
    def __init__(self, window_ref):
        self.window = window_ref
        self.word = ''

        self.welcome = tk.Label(self.window, text="Welcome Player 1")
        self.label = tk.Label(self.window, text="Pick A Word To Be Guessed (Min length: 4)")
        self.input = tk.Entry(self.window)
        self.button = tk.Button(self.window, text="Pick", command=self.pick_word)
        self.welcome.pack()
        self.label.pack()
        self.input.pack()
        self.button.pack(pady=(8, 0))
        self.validation_label = tk.Label(self.window, text="", fg="red")
        self.validation_label.pack()

    def pick_word(self):
        self.word = self.input.get().strip().upper()
        length = len(self.word)
        self.validation_label.config(text="")

        clear_input(self.input)

        # validation
        if length == 0:
            self.validation_label.config(text="This field is required")
        elif length < 4:
            self.validation_label.config(text="This field must be at least 4 characters long")
        elif " " in self.word:
            self.validation_label.config(text="Spaces are not allowed")
        else:
            self.welcome.destroy()
            self.label.destroy()
            self.input.destroy()
            self.button.destroy()
            self.validation_label.destroy()
            # player 2 turn when the player 1's submitted word is valid
            Player2(self.window, self.get_word())

    def get_word(self):
        return self.word
