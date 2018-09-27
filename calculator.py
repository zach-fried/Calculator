import math

import os

os.chdir("/Users/Zach/Desktop/Calculator")

import exponent

num1 =float(input("Enter a number:"))
operation = input("Enter the operation you would like to perform (+, -, /, *, abs, sqrt, power):")

if operation != "abs" and operation != "sqrt" and operation != "power":
    num2 = float(input("Enter another number:"))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    else:
        result = "Error."
elif operation == "abs":
    result = abs(num1)
elif operation == "sqrt":
    result = math.sqrt(num1)
elif operation == "power":
    num2 = float(input("Enter the exponent: "))
    result = exponent.exponential(num1, num2)
else:
    result = "Error."

print("The answer is: " + str(result))
