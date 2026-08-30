class LinkedList:
  def display(self):
    curr = self.head
    while curr:
      print(curr.data)
      curr = curr.next
    print("None")
