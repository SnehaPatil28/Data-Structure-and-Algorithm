def recursive_search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    elif target < node.value:
        return recursive_search(node.left, target)
    else:
        return recursive_search(node.right, target)


def iterative_search(root, target):
    current = root
    while current:
        if current.value == target:
            return True
        elif target < current.value:
            current = current.left
        else:
            current = current.right
    return False
