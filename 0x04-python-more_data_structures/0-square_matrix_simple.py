#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    resultingMatrix = [[y ** 2 for y in row] for row in matrix]
    return resultingMatrix
