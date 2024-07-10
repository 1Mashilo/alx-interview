#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): List where each element is a list containing keys for other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set([0])
    queue = deque([0])
    
    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key not in visited and key < n:
                visited.add(key)
                queue.append(key)
    
    return len(visited) == n
