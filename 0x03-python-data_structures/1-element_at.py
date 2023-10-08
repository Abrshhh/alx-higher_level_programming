#!/usr/bin/python3
my_list = []
idx = my_list.index()


def element_at(my_list, idx):
    if len(my_list) == 0:
        return None
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
