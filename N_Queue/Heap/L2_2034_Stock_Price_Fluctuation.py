""" https://leetcode.com/problems/stock-price-fluctuation/
while hashmap(always updated) timestamp's value not equals to current maximum/minimum heap value, pop the heap.
"""


class StockPrice:
    def __init__(self):
        self.SP = {}
        self.cur = -float("inf")
        self.max = []
        self.min = []

    def update(self, t: int, p: int) -> None:
        self.SP[t] = p
        self.cur = max(self.cur, t)
        heapq.heappush(self.max, (-p, t))
        heapq.heappush(self.min, (p, t))

    def current(self) -> int:
        return self.SP[self.cur]

    def maximum(self) -> int:
        while self.SP[self.max[0][1]] != -self.max[0][0]:
            heappop(self.max)
        return -self.max[0][0]

    def minimum(self) -> int:
        while self.SP[self.min[0][1]] != self.min[0][0]:
            heappop(self.min)
        return self.min[0][0]
