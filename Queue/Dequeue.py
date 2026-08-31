from collection import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
top_element = queue.pop()
if len(queue) == 0:
  print("Empty")


## used fot both stack and queue as it is double ended queue
