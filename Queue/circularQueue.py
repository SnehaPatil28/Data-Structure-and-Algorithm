class CircularQueue:
  def __init__(self, size):
    self.queue = [None] * size
    self.front = self.rear - 1
  def enqueue(self,data):
    if self.front == -1:
      self.front = 0
    if (self.rear + 1) % len(self.queue) != self.front:
      self.rear = (self.rear + 1) % len(self.queue)
      self.queue[self.rear] = data
    else:
      return "Queue Null"
  def dequeue(self):
    if self.front == self.rear:
      return "Queue Full"
    elif self.front == -1:
      return "Queue Empty"
    else:
      self.front = (self.front + 1) % len(self.queue)
      return self.queue[self.front]
      
    
  
