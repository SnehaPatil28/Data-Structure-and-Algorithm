class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Get height of a node
def get_height(node):
    if node is None:
        return 0

    return node.height


# Get balance factor
def get_balance(node):
    if node is None:
        return 0

    return get_height(node.left) - get_height(node.right)


# Right Rotation
def right_rotate(y):

    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(
        get_height(y.left),
        get_height(y.right)
    )

    x.height = 1 + max(
        get_height(x.left),
        get_height(x.right)
    )

    return x


# Left Rotation
def left_rotate(x):

    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(
        get_height(x.left),
        get_height(x.right)
    )

    y.height = 1 + max(
        get_height(y.left),
        get_height(y.right)
    )

    return y


# Insert into AVL Tree
def insert(node, key):

    # Step 1: Normal BST insertion
    if node is None:
        return TreeNode(key)

    if key < node.key:
        node.left = insert(node.left, key)

    elif key > node.key:
        node.right = insert(node.right, key)

    else:
        # Duplicate values are not allowed
        return node

    # Step 2: Update height
    node.height = 1 + max(
        get_height(node.left),
        get_height(node.right)
    )

    # Step 3: Get balance factor
    balance = get_balance(node)

    # Step 4: Check four rotation cases

    # LL Case
    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    # RR Case
    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    # LR Case
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # RL Case
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


# Inorder Traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Main program
root = None

root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 10)
root = insert(root, 25)
root = insert(root, 28)
root = insert(root, 40)
root = insert(root, 50)

print("Inorder traversal:")
inorder(root)
