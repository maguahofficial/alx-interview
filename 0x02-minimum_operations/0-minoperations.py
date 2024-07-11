#!/usr/bin/python3
"""
function that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Function returns the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    operationsx = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operationsx += min_operations
            n /= min_operations
        min_operations += 1
    return operationsx
