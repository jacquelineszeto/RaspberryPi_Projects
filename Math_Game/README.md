*Please note that this code is still a work in progress.*

# Introduction
math_game.py is a simply math game that whenever the user will entre the correct answer based on the mathematical operation selected, the LED will "clap" (i.e. blink).

# Description
The user will be prompted to select one of the following mathematical operations at the start of the program:

    * Multiplication
    * Addition
    * Division
    * Subtraction

Two random number generators are used to generate two numbers and the script will use these two numbers to carry the operation on. The script will prompt the user to enter the answer. If the answer is correct, the LED will blink for 5 seconds. If the answer is incorrect, the user will have three more attemps before the application terminates.

## Electrical Configuration
This project requires the following:

    * Breadboard
    * One (1) LED
    * One (1) male-to-female jumper wires
    * 220 Ohm resistor

CLK (PI GPIO 12) -------- LED -------- 220 Ohm R -------- GND (PI)

# Installation and Run
Ensuring that you have the proper electrical componet setup to the Raspberry Pi, simply clone the repository to your Raspberry Pi and run the code in Thonny IDE.

# Credits
Jacqueline Szeto
2024


