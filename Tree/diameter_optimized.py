def diameter_optimized(root):
    """Calculates the diameter of a tree using the optimized approach."""
    diameter = [0]  # Use a list to store diameter, so it can be modified in the inner function

    def height(node):
        """Calculates the height and updates the diameter."""
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        # Diameter through the current node
        diameter[0] = max(diameter[0], left + right)

        # Return the height of the current node
        return max(left, right) + 1

    height(root)
    return diameter[0]
