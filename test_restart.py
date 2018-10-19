#! /bin/env python3
import os
import sys

def like_cheese():
    var = input("Hi! I like cheese! Do you like cheese?").lower()
    if var == "yes":
        print("That's awesome!")

if __name__ == '__main__':
    #like_cheese()
    print('process id:', os.getpid(), ', argv:', sys.argv)
    path = os.path.realpath(__file__)
    python_path = sys.executable
    print(path)
    os.execv(python_path, ['python', path])  # Run a new iteration of the current script, providing any command line args from the current iteration.
