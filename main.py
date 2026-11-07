import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog #ttk:themed tkinter: provides improved widgets and styling options
import csv

from frequency_functions import QualitativeData, QuantitativeData


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


#Buttons
buttons_frame = tk.Frame(window, bg="white")
buttons_frame.pack(pady=25)

# Display results in the table
def display_results(data, data_type):

    try:
        if data_type == "qualitative":
            dataset = QualitativeData(data)
            fi, fr, percentage = dataset.calculate_table()

        else:
            data = [float(x) for x in data]
            dataset = QuantitativeData(data)
            fi, Fi, fr, Fri, percentage = dataset.calculate_table()

        # Clear previous results
        for item in table.get_children():
            table.delete(item)

        # Insert new results
        for Xi in fi:
            if data_type == "qualitative":
                values = (
                    Xi, fi[Xi], "-", fr[Xi], "-", percentage[Xi]
                )
            else:
                values = (
                    Xi, fi[Xi], Fi[Xi], fr[Xi], Fri[Xi],
                    percentage[Xi]
                )

            table.insert("", "end", values=values)

    except (ValueError, TypeError, ZeroDivisionError) as error:
        messagebox.showerror("Error", str(error))


# Choose data type
def choose_data_type():

    choice = simpledialog.askstring(
        "Data Type",
        "Enter qualitative or quantitative:"
    )

    if choice is None:
        return None

    choice = choice.strip().lower()

    if choice not in ["qualitative", "quantitative"]:
        messagebox.showerror("Error", "Invalid data type")
        return None

    return choice


# Import CSV file
def import_data():

    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            data = []

            for row in reader:
                for value in row:
                    if value.strip():
                        data.append(value.strip())

        if not data:
            raise ValueError("The file is empty")

        data_type = choose_data_type()

        if data_type is not None:
            display_results(data, data_type)

    except (OSError, csv.Error, ValueError) as error:
        messagebox.showerror("File Error", str(error))


# Manual data input
def manual_input():

    data_text = simpledialog.askstring(
        "Manual Input",
        "Enter values separated by commas:"
    )

    if data_text is None:
        return

    data = [x.strip() for x in data_text.split(",") if x.strip()]

    if not data:
        messagebox.showerror("Error", "No data entered")
        return

    data_type = choose_data_type()

    if data_type is not None:
        display_results(data, data_type)


# Import Button
input_button = tk.Button(
    buttons_frame,
    text="Import Data",
    font=("Arial", 12, "bold"),
    bg=dark_blue,
    fg=white,
    width=18,
    pady=8,
    command=import_data
)
input_button.pack(side="left", padx=15)


# Manual Input Button
output_button = tk.Button(
    buttons_frame,
    text="Manual Input",
    font=("Arial", 12, "bold"),
    bg=dark_blue,
    fg=white,
    width=18,
    pady=8,
    command=manual_input
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