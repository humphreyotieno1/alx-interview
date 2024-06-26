#!/usr/bin/python3
"""Algorithm module"""
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list): The 2D matrix to be rotated.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
