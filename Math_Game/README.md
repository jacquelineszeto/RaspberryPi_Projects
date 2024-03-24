*Please note that this code is still a work in progress.*

# Introduction
math_game.py is a simple math game where the user will enter an answer based on the mathematical operation selected. When the user enters the correct answer, the LED will "clap" (i.e. blink).

# Description
The user will be prompted to select one of the following mathematical operations at the start of the program:

    * Multiplication
    * Addition
    * Division
    * Subtraction

Two random number generators are used to generate two numbers and the script will use these two numbers to carry the operation on. The script will prompt the user to enter the answer. If the answer is correct, the LED will blink for 5 seconds. If the answer is incorrect, the user will have three more attemps before the program terminates.

## Circuit Configuration
This project requires the following:

    * Breadboard
    * One (1) LED
    * One (1) male-to-female jumper wires
    * 220 Ohm resistor

CLK (PI GPIO 12) -------- LED -------- 220 Ohm R -------- GND (PI)

**It is recommended to shutdown your Raspberry Pi whenever making electrical configuration changes.**

# Installation and Run
Ensuring that you have the proper circuit configured on your Raspberry Pi, simply clone the repository to your Raspberry Pi and run the code in Thonny IDE.

# Credits
Jacqueline Szeto
2024


