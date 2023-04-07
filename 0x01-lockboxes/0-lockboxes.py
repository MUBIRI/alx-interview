#!/usr/bin/python3
""" Lockboxes problem solution"""


def canUnlockAll(boxes):
    """Determines wether  all the boxes can be opened"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for n in range(1, len(boxes) - 1):
        unlocked = False
        for a in range(len(boxes)):
            unlocked = n in boxes[a] and n != a
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True
