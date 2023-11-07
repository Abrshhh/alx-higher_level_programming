#!/usr/bin/pthon3
'''Define a function writing a string to a text file.'''


def read_file(filename="", text=""):
    '''Returns the number of character written.'''

    with open('filename', 'w', encoding="utf-8") as f:
        return (f.write(text), end="")
