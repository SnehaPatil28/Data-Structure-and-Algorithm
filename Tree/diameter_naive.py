def height(node):
    """Calculates the height of a subtree."""
    if not node:
        return 0
    return max(height(node.left), height(node.right)) + 1

def diameter_naive(root):
    """Calculates the diameter of a tree using the naive approach."""
    if not root:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    # Diameter through the current node
    diameter_through_root = left_height + right_height

    # Diameter might be in the left or right subtrees
    left_diameter = diameter_naive(root.left)
    right_diameter = diameter_naive(root.right)

    # Return the maximum diameter
    return max(diameter_through_root, max(left_diameter, right_diameter))
