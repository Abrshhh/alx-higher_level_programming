#!/usr/bin/python3
my_list = []
idx = my_list.index


def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    else:
        return my_list(idx)
    return my_list[idx]
