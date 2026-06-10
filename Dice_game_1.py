"""
Dice Game
A simple Python project that simulates rolling a six-sided die.
"""

import random
def get_player_name():
    """Prompt the user for a valid name."""
    while True:
        name = input("Please enter your name: ").strip()
        if name.isalpha():
            return name
        print("Invalid input. Please enter a name using only letters.")

def roll_dice():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)
def main():
    print("=" * 25)
    print(" Welcome to Dice Game ")
    print("=" * 25)

    name = get_player_name()
    print(f"\nHello, {name}! Let's play.\n")

    rolls = 0

    while True:
        choice = input(
            "Press Enter to roll the dice or 'q' to quit: "
        ).lower()

        if choice == "q":
            print(f"\n{name}, thanks for playing!")
            print(f"You rolled the dice {rolls} time(s).")
            break

        elif choice == "":
            rolls += 1
            result = roll_dice()
            print(f"You rolled: {result}\n")

        else:
            print("Invalid input. Please press Enter or 'q'.\n")

    print("Hope to see you again soon!")
if __name__ == "__main__":
    main()