#!/usr/bin/env python3
"""
Rock, Paper, Scissors — simple console game

Author: Suleiman Lamorde
Date: 2025-09-15

Description:
    A small command-line program that plays Rock, Paper, Scissors between
    the user and the computer.

How to run:
    python rock_paper_scissors.py

Features:
- Defines possible choices: rock, paper, scissors
- Gets the user's choice (case-insensitive, with validation)
- Generates a random choice for the computer
- Determines the winner using standard rules
- Allows the user to play multiple rounds and quit with 'q'
"""

import random
from typing import Tuple

CHOICES = ("rock", "paper", "scissors")

def get_user_choice() -> str:
    """Prompt the user until they enter a valid choice or 'q' to quit.

    Returns:
        'quit' if the user typed 'q', otherwise one of CHOICES.
    """
    while True:
        choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").strip().lower()
        if choice == 'q':
            return 'quit'
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type 'rock', 'paper', or 'scissors' (or 'q' to quit).")

def get_computer_choice() -> str:
    """Randomly choose and return one of CHOICES for the computer."""
    return random.choice(CHOICES)

def determine_winner(user: str, computer: str) -> str:
    """Decide the round winner.

    Returns:
        'tie' if it's a draw,
        'user' if the user wins,
        'computer' if the computer wins.
    """
    if user == computer:
        return 'tie'

    # Mapping of what each choice defeats
    wins_against = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if wins_against[user] == computer:
        return 'user'
    return 'computer'

def main():
    print("=== Rock, Paper, Scissors ===")
    print("Type 'q' anytime to quit.\n")

    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            print("Thanks for playing. Goodbye!")
            break

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == 'tie':
            print("It's a tie!\n")
        elif result == 'user':
            print("You win! 🎉\n")
        else:
            print("Computer wins. Better luck next time!\n")

if __name__ == '__main__':
    main()
