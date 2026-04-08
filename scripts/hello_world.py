#!/usr/bin/env python3

import argparse
import cowsay

def lawyer():
    parse_master5000=argparse.ArgumentParser(description="The cow in this script will greet you")

    parse_master5000.add_argument("name",help="The name of the person to greet")
    return parse_master5000.parse_args()

# say hello world
def helloworld():
    greeting = cowsay.cow("Hello, " + args.name)
    return greeting

def main():
    greet = helloworld()
    print(greet)

args = lawyer()

if __name__ == "__main__":
    main()
