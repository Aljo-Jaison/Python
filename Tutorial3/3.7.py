import tkinter as tk
from tkinter import messagebox
import math

def Sqrt_computer():
    try:
        num = float(entry_number.get())
        if num < 0:
            raise ValueError("Cannot compute sqrt of a -ve number.")
        sqrt_result = math.sqrt(num)
        entry_sqrt.delete(0, tk.END)
        entry_sqrt.insert(0, f"{sqrt_result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid i/p", "Please enter a valid non -ve number.")
window = tk.Tk()
window.title("Sqrt Calc")

label_number = tk.Label(window, text="Enter the Number:")
label_number.grid(row=0, column=0)
entry_number = tk.Entry(window)
entry_number.grid(row=0, column=1)

label_sqrt = tk.Label(window, text="sqrt:")
label_sqrt.grid(row=1, column=0)
entry_sqrt = tk.Entry(window)
entry_sqrt.grid(row=1, column=1)

button_sqrt = tk.Button(window, text="Compute sqrt", command=Sqrt_computer)
button_sqrt.grid(row=2, column=0, columnspan=2)

window.mainloop()
