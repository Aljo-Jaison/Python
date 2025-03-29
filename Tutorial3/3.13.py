import tkinter as tk
from tkinter import messagebox
import math

def SqrtFinder():
    try:
        num = float(entry_number.get())
        if num < 0:
            raise ValueError("Cannot compute square root of a -ve number.")
        sqrt_result = math.sqrt(num)
        entry_sqrt.delete(0, tk.END)
        entry_sqrt.insert(0, f"{sqrt_result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid non -ve number.")

window = tk.Tk()
window.title("Square Root calc")

label_number = tk.Label(window, text="Enter the Num:")
label_number.grid(row=0, column=0)
entry_number = tk.Entry(window)
entry_number.grid(row=0, column=1)

label_sqrt = tk.Label(window, text="Sqrt :")
label_sqrt.grid(row=1, column=0)
entry_sqrt = tk.Entry(window)
entry_sqrt.grid(row=1, column=1)

button_compute = tk.Button(window, text="Compute sqrt", command=SqrtFinder)
button_compute.grid(row=2, column=0, columnspan=2)

window.mainloop()
