stack = []

def push(ele):
  stack.append(ele)
def pop(ele):
  if not is_empty():
    return stack.pop()
  return "Stack Empty"
def peek:
  if not is_empty():
    return stack[-1]
  return "Steck Empty"
def is_empty():
  return len(stack) == 0
