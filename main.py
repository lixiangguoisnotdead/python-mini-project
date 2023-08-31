# Import tkinter module
# Import csv module
import csv
import tkinter as tk
from tkinter import ttk


def users():
    rows = []

    with open("users.csv", 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            rows.append(row)

    return rows


def cars():
    rows = []

    with open("cars.csv", 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            rows.append(row)

    return rows


def main():
    # Create window
    root = tk.Tk()

    # Provide Window Size
    root.geometry("750x750")

    # App Title
    T = tk.Text(root, height=2, width=30, font=("Courier", 25))

    # Pack Tkinter elements
    T.pack()

    T.insert(tk.END, "Car Rental Admin Dashboard")

    # Run app
    root.mainloop()


if __name__ == "__main__":
    main()
