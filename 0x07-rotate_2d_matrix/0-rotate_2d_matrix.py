#!/usr/bin/python3
"""Model for rotating a 2D matrix in place"""


def rotate_2d_matrix(matrix):
    """Rotate a matrix 90 degree in place"""
    # Define the rows variable
    rows = len(matrix)

    # swap the values in rows with the values in cols using nested loop
    for r in range(rows):
        for c in range(r + 1, rows):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # Reverse the elements of each row
    for r in range(rows):
        matrix[r].reverse()
