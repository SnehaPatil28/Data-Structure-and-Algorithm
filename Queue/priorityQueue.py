import heapq as hp
class PriorityQueue:
  def __init__(self):
    self.queue = []
  def add(self,data,priority):
    hp.heappush(self.queue, (priority, data)
  def pop(self):
    return hp.heappop(self.queue[1] self.queue else None)
    
