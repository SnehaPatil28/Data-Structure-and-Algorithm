class Queue:
  def __init__(self):
    self.item = []
  def enqueue(self,ele):
    self.item.append(ele)
  def dequeue(self):
    if not self.isempty():
      return self.item.pop(0)
    return "Queue empty"
  def peek(self):
    if not self.isempty():
      return self.item(0)
    return "Queue empty"
  def isempty(self):
    return len(self.item) == 0
