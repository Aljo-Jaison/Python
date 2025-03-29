import tkinter as tk
from tkinter import messagebox
import random

def Guess_game():
    global guess_count
    try:
        user_guess = int(entry_guess.get())
        guess_count += 1
        if user_guess < target_number:
            label_result.config(text="Too small, try again.")
        elif user_guess > target_number:
            label_result.config(text="Too large, try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it right in {guess_count} attempts!")
            game_reseter()
    except ValueError:
        messagebox.showerror("Invalid i/p", "Please enter a valid int.")

def game_reseter():
    global target_number, guess_count
    target_number = random.randint(1, 100)
    guess_count = 0
    label_result.config(text="")
    entry_guess.delete(0, tk.END)

window = tk.Tk()
window.title("Guess the num game")

label_guess = tk.Label(window, text="Guess a num (1-100):")
label_guess.grid(row=0, column=0)
entry_guess = tk.Entry(window)
entry_guess.grid(row=0, column=1)

button_guess = tk.Button(window, text="Submit your Guess", command=Guess_game)
button_guess.grid(row=1, column=0, columnspan=2)

label_result = tk.Label(window, text="", font=("Arial", 10))
label_result.grid(row=2, column=0, columnspan=2)

button_reset = tk.Button(window, text="Reset the Game", command=game_reseter)
button_reset.grid(row=3, column=0, columnspan=2)

target_number = random.randint(1, 100)
guess_count = 0

window.mainloop()