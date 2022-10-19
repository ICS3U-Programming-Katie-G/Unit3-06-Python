#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 18th, 2022
# This program generates a random number,
# then gets the user's guess. The program
# uses a try-catch statement to make sure
# the user enters a valid integer, then
# another if statement to make sure the
# integer is within the acceptable parameters.
# Then, the program checks to see if the user's
# guess is correct, and tells the user the correct
# number.
import random


# this function generates a random number,
# gets the user's input, then checks to see
# if it's a valid integer using a try-catch
# statement, then checking to see if the user
# input is within the acceptable range. Then,
# this function will check to see if the user's
# guess is the correct guess, and display the result
# back to the user.
def main():
    # getting the guess from the user
    user_guess = input("Hello my friend! Guess a number from 0-9 please! ")

    # the program generates a random number from 0-9.
    correct_num = random.randint(0, 9)

    # checks to see if user's guess can be casted
    # to an integer.
    try:
        user_guess_as_integer = int(user_guess)
        if user_guess_as_integer >= 0 and user_guess_as_integer <= 9:
            if user_guess_as_integer == correct_num:
                print("Your guess of {} was correct!".format(user_guess_as_integer))
            else:
                print(
                    "Your guess was not correct. The correct number "
                    "was {}.".format(correct_num)
                )
        else:
            print(
                "My friend. My very good friend. {} is not a valid integer. "
                "Only integers from 0-9 "
                "please.".format(user_guess_as_integer)
            )
    except Exception:
        print(
            "My friend. My very good friend. {} is not a valid integer. "
            "Only integers from 0-9 please.".format(user_guess)
        )
    finally:
        print(
            "Thank you for using this program! "
            "I hope your experience was positive :)"
        )


if __name__ == "__main__":
    main()
