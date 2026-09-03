class TreeNod:
  def __init__(self,data):
    self.data = data
    self.left = self.right = None
  def insert_at_root(self,data):
    if self.root is None:
      self.root = TreeNone(data)
    self.insert(self.root,data)
  def insert(self,node, data):
    if data < node.data:
      if node.left is None:
        node.left = TreeNode(data)
      self.insert(node.left, data)
    else:
      if node.right is None:
        node.right = TreeNode(data)
      self.insert(node.right, data)
    return node

  def delete(self,node,data):
    if node is None:
      return
    if data < node.data:
      node.left = delete(node.left, data)
    elif data > node.data:
      node.right = delete(node.right, data)
    else:
      if node.left is None:
        return node.right
      elif node.rigth is None:
        return node.left
      successor = node.right
      while successor.left is not None:
        successor = successor.left
      node.data = successor.data
      node.right = delete(node.right, successor.data)
    retrun node
    
