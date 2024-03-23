import RPi.GPIO as GPIO
import time
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
    selection = input("Select number for operation: \n\n 1. Add\n 2. Subtract\n 3. Divide\n 4. Multiply\n")
    return selection
    
if __name__ == "__main__":
    
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
    print(f"\nThe numbers randomly generated are {a} and {b}. You have chosen to {options[selection]}. The answer is {value}")

    
    
