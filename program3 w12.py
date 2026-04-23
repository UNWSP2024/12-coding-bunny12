"""
Author: Abrielle Nyei
Date: 2026-04-23
Title: Long-Distance Call Calculator
Description: Calculates cost of a phone call based on time category.
"""

import tkinter as tk
from tkinter import messagebox

def calculate_cost():
    try:
        minutes = float(entry_minutes.get())
        rate = rate_var.get()

        if rate == "":
            messagebox.showerror("Error", "Please select a rate category.")
            return

        cost = minutes * float(rate)
        messagebox.showinfo("Call Cost", f"Total charge: ${cost:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of minutes.")

root = tk.Tk()
root.title("Long-Distance Call Calculator")

# Rate selection
rate_var = tk.StringVar()

tk.Label(root, text="Select Rate Category:").pack(anchor='w')

tk.Radiobutton(root, text="Daytime ($0.02/min)", variable=rate_var, value="0.02").pack(anchor='w')
tk.Radiobutton(root, text="Evening ($0.12/min)", variable=rate_var, value="0.12").pack(anchor='w')
tk.Radiobutton(root, text="Off-Peak ($0.05/min)", variable=rate_var, value="0.05").pack(anchor='w')

# Minutes input
tk.Label(root, text="Minutes:").pack()
entry_minutes = tk.Entry(root)
entry_minutes.pack()

# Button
tk.Button(root, text="Calculate Cost", command=calculate_cost).pack()

root.mainloop()