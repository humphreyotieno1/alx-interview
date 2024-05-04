#!/usr/bin/python3

def canUnlockAll(boxes):
    # Create a set to keep track of the boxes that have been visited
    visited = set()

    # Add the first box to the visited set
    visited.add(0)

    # Create a stack to store the boxes to be visited
    stack = [0]

    # Iterate through the stack until it is empty
    while stack:
        # Pop the top box from the stack
        current_box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and the box has not been visited yet
            if key < len(boxes) and key not in visited:
                # Add the box to the visited set
                visited.add(key)

                # Add the box to the stack to be visited later
                stack.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)
