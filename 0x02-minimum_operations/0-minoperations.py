#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n: float) -> int:
    '''function that returns the minimum operations needed'''
    factors = []
    div = 2

    while n > 1:
        if n % div == 0:
            factors.append(div)
            n = n / div
        else:
            div += 1
    return sum(factors)
