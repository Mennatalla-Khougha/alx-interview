#!/usr/bin/python3
"""This module for the lockBoxes"""


def canUnlockAll(boxes):
    """return whether all the boxes can be opened or not"""

    hash = {0: boxes[0]}

    for idx in boxes:
        for box, keys in list(hash.items()):
            for key in keys:
                if key not in hash:
                    hash[key] = boxes[key]

    return len(hash) == len(boxes)
