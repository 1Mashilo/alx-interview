#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): A 2D matrix
        where each sublist represents a row.

    Returns:
        None: The matrix is modified in-place, so nothing
        is returned.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotate_2d_matrix(matrix)
        # matrix becomes [[7, 4, 1],
        #                 [8, 5, 2],
        #                 [9, 6, 3]]
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

