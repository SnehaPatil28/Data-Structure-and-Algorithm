from collections import deque

class TreeNode:  # Assuming a TreeNode class is defined
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root]) # Initialize queue with root node

    while queue:
        node = queue.popleft() # Process the leftmost node in the queue
        result.append(node.val) # Add the node's value to the result

        if node.left:
            queue.append(node.left) # Add the left child to the queue
        if node.right:
            queue.append(node.right) # Add the right child to the queue

    return result
