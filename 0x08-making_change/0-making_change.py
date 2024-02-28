#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total
"""
from typing import List


def makeChange(coins: List[int], amount: int) -> int:
    """
    Calculate the minimum number of coins needed to make change for a given
    amount.

    Parameters:
    - coins (List[int]): A list of coin denominations available.
    - amount (int): The amount for which change needs to be made.

    Returns:
    - int: The minimum number of coins needed to make change for the given
    amount. Returns -1 if change cannot be made.

    Example:
    >>> makeChange([1, 2, 5], 11)
    3
    >>> makeChange([2], 3)
    -1
    """
    res = [0] + [float('inf')] * amount
    for i in range(1, amount+1):
        for j in coins:
            if i >= j:
                res[i] = min(res[i-j]+1, res[i])
    return res[amount] if res[amount] != float('inf') else -1
