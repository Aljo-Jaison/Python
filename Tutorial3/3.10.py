import tkinter as tk
from tkinter import messagebox

def Distance_Calculator():
    try:
        h = float(entry_height.get())
        b = float(entry_bounce.get())
        n = int(entry_bounces.get())
        d = h
        for _ in range(n):
            h *= b
            d += 2 * h
        entry_distance.delete(0, tk.END)
        entry_distance.insert(0, f"{d:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid num.")

window = tk.Tk()
window.title("Bouncy Ball Distance Calculator")

label_height = tk.Label(window, text="Initial Height:")
label_height.grid(row=0, column=0)
entry_height = tk.Entry(window)
entry_height.grid(row=0, column=1)

label_bounce = tk.Label(window, text="Bounciness Index:")
label_bounce.grid(row=1, column=0)
entry_bounce = tk.Entry(window)
entry_bounce.grid(row=1, column=1)

label_bounces = tk.Label(window, text="Number of Bounces:")
label_bounces.grid(row=2, column=0)
entry_bounces = tk.Entry(window)
entry_bounces.grid(row=2, column=1)

label_distance = tk.Label(window, text="Total Distance:")
label_distance.grid(row=3, column=0)
entry_distance = tk.Entry(window)
entry_distance.grid(row=3, column=1)

button_compute = tk.Button(window, text="Compute Distance", command=Distance_Calculator)
button_compute.grid(row=4, column=0, columnspan=2)

window.mainloop()
