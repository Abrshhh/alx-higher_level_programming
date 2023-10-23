#!/usr/bin/python3
my_list = []
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i])
            count = count + 1
        except IndexError:
            break
    return count
