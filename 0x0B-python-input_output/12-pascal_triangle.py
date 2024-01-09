#!/usr/bin/python3
"""
Pascal's Triangle task
"""


def pascal_triangle(n):
    """
    Check if n is less than or equal to 0.
    If so, return an empty list.

    Initialize an empty list to store the rows of Pascal's triangle.

    Iterate through each row from 0 to n-1.
    Initialize a new row with all elements set to 1.

    Update the middle elements of the row based on the values
    from the previous row.

    Append the current row to the triangle list.

    Return the final Pascal's triangle as a list of lists.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
