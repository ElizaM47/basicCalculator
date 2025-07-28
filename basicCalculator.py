# Basic calculator using integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 // num2}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
