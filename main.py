import csv
import tkinter as tk
from tkinter import ttk

CAR_STATUS_INDEX = 3


def users():
    rows = []

    with open("users.csv", 'r') as file:
        csvreader = csv.reader(file)

        # Skip headers
        next(csv_reader)
        for row in csvreader:
            rows.append(row)

    return rows


def cars():
    rows = []

    with open("cars.csv", 'r') as file:
        csv_reader = csv.reader(file)

        # Skip headers
        next(csv_reader)

        for row in csv_reader:
            rows.append(row)

    return rows


def rentedCars():
    return filter(getRentedCars, cars())


def getRentedCars(carRow):
    carStatus = carRow[CAR_STATUS_INDEX]

    if carStatus == "Rented":
        return True
    else:
        return False


def rentedCarsCount():
    return len(list(rentedCars()))


def main():
    # Create window
    root = tk.Tk()

    # Provide Window Size
    root.geometry("750x750")

    # App Title
    tk.Label(text="Car Rental Admin Dashboard",
             height=2,
             width=30,
             font=("Courier", 25)).pack()

    # Rented Cars Section
    tk.Label(text="Rented Cars").pack()
    tk.Label(text="{rentedCarsCount}".format(
        rentedCarsCount=rentedCarsCount())).pack()

    # Run app
    root.mainloop()


if __name__ == "__main__":
    main()
