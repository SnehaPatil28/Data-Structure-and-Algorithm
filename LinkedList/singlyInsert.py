class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def insert_at_begining(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  def inser_after(self, prev_node, data):
    if prev_node is None:
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = new_node
  def insert_at_k(self, data, k):
    new_node = Node(data)
    if k == 0:
      new_node.next = self.head
      self.head = new_node
      return
    temp = self.head
    for _ in range(k-1):
      if temp is None:
        return
      temp = temp.next
    new_node.next = temp.next
    temp.next = new_node
