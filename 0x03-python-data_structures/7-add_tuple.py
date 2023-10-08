#!/usr/bin/python3
tuple_a = ()
tuple_b = ()


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) == 1:
        list_a[1] = 0
    elif len(list_a) == 0:
        list_a[0] = 0
        list_a[1] = 0
    elif len(list_b) == 1:
        list_b[1] = 0
    elif len(list_b) == 0:
        list_b[0] = 0
        list_b[1] = 0
    x = list_a[0] + list_b[0]
    y = list_a[1] + list_b[1]
    new_list = (x, y)
    new_tuple = tuple(new_list)
    return new_tuple
