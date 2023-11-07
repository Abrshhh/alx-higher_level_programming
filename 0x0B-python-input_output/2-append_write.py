#!/usr/bin/python3
'''Define a string appending function.'''


def append_write(filename="", text=""):
    '''Append a string to a UTF8 file.

    Args:
        filename (str): the file which the text is appended on.
        text (str): the text to be appended.

        Returns: the number of characters added'''

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
