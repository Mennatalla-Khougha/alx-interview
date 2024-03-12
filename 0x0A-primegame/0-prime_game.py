#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines if a player is the winner"""
    if x is None or nums is None or len(nums) == 0:
        return None
    if x < 0:
        return None
    if x < len(nums) or x > len(nums):
        return None

    b_win, m_win, start = 0, 0, 3
    primes = [2]
    nums.sort()

    for n in nums:
        if n < 2:
            b_win += 1
            continue

        if n % 2 == 0:
            m_win += 1
            continue

        prime = len(primes)
        for ele in range(start, n + 1, 2):
            for p in range(prime):
                if ele % primes[p] == 0:
                    break
            if p == prime - 1:
                primes.append(ele)
                prime += 1

        if n % 2 != 0:
            start = ele
        else:
            start = ele + 1

        if prime % 2 == 0:
            b_win += 1
        else:
            m_win += 1

    if b_win > m_win:
        return "Ben"
    if b_win < m_win:
        return "Maria"
    if b_win == m_win:
        return None
