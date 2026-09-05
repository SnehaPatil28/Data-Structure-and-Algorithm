def find_floor(root, key):
    if root is None:
        return None  # No floor if the tree is empty
    if root.value == key:
        return root.value  # Key is the floor
    if root.value > key:
        return find_floor(root.left, key)  # Search left subtree
    floor_val = find_floor(root.right, key)  # Search right subtree
    return floor_val if floor_val is not None else root.value  # Return floor if found, otherwise the current 
