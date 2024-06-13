#!/usr/bin/python3
'''Module for finding the perimeter'''


def island_perimeter(grid):
    '''function to compute the perimeter'''
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check up
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check down
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter
