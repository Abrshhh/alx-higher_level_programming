#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]


def print_reversed_list_integer(my_list=[]):

    my_list.reverse()

    for item in my_list:
            print("{:d}".format(item))
