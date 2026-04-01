#!/usr/bin/env python3

import argparse

# ===== function to parse the command line arguments =====
def lawyer():
    # we need an argument parser
    parse_master5000=argparse.ArgumentParser(description="This script calculates the Fibonacci number for a \
                                        given position")
    
    # command line arguments - required - positional arguments
    parse_master5000.add_argument("position",help="Position in the Fibonacci sequence",type=int)
    
    # here's an optional argument
    parse_master5000.add_argument("-v","--verbose",help="Print verbose output",action="store_true")
    
    # parse the arguments and return them
    return parse_master5000.parse_args() # one step

# ===== function to calculate the Fibonacci number =====
def fib_master5000():
    # initialise 2 integers
    a,b=0,1
    for i in range(args.position):
        a,b=b,a+b
    fibonacci_number = a
    return fibonacci_number # two steps

# ===== function to print the output =====
def print_output(x):
    if args.verbose:
        print(f"The Fibonacci number for {args.position} is {x}")
    else:
        print(x)


# ===== main function =====
def main():
    answer = fib_master5000()
    print_output(answer)

# ===== using lawyer function =====
args = lawyer()

# set the environment for this script
# is this master (i.e., a standalone Python script), or
# is this a python module
if __name__ == "__main__":
    main()
