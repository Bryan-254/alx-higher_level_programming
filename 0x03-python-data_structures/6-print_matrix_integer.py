#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[x]:
        print()

    row_count = len(matrix)
    col_count = len(matrix[x])

    for x in range(row_count):
        for y in range(col_count):
            if y != col_count - 1:
                endspace = ' '
            else:
                endspace = ''
            print("{:d}".format(matrix[x][y]), end=endspace)
        print()
