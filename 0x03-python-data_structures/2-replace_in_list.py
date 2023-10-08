#!/usr/bin/python3
#idx = my_list.index()
my_list = []
idx = my_list.index()
#element = my_list[idx]


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        my_list[idx] = my_list
        return my_list
    
