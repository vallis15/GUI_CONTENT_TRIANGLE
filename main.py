import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        a = float(side_a_entry.get())
        b = float(side_b_entry.get())
        c = float(side_c_entry.get())
        s = (a + b + c) / 2
        area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
        messagebox.showinfo("Calculate the content", f"Content of a triangle is : {area:.2f} square units.")
    except ValueError:
        messagebox.showerror("Error", "Enter valid valuse for all sides of the triangle!")

root = tk.Tk()
root.title("Calculate the content of a triangle")

side_a_label = tk.Label(root, text="Side a:")
side_a_entry = tk.Entry(root)

side_b_label = tk.Label(root, text="Side b:")
side_b_entry = tk.Entry(root)

side_c_label = tk.Label(root, text="Side c:")
side_c_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Result", command=calculate_area)

side_a_label.grid(row=0, column=0)
side_a_entry.grid(row=0, column=1)

side_b_label.grid(row=1, column=0)
side_b_entry.grid(row=1, column=1)

side_c_label.grid(row=2, column=0)
side_c_entry.grid(row=2, column=1)

calculate_button.grid(row=3, column=1)

root.mainloop()
