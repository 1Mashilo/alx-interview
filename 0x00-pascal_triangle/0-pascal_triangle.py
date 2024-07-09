#!/usr/bin/python3
"""
Module for generating Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

