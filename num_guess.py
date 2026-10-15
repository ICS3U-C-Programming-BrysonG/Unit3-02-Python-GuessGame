#!/usr/bin/env python3
# Created By: Bryson
# Date: 10 15, 2026
# This program runs a guessing game where
# it asks the user for a number then compares it to
# the correct number.

import constants


def main():

    # Get the guessed number from the user
    guessed_number = int(input("Enter your guessed number (0 - 10): "))

    # Check if guessed number is the same as the correct number
    if guessed_number == constants.CORRECT_NUMBER:
        print("You guessed correct!")

    if guessed_number != constants.CORRECT_NUMBER:
        print("You guessed wrong! The correct number was 5")


if __name__ == "__main__":
    main()
