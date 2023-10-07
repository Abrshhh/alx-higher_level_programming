#!/usr/bin/python3


def print_list_integer(my_list=[]):

    list_entered = []

    for lists in my_list:
        if isinstance(my_list, int):
            list_entered.append(lists)

    for printed_lists in list_entered:
        print("{}".format(int(lists)))
