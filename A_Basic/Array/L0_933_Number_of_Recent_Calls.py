""" https://leetcode.com/problems/number-of-recent-calls/
keep queue by t-3000 > self.queue[0]
"""


class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - 3000 > self.queue[0]:
            self.queue.pop(0)
        return len(self.queue)
