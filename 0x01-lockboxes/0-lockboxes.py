#!/usr/bin/python3
"""This file contains the canUnloackAll function
"""


def canUnlockAll(boxes):
    """This function checks if all the boxes can be opened"""

    visited = [False] * len(boxes)
    visited[0] = True
    queue = [0]
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
