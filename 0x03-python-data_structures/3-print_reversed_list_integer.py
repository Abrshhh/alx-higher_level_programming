#!/usr/bin/python3
my_list = []


def print_reversed_list_integer(my_list=[]):

    reverse_list = my_list.reverse()

    for item in reverse_list:
        print("{:d}".format(item))
