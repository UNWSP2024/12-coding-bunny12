"""
Author: Abrielle Nyei
Date: 2026-04-23
Title: Joe's Automotive Service Calculator
Description: Calculates total cost of selected car services.
"""

import tkinter as tk

def calculate_total():
    total = 0

    if oil_var.get(): total += 30
    if lube_var.get(): total += 20
    if radiator_var.get(): total += 40
    if transmission_var.get(): total += 100
    if inspection_var.get(): total += 35
    if muffler_var.get(): total += 200
    if tire_var.get(): total += 20

    result_label.config(text=f"Total Charges: ${total:.2f}")

root = tk.Tk()
root.title("Joe's Automotive")

# Variables
oil_var = tk.IntVar()
lube_var = tk.IntVar()
radiator_var = tk.IntVar()
transmission_var = tk.IntVar()
inspection_var = tk.IntVar()
muffler_var = tk.IntVar()
tire_var = tk.IntVar()

# Checkbuttons
tk.Checkbutton(root, text="Oil Change ($30)", variable=oil_var).pack(anchor='w')
tk.Checkbutton(root, text="Lube Job ($20)", variable=lube_var).pack(anchor='w')
tk.Checkbutton(root, text="Radiator Flush ($40)", variable=radiator_var).pack(anchor='w')
tk.Checkbutton(root, text="Transmission Fluid ($100)", variable=transmission_var).pack(anchor='w')
tk.Checkbutton(root, text="Inspection ($35)", variable=inspection_var).pack(anchor='w')
tk.Checkbutton(root, text="Muffler Replacement ($200)", variable=muffler_var).pack(anchor='w')
tk.Checkbutton(root, text="Tire Rotation ($20)", variable=tire_var).pack(anchor='w')

# Button
tk.Button(root, text="Calculate Total", command=calculate_total).pack()

# Result
result_label = tk.Label(root, text="Total Charges: $0.00")
result_label.pack()

root.mainloop()