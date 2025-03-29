import tkinter as tk

def Upper():
    text = input_entry.get()
    result_label.config(text=text.upper())

root = tk.Tk()
root.title("Convert to UpperCase")


tk.Label(root, text="Enter the Text to be converted:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=30)
input_entry.grid(row=0, column=1, padx=10, pady=10)
convert_btn = tk.Button(root, text="Convert", command=Upper)
convert_btn.grid(row=1, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="Result: ", font=("Montserrat", 12, "bold"))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
