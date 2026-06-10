""" Dice Game
A simple Python project that simulates rolling a six-sided die.
"""
print("===================")
print("Welcome to dice game")
print("===================")
while True:
    name = input("Please enter your name: ").strip()
    """
    Prompt to check,user's valid name or inputs
    """
    if name.isalpha():
        print(f"{name}! Let's play dice game")
        break
    else:
        print("You chose an invalid input. Please enter your name: ")

import random
while True:
    choose = input("Please press 'Enter' to pay Game or press 'q' to quit: ")
    if choose == "q":
        print(f"{name}! Thank you for choosing dice game")
        """ if user wants to quit the game."""
        break
    elif choose == "":
        print(f"Your number is: {random.randint(1, 6)}\n")
    else:
        print("You chose an invalid input. Please try again.")
print("{name}, thanks for playing dice game. ")

