# case1:
def delete_leaf(parent, node):
    """Deletes a leaf node from the BST."""
    if parent.left == node:
        parent.left = None  # Node is the left child
    else:
        parent.right = None # Node is the right child

# case2:
def delete_one_child(parent, node):
    """Deletes a node with one child from the BST."""
    child = node.left if node.left else node.right # Determine the child
    if parent.left == node:
        parent.left = child # Node is the left child
    else:
        parent.right = child # Node is the right child

# case3:
def find_min(node):
    """Finds the in-order successor (minimum value in the subtree)."""
    while node.left:
        node = node.left
    return node

def delete_two_children(node_to_delete):
    """Deletes a node with two children from the BST."""
    successor = find_min(node_to_delete.right) # Find the in-order successor
    node_to_delete.value = successor.value # Replace the node's value
    # Now, delete the successor node (which is a leaf or has one child)
    # This part would involve recursively calling the delete function
    # on the successor's parent.  This is a simplified example.
