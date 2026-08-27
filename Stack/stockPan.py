class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span

spanner = StockSpanner()
print(spanner.next(100))  # Returns 1
print(spanner.next(80))   # Returns 1
print(spanner.next(60))   # Returns 1
print(spanner.next(70))   # Returns 2
print(spanner.next(60))   # Returns 1
print(spanner.next(75))   # Returns 4
print(spanner.next(85))   # Returns 6
