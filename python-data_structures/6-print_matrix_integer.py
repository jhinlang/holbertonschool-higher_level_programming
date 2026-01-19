#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for integers in range(len(row)):
            if integers != len(row) - 1:
                print('{:d}'.format(row[integers]), end = "")
            else:
                print('{:d}'.format(row[integers]))
