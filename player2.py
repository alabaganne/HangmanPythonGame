import tkinter as tk
from helpers import *
from hangman_drawings import HANGMAN_DRAWINGS

class Player2:
    def __init__(self, window_ref, valid_word):
        self.window = window_ref
        self.word = valid_word
        self.attempts = 7
        self.hidden_word = "_" * len(self.word)
        self.guessed_chars = []

        # prepare UI for player 2
        self.welcome = tk.Label(self.window, text="Hey Player 2, It's Your Turn Now!")
        self.label = tk.Label(self.window, text="Guess a character from the word:")
        self.input = tk.Entry(self.window)
        self.button = tk.Button(self.window, text="Guess", command=self.guess)
        self.drawing = tk.Label(self.window, text=HANGMAN_PICS[7 - self.attempts])
        self.hidden_word_label = tk.Label(self.window, text=self.hidden_word)
        self.attempts_label = tk.Label(self.window, text="{} attempts left!".format(self.attempts))
        self.validation_label = tk.Label(self.window, text="", fg="red")
        self.welcome.pack()
        self.label.pack()
        self.input.pack()
        self.button.pack(pady=(10, 0))
        self.drawing.pack()
        self.hidden_word_label.pack()
        self.attempts_label.pack()
        self.validation_label.pack()

        # messages
        self.lost_message = tk.Label(self.window, text="Sorry! you lost.", fg="red")
        self.win_message = tk.Label(self.window, text="Bingooo! You found the right word!", fg="green")

    def guess(self):
        player_input = self.input.get().strip().upper()
        self.validation_label.config(text="")  # hide validation message

        clear_input(self.input)

        if len(player_input) == 0:
            self.validation_label.config(text="This field is required")
            return
        elif len(player_input) > 1:
            self.validation_label.config(text="This field must be 1 character long")
            return

        if player_input in self.guessed_chars:
            self.validation_label.config(text="You already entered this letter")
            return

        self.guessed_chars.append(player_input)

        if player_input in self.word:
            print("right")
            for i in range(len(self.word)):
                if self.word[i] == player_input:
                    self.hidden_word = update_string_char(self.hidden_word, i, player_input)
                    self.hidden_word_label.config(text=self.hidden_word)
        else:
            self.attempts = self.attempts - 1
            if self.attempts > 0:
                self.attempts_label.config(text="You have " + str(self.attempts) + " left!")
                self.drawing.config(text=HANGMAN_PICS[7 - self.attempts])
            print("wrong")

        if "_" not in self.hidden_word or self.attempts == 0:
            self.welcome.destroy()
            self.label.destroy()
            self.input.destroy()
            self.button.destroy()
            self.drawing.destroy()
            self.hidden_word_label.destroy()
            self.attempts_label.destroy()
            self.validation_label.destroy()
            if "_" not in self.hidden_word:
                self.win_message.pack()
            else:
                self.lost_message.pack()

