def find_ceil(root, key):
    if root is None:
        return None  # No ceil if the tree is empty
    if root.value == key:
        return root.value  # Key is the ceil
    if root.value < key:
        return find_ceil(root.right, key)  # Search right subtree
    ceil_val = find_ceil(root.left, key)  # Search left subtree
    return ceil_val if ceil_val is not None else root.value  # Return ceil if found, otherwise the current no
