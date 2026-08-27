class Stack:
  def __init__(self):
    self.item = []
  def push(self, ele):
      self.item.append(ele)
  def pop(self):
    if not is_empty():
      self.item.pop()
    return "Stack Empty"
  def peek():
    if not is_empty():
      self.item[-1]
    return "Stack Empty"
  def is_empty():
    return len(self.item) == 0
    
