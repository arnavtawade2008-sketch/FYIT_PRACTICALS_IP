# Pracs3-Q7 Program to perform simple calculator operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator! Please enter +, -, *, or /.")
