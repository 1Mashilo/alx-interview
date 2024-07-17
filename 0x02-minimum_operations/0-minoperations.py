#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of operations
needed to result in exactly n 'H' characters in a text file using only
'Copy All'
and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n 'H' characters in a file.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
