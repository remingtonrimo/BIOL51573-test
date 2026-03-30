#!/usr/bin/env python3

import argparse

# we need an argument parser
parse_master5000=argparse.ArgumentParser(description="This script calculates the Fibonacci number for a \
                                     given position")
# command line arguments - required - positional arguments
parse_master5000.add_argument("position",help="Position in the Fibonacci sequence",type=int)
# parse the arguments
args=parse_master5000.parse_args()

# initialise 2 integers
a,b=0,1

for i in range(args.position):
    a,b=b,a+b

fibonacci_number = a

print(f"The Fibonacci number for {args.position} is {fibonacci_number}")