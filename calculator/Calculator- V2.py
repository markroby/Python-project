import tkinter as tk
from tkinter import messagebox
import math

class Calcu:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def percentage(x):
        return x / 100

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def power(x, y):
        return x ** y

    @staticmethod
    def log(x, base):
        if x > 0 and base > 0 and base != 1:
            result = 0
            exponent = 1
            while exponent < x:
                result += 1
                exponent = exponent * base
            return result
        else:
            return "incorrect input for log function."

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by Zero.."

    @staticmethod
    def sine(x):
        while x > math.pi:
            x -= 2 * math.pi
        while x < -math.pi:
            x += 2 * math.pi
        sum_val = 0
        term = x
        epsilon = 0.0000001
        n = 1
        while abs(term) > epsilon:
            sum_val += term
            term = -term * x * x / ((n + 1) * (n + 2))
            n += 2
        return sum_val

    @staticmethod
    def tangent(x, is_degrees=False):
        x = math.radians(x) if is_degrees else x
        return math.tan(x)

    @staticmethod
    def matrix_addition(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrix dimensions do not match for addition.")
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        return result

    @staticmethod
    def cosine(x):
        while x > math.pi:
            x -= 2 * math.pi
        while x < -math.pi:
            x += 2 * math.pi
        sum_val = 0
        term = 1
        epsilon = 0.0000001
        n = 0
        while abs(term) > epsilon:
            sum_val += term
            term = -term * x * x / ((n + 1) * (n + 2))
            n += 2
        return sum_val

    @staticmethod
    def square_root(x):
        if x < 0:
            return "Cannot be square root of a negative number."
        else:
            guess = x / 2
            epsilon = 0.0000001
            while abs(guess * guess - x) > epsilon:
                guess = (guess + x / guess) / 2
            return guess
class CalculatorInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("500x700")

        self.result_var = tk.StringVar()

        self.calcu = Calcu()

        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        entry = tk.Entry(entry_frame, textvariable=self.result_var, font=("Helvetica", 20), bd=10, insertwidth=4,
                         width=18, justify='right')
        entry.grid(row=0, column=0)
        entry.bind("<Return>", lambda event: self.calculate())

        button_frame = tk.Frame(self)
        button_frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("log", 5, 0), ("cos", 5, 1), ("power", 5, 2), ("square_root", 5, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=("Helvetica", 20), width=5, height=2,
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col)

    def calculate(self):
        expression = self.result_var.get()
        try:
            result = eval(expression)
            self.result_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def button_click(self, text):
        current_text = self.result_var.get()
        if text == "=":
            self.calculate()
        elif text == "C":
            self.result_var.set("")
        elif text == "log":
            try:
                x = float(current_text)
                if x > 0:
                    result = math.log(x)
                    self.result_var.set(result)
                else:
                    messagebox.showerror("Error", "Cannot calculate logarithm of a non-positive number")
            except ValueError:
                messagebox.showerror("Error", "Invalid input for logarithm calculation")
        elif text == "cos":
            try:
                x = float(current_text)
                while x > math.pi:
                    x -= 2 * math.pi
                while x < -math.pi:
                    x += 2 * math.pi
                sum_val = 0
                term = 1
                epsilon = 0.0000001
                n = 0
                while abs(term) > epsilon:
                    sum_val += term
                    term = -term * x * x / ((n + 1) * (n + 2))
                    n += 2
                self.result_var.set(sum_val)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for cosine calculation")
        elif text == "power":
            try:
                base, exponent = map(float, current_text.split("**"))
                result = base ** exponent
                self.result_var.set(result)
            except (ValueError, IndexError):
                messagebox.showerror("Error", "Invalid input for power calculation")
        elif text == "square_root":
            try:
                x = float(current_text)
                if x >= 0:
                    result = math.sqrt(x)
                    self.result_var.set(result)
                else:
                    messagebox.showerror("Error", "Cannot calculate square root of a negative number")
            except ValueError:
                messagebox.showerror("Error", "Invalid input for square root calculation")
        else:
            self.result_var.set(current_text + str(text))
        

if __name__ == "__main__":
    app = CalculatorInterface()
    app.mainloop()
