#!/usr/bin/env python

"""
    This module contains a simple math game where the user
    will have to provide an answer based on the mathematical
    operation selected.

    The game contains four mathematical operations that can be
    selected on a per turn basis:

        1. Addition
        2. Subtraction
        3. Division
        4. Mulitplication

    If the user answers the question correctly, the LED will "clap"
    (i.e. blink) for five seconds. If the user answers the question
    incorrectly, the user will have three more attempts until the
    game terminates. At termination, the user will be given an option
    to play again.
"""

import time
import re
from abc import ABC, abstractmethod
from random import randint, randrange
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

class MyMath(ABC):
    """ Abstract base class """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def operation(self, a, b):
        pass

class Add(MyMath):
    """ Addition class """
    def operation(self, a, b):
        return a+b

class Subtract(MyMath):
    """ Subtraction class """
    def operation(self, a, b):
        return a-b

class Divide(MyMath):
    """ Division class.
        Note that floor division is used.
    """
    def operation(self, a, b):
        return a//b

class Multiply(MyMath):
    """ Multiplication class """
    def operation(self, a, b):
        return a*b

def select_input():
    """ Prints the list of operations for the user to choose and asks for a selection input.

        Returns:
            selection
                An integer from 1 to 4 that defines the operation the user selects.
    """
    selection = input("\nSelect number for operation: \n" \
                      "1. Add\n" \
                      "2. Subtract\n" \
                      "3. Divide\n" \
                      "4. Multiply\n> ")
    return selection

def play_again():
    """ Asks the user to input "yes" or "y" to play again or "no" to quit program.

        Returns:
            decision
                yes/y or no
    """
    decision = input("\nWould you like to play again? ([yes]/no): ")
    return decision.lower() in ["yes", "y"]

def correct_ans():
    """ Called when the user inputs the correct answer which
        will cause the LED to blink for 5 seconds.
    """
    print("\nCongratulations! The LED is clapping for you!")
    t_end = time.time() + 5
    while time.time() < t_end:
        GPIO.output(18, True)
        time.sleep(.25)
        GPIO.output(18, False)
        time.sleep(.25)

if __name__ == "__main__":
    while True:
        selection = select_input()
        a = randint(1, 100)
        b = randint(1, 100)
        options = {
            "1": "Add",
            "2": "Subtract",
            "3": "Divide",
            "4": "Multiply"
        }

        while True:
            try:
                command = (eval(options[selection]))(a, b)
                break
            except KeyError:
                print("\nPlease select a number from the list. Try again.")
                selection = select_input()

        if options[selection] == "divide":
            if a < b:
                a, b = b, a
            print("\nTo simplify division, the answer will be a whole number" \
                  "i.e. how many times can the higher number divide into the smaller number.")

        value = command.operation(a, b)

        for count in range(3, -1, -1):
            while True:
                try:
                    ans = input(f"\nThe numbers randomly generated are {a} and {b}."\
                                f" You have chosen to {options[selection].lower()}. What is the answer? ")
                    if re.search('[A-z]+', ans) is not None:
                        raise
                    else:
                        break
                except:
                    print("\nPlease input a valid number. Try again.")

            if ans == str(value):
                correct_ans()
                break
            else:
                print(f"\nWrong answer! You have {count} more tries. Please enter your answer: ")
        else:
            print("\nYou have exceeded the number of tries. Game Over!")

        if not play_again():
            print("\nThanks for playing, goodbye!")
            break
