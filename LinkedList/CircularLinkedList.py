class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class CircularLinkedList:
  def __init__(self):
    self.head = None
  def insert(self, data, pos):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      new_node.next = new_node
      return
    curr = self.head
    for _ in range(pos -1):
      curr = curr.next
    new_node.next = curr.next
    curr.next = new_node

  def delete(self,pos):
    if not self.head:
      return
    if pos == 0:
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      temp.next = self.head.next
      self.head = self.head.next
      return
    curr = self.head
    for _ in range(pos - 1):
      curr = curr.next
    curr.next = curr.next.next
