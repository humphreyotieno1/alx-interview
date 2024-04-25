#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''Function that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.'''
    if n <= 1:
        return 0

    operations = 0
    buffer = 1

    while buffer < n:
        if n % buffer == 0:
            operations += n // buffer
            buffer *= n // buffer
            if buffer == n:
                return operations
        buffer += 1

    return 0
