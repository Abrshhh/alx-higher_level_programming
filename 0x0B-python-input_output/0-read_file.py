#!/usr/bin/python3
'''Define a text reading function.'''


def read_file(filename=""):
    '''Reads and prints a text file.'''

    with open('filename', 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
