#!/usr/bin/python3
"""Define a function writing a string to a text file."""


def write_file(filename="", text=""):
    """Returns the number of character written.


    Args:
        filename (str): the name of the file.
        text (str): the text to be written.

    Returns: the number of character written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text), end="")
