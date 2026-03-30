#!/usr/bin/env python3

import argparse

# prompt the user for a number
position = input("Please enter a position in the fibonacci sequence:") # This is a very clunky way of doing things


# initialise 2 integers
a,b=0,1
for i in range(int(position)):
    a,b=b,a+b

fibonacci_number = a

print(f"The Fibonacci number for {position} is {fibonacci_number}")