#simple calculator to take in 2 inputs and perform an operation defined by the user
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

operation = input("Enter the operation you want performed")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
else:
    print(num1 / num2)


