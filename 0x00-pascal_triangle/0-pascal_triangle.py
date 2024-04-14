#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle.

Pascal's triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it.

The function pascal_triangle(n) takes an integer n as input and returns a list of lists representing the Pascal's triangle up to the nth row.
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
