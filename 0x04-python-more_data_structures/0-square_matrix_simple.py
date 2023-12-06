#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return []

    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Iterate through each element in the matrix and compute the square
    for x in range(num_rows):
        for y in range(num_cols):
            new_matrix[x][y] = matrix[x][y] ** 2

    return new_matrix
