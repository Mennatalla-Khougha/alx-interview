#!/usr/bin/python3
"""Defines an island perimeter measuring function."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""
    rows, cols, size = len(grid), len(grid[0]), 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dirct = [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
                for dr, dc in dirct:
                    if dr == -1 or dr == rows or dc == -1 or dc == cols:
                        size += 1
                    elif grid[dr][dc] == 0:
                        size += 1

    return size
