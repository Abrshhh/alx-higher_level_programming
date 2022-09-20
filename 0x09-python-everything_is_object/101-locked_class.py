#!/usr/bin/class
""" Define a locked class"""


class LockedClass:
    """
    Prevent anything except attribute called 'first name'
    """

    __slots__ = ["first_name"]
