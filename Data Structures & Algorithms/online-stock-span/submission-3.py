class StockSpanner:

    def __init__(self):
        self.stockSpan = [] # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stockSpan and (self.stockSpan[-1][0] <= price):
            span += self.stockSpan[-1][1]
            self.stockSpan.pop()
        self.stockSpan.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)