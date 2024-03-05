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
                    if -1 < dr < rows and -1 < dc < cols and grid[dr][dc] == 0:
                        size += 1

    return size
    # width = len(grid[0])
    # height = len(grid)
    # edges = 0
    # size = 0

    # for i in range(height):
    #     for j in range(width):
    #         if grid[i][j] == 1:
    #             size += 1
    #             if (j > 0 and grid[i][j - 1] == 1):
    #                 edges += 1
    #             if (i > 0 and grid[i - 1][j] == 1):
    #                 edges += 1
    # return size * 4 - edges * 2
