


import tkinter as tk
from math import sqrt,factorial

def clear():
    entry_result.delete(0, tk.END)

def backspace():
    current = entry_result.get()
    entry_result.delete(len(current) - 1)

def add_digit(digit):
    current = entry_result.get()
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, current + str(digit))

def add_point():
    current = entry_result.get()
    if '.' not in current:
        entry_result.insert(tk.END, '.')

def calculate_sqrt():
    try:
        value = float(entry_result.get())
        if value >= 0:
            result = sqrt(value)
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, str(result))
        else:
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, "Invalid input")
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Invalid input")
        
def calculate_factorial():
    try:
        value = int(entry_result.get())
        if value >= 0:
            result = factorial(value)
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, str(result))
        else:
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, "Invalid input")
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Invalid input")
        
def add_operator(operator):
    current = entry_result.get()
    if current and current[-1] not in ['+', '-', '*', '/']:
        entry_result.insert(tk.END, operator)
        
def calculate():
    try:
        expression = entry_result.get()
        result = eval(expression)
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, str(result))
    except:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error")
        
        
root = tk.Tk()
root.title("Calculator")

entry_result = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_fact = tk.Button(root, text="!", font=("Arial", 16), padx=20, pady=10, command=calculate_factorial)
btn_fact.grid(row=1, column=0, padx=5, pady=5)

btn_sqrt = tk.Button(root, text="√", font=("Arial", 16), padx=20, pady=10, command=calculate_sqrt)
btn_sqrt.grid(row=1, column=1, padx=5, pady=5)

btn_clear = tk.Button(root, text="C", font=("Arial", 16), padx=20, pady=10, command=clear)
btn_clear.grid(row=1, column=2, padx=5, pady=5)

btn_backspace = tk.Button(root, text="←", font=("Arial", 16), padx=20, pady=10, command=backspace)
btn_backspace.grid(row=1, column=3, padx=5, pady=5)

row_start = 4
for i in range(1, 10):
    btn = tk.Button(root, text=str(i), font=("Arial", 16), padx=20, pady=10, command=lambda digit=i: add_digit(digit))
    btn.grid(row=row_start - (i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)

btn_zero = tk.Button(root, text="0", font=("Arial", 16), padx=20, pady=10, command=lambda: add_digit(0))
btn_zero.grid(row=row_start + 1, column=1, padx=5, pady=5)

operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    btn_operator = tk.Button(root, text=operator, font=("Arial", 16), padx=20, pady=10, command=lambda op=operator: add_operator(op))
    btn_operator.grid(row=row_start - i+1, column=3, padx=4, pady=4)

btn_equals = tk.Button(root, text="=", font=("Arial", 16), padx=20, pady=10, command=calculate)
btn_equals.grid(row=row_start + 1, column=2, padx=5, pady=5)

btn_point = tk.Button(root, text=".", font=("Arial", 16), padx=20, pady=10, command=add_point)
btn_point.grid(row=row_start + 1, column=0, padx=5, pady=5)

root.mainloop()
