#!/usr/bin/python3
row_1 = []
row_2 = []
row_3 = []
matrix = []


def print_matrix_integer(matrix=[[]]):
    matrix.append(row_1)
    matrix.append(row_2)
    matrix.append(row_3)
    for row1 in matrix[0]:
        print("{:d} ".format(row1), end="")
    for row2 in matrix[1]:
        print("\n{:d} ".format(row2), end="")
    for row3 in matrix[2]:
        print("\n{:d} ".format(row3), end="")
