#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    triangle = [[1]]

    for i in range(1, n):
        temp = []
        row = [0] + triangle[-1] + [0]
        for j in range(i + 1):
            temp.append(row[j] + row[j + 1])
        triangle.append(temp)
    return triangle
