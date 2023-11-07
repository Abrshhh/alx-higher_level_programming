#!/usr/bin/python3
'''Define a text reading function.'''


def read_file(filename=""):
    '''Reads and prints a text file.'''

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
