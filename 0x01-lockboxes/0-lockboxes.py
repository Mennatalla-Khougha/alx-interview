#!/usr/bin/python3
"""This module for the lockBoxes"""


def canUnlockAll(boxes):
    """return whether all the boxes can be opened or not"""

    hash = {0}
    closed = []

    for idx in range(len(boxes)):
        if idx in hash:
            keys = boxes[idx]
            for key in keys:
                if key < len(boxes) and key not in hash:
                    hash.add(key)
        else:
            closed.append(idx)

    count = len(closed)
    for i in closed:
        if i in hash:
            keys = boxes[i]
            for key in keys:
                hash.add(key)
            count -= 1
    return count == 0
