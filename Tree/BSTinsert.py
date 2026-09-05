class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)  # Create a new node if the spot is empty
    if value < root.value:
        root.left = insert(root.left, value)  # Go left if value is smaller
    else:
        root.right = insert(root.right, value) # Go right if value is larger
    return root # Return the (potentially modified) root
