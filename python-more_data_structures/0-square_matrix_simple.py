#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
      for row in matrix:
        for integers in row:
            new_matrix = list(map(lambda x: x ** 2))
    return new_matrix