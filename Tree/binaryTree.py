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
    
