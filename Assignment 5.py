# Task 1
# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.


dic = {"Nichole":45,"Max": 66,"Peater":78,"Micheal":89}
"""
student marks in dictionary. 
"""
user = input("Please enter student name: ").capitalize()

if user in dic:
    print(f"{user}'s marks: {dic[user]}")
else:
    print("student not fount")

# TASK 2:
# Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

list_1 = list(range(1,11))
print(f"Orignal list: {list_1}")
print(f"Extracts the first five elements : {list_1[0:5]}")
print(f"Reverses extracted elements : {list_1[0:5][::-1]}")

