class ValidParenthesis:
  def is_valid(self, exp) -> bool:
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}

    for char in exp:
      if char in "({[":
        stack.append(char)
      elif char in ")}]":
        if not stack:
          return False
        top = stack.pop()
        if pair[char] != top:
          return False
    return len(stack) == 0
          
