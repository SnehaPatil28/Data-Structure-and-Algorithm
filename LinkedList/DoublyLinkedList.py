class Node:
  def __init__(self,data):
    self.data = data
    self.next = self.prev = 0
class DoublyLinkedList:
  def __init__(self):
    self.head = None
  def insert_at_head(self,data):
    new_node = Node(data)
    if self.head:
      self.head.prev = new_node
      new_node.next = self.head
    self.head = new_node
  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    curr = self.head
    while curr.next is not None:
      curr = curr.next
    curr.next = new_node
    new_node.prev = curr
  def insert_at_pos(self, data, pos):
    new_node = Node(data)
    if pos == 0:
      if self.head is not None:
        self.head.prev = new_node
        new_node.next = self.head
      self.head = new_node
      return
    curr = self.head
    count = 0
    while curr is not None and count < pos -1:
      curr = curr.next
      count +=1
    if curr is None:
      print("Position out of bound")
      return
    if curr.next is None:
      curr.next = new_node
      new_node.prev = curr
      return
    new_node.next = curr.next
    new_node.prev = curr
    curr.next.prev = new_node
    curr.next = new_node

  def delete(self, key):
    if not self.head:
      return
    curr = self.head
    while curr:
      if curr.data == key:
        if curr.prev:
          curr.prev.next = curr.next
        if curr.next:
          curr.prev.next = curr.next
        if curr == self.head:
          self.head = curr.next
        return
      curr = curr.next
        
      
