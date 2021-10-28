#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'islands' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_STRING_ARRAY grid as parameter.
#


def islands(grid):
    # Write your code here
    num_island = 0
    n_row = len(grid)
    n_col = len(grid[0])

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for i in range(n_row):
        for j in range(n_col):
            if grid[i][j] == "1":
                dfs(grid, i, j, n_row, n_col, directions)
                num_island += 1
    return num_island


def dfs(grid, i, j, n_row, n_col, directions):
    if i < 0 or j < 0 or i >= n_row or j >= n_col or grid[i][j] != "1":
        return

    # visit
    grid[i][j] = "-1"

    for direction in directions:
        x = direction[0] + i
        y = direction[1] + j
        dfs(grid, x, y, n_row, n_col, directions)


# Time
# O(row*col)
if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    # print(islands(grid))
    assert islands(grid) == 1

    # grid = [
    #   ["1","1","0","1","0"],
    #   ["1","1","0","1","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","0","0","0"]
    # ]
    # assert islands(grid) == 1
