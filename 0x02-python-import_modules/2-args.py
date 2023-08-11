#!/usr/bin/python3
import sys

def print_args(args):
    num_args = len(args)

    if num_args == 0:
        print(num_args, "arguments.")
    elif num_args == 1:
        print(num_args, "argument:")
    elif num_args > 1:
        print(num_args, "arguments:")

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    arguments = sys.argv[1:]

    print_args(arguments)
