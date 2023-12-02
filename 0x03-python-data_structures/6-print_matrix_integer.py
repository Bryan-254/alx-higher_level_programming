#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print("Empty matrix")
        return

    row_count = len(matrix)
    col_count = len(matrix[0])

    for x in range(row_count):
        for y in range(col_count):
            if y == col_count - 1:
                print("{:d}".format(matrix[x][y]), end="")
            else:
                print("{:d}".format(matrix[x][y]), end=" ")
        print()
