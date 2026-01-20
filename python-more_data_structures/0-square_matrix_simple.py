#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        square = []
        for integers in row:
            square.append(integers ** 2)
            new_matrix.append(square)
        return new_matrix
