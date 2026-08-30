class LinkedList:
  def search(self,target):
    curr = self.head
    position = 0
    while curr is not None:
      if curr.data == target:
        return f"Found {target} at index {position}"
      curr = curr.next
      position += 1
    return f"{target} not found in list"

  def recursively_search(self, node, target, index = 0):
    if node is None:
      return f"{target} not found in list"
    if node.data == target:
      return f"found {target} at index {index}"
    return self.recursively_search(node.next, target, index += 1)
    
