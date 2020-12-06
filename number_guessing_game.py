#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program is the number guessing game

import random


def main():
    # this function can tell the user if the number they guessed is correct

    # input
    guessed_string = input("Guess a number between 0 to 9: ")
    print("")

    # process
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    try:
        guessed_number = int(guessed_string)

        if guessed_number == random_number:
            print("You are correct!! {} is the correct number."
                  .format(random_number))
        else:
            print("You are wrong! {} was the correct number. Try agian."
                  .format(random_number))

    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
