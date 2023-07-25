#!/usr/bin/python3
import sys

def arguments (argv):
    num_argv = len(argv)
    
    if num_argv == 0:
        print(f"{num_argv} argments.")
    elif num_argv == 1:
        print(f"{num_argv} argument:")
        print(f"{num_argv}: {argv[0]}")
    else:
        print(f"{num_argv} arguments:")
        for i in range(num_argv):
            print(f"{i + 1}: {argv[i]}")

if __name__ == "__main__":
    arguments(sys.argv[1:])