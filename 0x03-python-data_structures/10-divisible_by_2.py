#!/usr/bin/python3
my_list = []
new_list = []


def divisible_by_2(my_list=[]):
    for number in my_list:
        if number % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
