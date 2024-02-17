
import math



class Calcu :
    
    def add(x, y):
        return x + y
    def percentage(x):
        return x / 100
    def subtract(x, y):
        return x - y
    def power(x, y):
        return x ** y
    def Log(x, base):
        if x > 0 and base > 0 and base != 1:
            result = 0
            exponent = 1
            while exponent < x:
                result += 1
                exponent = exponent * base
            return result
        else:
            return "incorrectr input for log function."

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by Zero.."
    def sine(x,is_degrees):
        while x > math.pi:
            x -= 2 * math.pi
        while x < -math.pi:
            x += 2 * math.pi
        sum = 0
        term = x
        epsilon = 0.0000001
        n = 1
        while abs(term) > epsilon:
            sum += term
            term = -term * x * x / ((n + 1) * (n + 2))
            n += 2
        return sum
    def tangent(x, is_degrees=False):
        x = math.radians(x) if is_degrees else x
        return math.tan(x)
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
    def cosine(x,is_degrees):
        while x > math.pi:
            x -= 2 * math.pi
        while x < -math.pi:
            x += 2 * math.pi
        sum = 0
        term = 1
        epsilon = 0.0000001
        n = 0
        while abs(term) > epsilon:
            sum += term
            term = -term * x * x / ((n + 1) * (n + 2))
            n += 2
        return sum
    def square_root(x):
        if x < 0:
            return "Cannot be square root of a negative number."
        else:
            guess = x / 2
            epsilon = 0.0000001
            while abs(guess * guess - x) > epsilon:
                guess = (guess + x / guess) / 2
            return guess


is_degrees = True

while True:
    print("Select operation:")
    print("1.  Add")
    print("2.  Subtract")
    print("3.  Multiply")
    print("4.  Divide")
    print("5.  Square Root")
    print("6.  Power")
    print("7.  Log")
    print("8.  Sine")
    print("9.  Cosine")
    print("10. Tangent")
    print("11. Percentage")
    print("12. Pi (Π)")
    print("13. Euler's  (e)")
    print("14. (φ)")
    print("15. (τ)")
    print("16. Inverse (Inv)")
    print("17. Switch Degrees/Radians")
    print("18. Matrix Addition")
    print("19. Exit")

    choice = input("Enter choice (1-18): ")

    if choice in ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']:
        num1 = float(input("Enter the number: "))
    elif choice in ['8', '9', '10']:
        is_degrees = input("Enter 'deg' for degrees or 'rad' for radians: ").lower().startswith('deg')
    elif choice == '18':
        matrix1 = []
        matrix2 = []
        rows = int(input("Enter the number of rowss : "))
        cols = int(input("Enter the number of columns : "))
        print("Enter elements for Matrix 1:")
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(float(input(f"Enter element at position ({i + 1}, {j + 1}): ")))
            matrix1.append(row)
        print("Enter elements for Matrix 2:")
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(float(input(f"Enter element at position ({i + 1}, {j + 1}): ")))
            matrix2.append(row)
        print("Matrix 1:")
        for row in matrix1:
            print(row)
        print("Matrix 2:")
        for row in matrix2:
            print(row)
        result_matrix = Calcu.matrix_addition(matrix1, matrix2)
        print("Matrix Add Result:")
        for row in result_matrix:
            print(row)
    elif choice in ['19']:
        print("Exiting.")
        break
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", Calcu.add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", Calcu.subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", Calcu.multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", Calcu.divide(num1, num2))
    elif choice == '5':
        print("Square root of", num1, "=", Calcu.square_root(num1))
    elif choice == '6':
        exp = float(input("Enter the exponent: "))
        print(num1, "raised to the power of", exp, "=", Calcu.power(num1, exp))
    elif choice == '7':
        base = float(input("Enter the Log base: "))
        print("Log of", num1, "with base", base, "=", Calcu.Log(num1, base))
    elif choice == '8':
        print("Sine of", num1, "degrees =", Calcu.sine(num1, is_degrees))
    elif choice == '9':
         print("Cosine of", num1, "degrees =", Calcu.cosine(num1, is_degrees))
    elif choice == '10':
        print("Tangent of", num1, "degrees =", Calcu.tangent(num1, is_degrees))
    elif choice == '11':
        print(num1, "% =", Calcu.percentage(num1))
    elif choice == '12':
        print("Pi (Π) =", math.pi)
    elif choice == '13':
        print("Euler's nummber (e) =", math.e)
    elif choice == '14':
        print("Golden ratio (φ) =", (1 + math.sqrt(5)) / 2)
    elif choice == '15':
        print("Tau (τ) =", math.tau)
    elif choice == '16':
        while True:
            inverse_choice = input("Enter 'percent', 'sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'Exit': ")

            if inverse_choice.lower() == 'exit':
                print("Exiting the program.")
                break  
            if inverse_choice == 'sin':
                print(f"Arcsin of {num1} =", math.degrees(math.asin(num1)) if is_degrees else math.asin(num1))
                break 
            elif inverse_choice == 'cos':
                print(f"Arccos of {num1} =", math.degrees(math.acos(num1)) if is_degrees else math.acos(num1))
                break 
            elif inverse_choice == 'tan':
                print(f"Arctan of {num1} =", math.degrees(math.atan(num1)) if is_degrees else math.atan(num1))
                break
            elif inverse_choice == 'sqrt':
                print(f"Inverse square root of {num1} =", 1 / math.sqrt(num1))
                break
            elif inverse_choice == 'log':
                print(f"Inverse log of {num1} =", 10**num1)
                break
            elif inverse_choice == 'exp':
                print(f"Inverse exponential of {num1} =", math.exp(num1))
                break
            elif inverse_choice == 'percent':
                print(f"Value of {num1}% =", num1 / 100)
                break
            else:
                print("Invalid inverse choice.")
    elif choice == '17':
        is_degrees = not is_degrees
        print("Switched to", "degreees" if is_degrees else "radians") 
    else:
        print(" Please enter a valid choice.")
