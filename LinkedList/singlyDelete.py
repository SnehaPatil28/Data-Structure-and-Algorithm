class LinkedList:
  # delete by data
  def delete(self,key):
    # case 1: head itself contain target value
    curr = self.head
    if curr and curr.data == key:
      self.head = curr.next
      curr = None
      return
    # case 2: search value while keeping track of prev
    prev = None
    while curr and curr.data != key:
      prev = curr
      curr = curr.next
    # case 3: value not present in list
    if not curr:
      return
    prev.next = curr.next
    curr = None

# delete at k value
 def delete_at_k(self,k):
   if self.head is None:
     return
   if k == 0:
     self.head = self.head.next
     return
   temp = self.head
   for _ in range(k-1):
     if temp.next is None:
       return
     temp = temp.next
   if temp.next is not None:
     temp.next = temp.next.next
    
