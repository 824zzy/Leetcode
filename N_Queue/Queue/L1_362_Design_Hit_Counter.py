""" https://leetcode.com/problems/design-hit-counter/
maintain a deque for simulation
"""
from header import *


class HitCounter:
    def __init__(self):
        self.dq = deque()
        self.ans = 0

    def hit(self, t: int) -> None:
        if self.dq and self.dq[-1][0] == t:
            self.dq[-1][1] += 1
        else:
            self.dq.append([t, 1])
        self.ans += 1

    def getHits(self, t: int) -> int:
        while self.dq and self.dq[0][0] + 300 <= t:
            _, x = self.dq.popleft()
            self.ans -= x
        return self.ans
