"""1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly."""

number = int(input("Enter a number: "))

if number % 2==0:
    print("The number is even ")
else:
    print("The number is odd ")

"""1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""
total_sum = 0
for i in range(1,50):
    total_sum += i
print(f"the sum of all intergers from 1 to 50 is {total_sum}")

