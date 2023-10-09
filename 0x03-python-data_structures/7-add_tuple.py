#!/usr/bin/python3
tuple_a = ()
tuple_b = ()


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + ((0,) * (2 - len(tuple_a)))
    else:
        tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        tuple_b = tuple_b + ((0,) * (2 - len(tuple_b)))
    else:
        tuple_b = tuple_b[:2]
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    new_tuple = (x, y)
    return new_tuple
