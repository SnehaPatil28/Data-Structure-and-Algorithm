from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def spiral_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True # Flag to track traversal direction

    while queue:
        level_size = len(queue)
        level = deque() # Use a deque for efficient appending at both ends

        for _ in range(level_size):
            node = queue.popleft()

            if left_to_right:
                level.append(node.val) # Append to the right (left to right)
            else:
                level.appendleft(node.val) # Append to the left (right to left)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(level) # Add the level's values to the result
        left_to_right = not left_to_right # Switch direction for the next level

    return result
