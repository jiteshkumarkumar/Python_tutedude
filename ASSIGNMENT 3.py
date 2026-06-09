# TASK 1:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

num = int(input("Enter a number: " ))
def fun(num):
    if num==0 or num==1:
        return 1
    elif num < 0:
        return "Invalid Number"
    else:
        return num * fun(num-1)
print(f"Factorial of {num} is {fun(num)}")

# TASK 2:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# Square root of the number
# Natural logarithm (log base e) of the number
# Sine of the number (in radians)

num = int(input("Enter a number: " ))
import math

print(f"square root: {math.sqrt(num)}")
print(f"Longarithm: {math.log(num)}")
print(f"square root: {math.sin(num)}")

