


import tkinter as tk
from tkinter import ttk #themed tkinter: provides improved widgets and styling options

# Main window
window = tk.Tk()
window.title("Statistical Frequency Table")
window.geometry("900x600") #WidthxHeight
window.configure(bg="white")

# Colors
dark_blue = "#142D4E"
white = "#FFFFFF"

# Title
title = tk.Label(
    window,
    text="Statistical Frequency Table",
    font=("Arial", 26, "bold"),
    bg=dark_blue,
    fg=white,
    pady=20                             # pady : vertical padding / padx : horizontal padding
) 
title.pack(fill="x") #pack() to arrange and display widets inside the window


# Buttons
buttons_frame = tk.Frame(window, bg="white")
buttons_frame.pack(pady=25)

input_button = tk.Button(
    buttons_frame,
    text="Import Data",
    font=("Arial", 12, "bold"),
    bg=dark_blue,
    fg=white,
    width=18,
    pady=8
)
input_button.pack(side="left", padx=15)

output_button = tk.Button(
    buttons_frame,
    text="Manual Input",
    font=("Arial", 12, "bold"),
    bg=dark_blue,
    fg=white,
    width=18,
    pady=8
)
output_button.pack(side="left", padx=15)

# Table
columns = ("Xi", "fi", "Fi", "fr", "Fri", "Percentage")

table = ttk.Treeview(
    window,
    columns=columns,
    show="headings",
    height=12
)

for column in columns:
    table.heading(column, text=column)
    table.column(column, anchor="center", width=120)

table.pack(pady=20, padx=30, fill="x")
                             #the fill option makes a widget expend to fill the avaible space in acpecified direction 
# Table style
style = ttk.Style()
style.configure(
    "Treeview",
    background="white",
    foreground="black",
    font=("Arial", 11),
    rowheight=30
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 11, "bold")
)

window.mainloop()





