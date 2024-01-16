#!/usr/bin/python3
"""
This module is for defining the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    The function `minOperations` calculates the minimum number of
    operations required to reduce a given number `n` to 1 by repeatedly
    dividing it by its smallest prime factor.

    :param n: The parameter `n` represents a positive integer
    :type n: int
    :return: the minimum number of operations required to reduce the given
    number 'n' to 1.
    """
    if n <= 1:
        return 0

    result = 0
    num = 2
    while n > 1:
        while n % num == 0:
            result += num
            n //= num
        num += 1
    return result
