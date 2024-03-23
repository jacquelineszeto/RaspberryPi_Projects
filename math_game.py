import RPi.GPIO as GPIO
import time
import re
import sys
from abc import ABC, abstractmethod
from random import randint, randrange

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

class math():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @abstractmethod
    def operation(self):
        pass
    
class add(math):
    def __init__(self, a, b):
        super().__init__(a, b)
        
    def operation(self, a, b):
        return self.a+self.b
    
class subtract(math):
    def __init__(self, a, b):
        super().__init__(a, b)
        
    def operation(self, a, b):
        return self.a-self.b

class divide(math):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def operation(self, a, b):
        return self.a/self.b
    
class multiply(math):
    def __init__(self, a, b):
        super().__init__(a, b)
        
    def operation(self, a, b):
        return self.a*self.b

def selectInput():
    selection = input("\nSelect number for operation: \n 1. Add\n 2. Subtract\n 3. Divide\n 4. Multiply\n\n")
    return selection

def endDecision():
    decision = input("\nWould you like to play again? (yes/no)\n")
    return decision

def correctAns():
    print("\nCongratulations! The LED is clapping for you!\n")
    t_end = time.time() + 5
    while time.time() < t_end:
        GPIO.output(18, True)
        time.sleep(.25)
        GPIO.output(18, False)
        time.sleep(.25)
    
if __name__ == "__main__":
    while True:
        selection = selectInput()
        a = randint(10,99)
        b = randint(10,99)
        options = {
            "1": "add",
            "2": "subtract",
            "3": "divide",
            "4": "multiply"
        }
        
        while True:
            try:
                command = (eval(options[selection]))(a, b)  
                break
            except KeyError:
                print("\nPlease select a number from the list. Try again.\n")
                selection = selectInput()
            
        value = command.operation(a,b)
        ans = input(f"\nThe numbers randomly generated are {a} and {b}. You have chosen to {options[selection]}. What is the answer?\n")
        
        # need to check that the input is indeed numbers. use regexp since it comes in as string
#         if 
        
        count = 3
        if ans == str(value):
            correctAns()
        else:
            while count != 0:
                # need to work on this section - this is incomplete
                ans = input(f"\nWrong answer! You have {count} more tries. Please enter your answer.\n")
                if ans == str(value):
                    correctAns()
                    break
                count -= 1
            print("\nYou have exceeded the number of tries. Goodbye!")
            sys.exit()
        
        if endDecision() == "no":
            print("\nThanks for playing, goodbye!")
            break

            


    
    