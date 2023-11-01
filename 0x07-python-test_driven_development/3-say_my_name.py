#!/usr/bin/python3
'''Define a full name function.'''


def say_my_name(first_name, last_name=""):
    '''This function prints "My name is <first_name> <last_name>.

    Args:
        first_name: the first name.
        last_name: the last name.

    Raises:
        TypeError: if first_name and last_name are not string
    '''

    if not isinstance (first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance (last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first name.title} {last name.title}")
