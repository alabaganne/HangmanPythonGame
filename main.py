import tkinter as tk
import tkinter.font as font
from player1 import Player1

if __name__ == "__main__":
    window = tk.Tk()

    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family="Fira Code", size=12, weight="normal")
    window.option_add("*Font", default_font)

    window.title("Hangman Game")
    frame = tk.Frame(window, relief="sunken")
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    player1 = Player1(frame)
    word = player1.get_word()

    window.mainloop()
