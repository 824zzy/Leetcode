""" https://leetcode.com/problems/online-stock-span/
maintain a monotonic decreasing stack using price and span
"""


class StockSpanner:
    def __init__(self):
        self.stk = []

    def next(self, p: int) -> int:
        span = 1
        while self.stk and self.stk[-1][0] <= p:
            span += self.stk.pop()[1]
        self.stk.append((p, span))
        return span
