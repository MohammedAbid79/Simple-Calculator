import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    num1 = number1.get()
    num2 = number2.get()
    operator = operation.get()
    
    try:
        num1 = float(num1)
        if operator != "sqrt":
            num2 = float(num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
    elif operator == 'sqrt':
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            messagebox.showerror("Error", "Cannot take the square root of a negative number")
            return
    else:
        messagebox.showerror("Error", "Invalid operator. Please select a valid operator.")
        return

    result_label.config(text = str(result))

root = tk.Tk()

number1 = tk.StringVar()
number2 = tk.StringVar()
operation = tk.StringVar()

tk.Label(root, text="Number 1").pack()
tk.Entry(root, textvariable=number1).pack()
tk.Label(root, text="Operation (+, -, *, /, sqrt)").pack()
tk.OptionMenu(root, operation, "+", "-", "*", "/", "sqrt").pack()
tk.Label(root, text="Number 2 (Not required for sqrt)").pack()
tk.Entry(root, textvariable=number2).pack()
tk.Button(root, text="Calculate", command=calculate).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
