import tkinter as tk

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    factorial = 1
    while n >= 1:
        factorial = factorial * n
        n = n - 1
    return factorial

def factor(n):
    factors = []
    factor = 1
    while factor <= n:
        if n % factor == 0:
            factors.append(factor)
        factor = factor + 1
    return factors

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operator = operator_var.get()
    
    if operator == 'Add':
        result = add(num1, num2)
    elif operator == 'Subtract':
        result = subtract(num1, num2)
    elif operator == 'Multiply':
        result = multiply(num1, num2)
    elif operator == 'Divide':
        result = divide(num1, num2)
    elif operator == 'Power':
        result = power(num1, num2)
    elif operator == 'Factorial':
        result = factorial(num1)
    elif operator == 'Factor':
        result = factor(num1)
    
    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("500x380",)
 # Width x Height in pixels
window.resizable(True, True)
# Create entry fields for numbers
entry_num1 = tk.Entry(window)
entry_num1.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create a drop-down menu for operators
operator_var = tk.StringVar()
operator_var.set("Add")
operator_menu = tk.OptionMenu(window, operator_var, "Add", "Subtract", "Multiply", "Divide", "Power", "Factorial", "Factor")
operator_menu.pack()

# Create a button to calculate
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()
