"""
Author: Abrielle Nyei
Date: 2026-04-23
Title: MPG Calculator GUI
Description: Calculates miles per gallon based on user input.
"""

import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        miles = float(entry_miles.get())
        gallons = float(entry_gallons.get())

        if gallons == 0:
            messagebox.showerror("Error", "Gallons cannot be zero.")
            return

        mpg = miles / gallons
        result_label.config(text=f"MPG: {mpg:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Window setup
root = tk.Tk()
root.title("MPG Calculator")

# Input fields
tk.Label(root, text="Miles driven:").grid(row=0, column=0)
entry_miles = tk.Entry(root)
entry_miles.grid(row=0, column=1)

tk.Label(root, text="Gallons used:").grid(row=1, column=0)
entry_gallons = tk.Entry(root)
entry_gallons.grid(row=1, column=1)

# Button
tk.Button(root, text="Calculate MPG", command=calculate_mpg).grid(row=2, columnspan=2)

# Result
result_label = tk.Label(root, text="MPG: ")
result_label.grid(row=3, columnspan=2)

root.mainloop()