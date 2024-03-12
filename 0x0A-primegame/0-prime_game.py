#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines if a player is the winner"""
    if x is None or nums is None or len(nums) == 0:
        return None
    if x < 1:
        return None
    if x < len(nums):
        return None

    b_win, m_win, start = 0, 0, 3
    primes = []
    nums.sort()

    for n in nums:
        if n < 2:
            b_win += 1
            continue
        elif n % 2 == 0:
            primes.append(2)
            m_win += 1
            continue
        elif n % 2 == 0:
            primes.append(2)
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
    return None
