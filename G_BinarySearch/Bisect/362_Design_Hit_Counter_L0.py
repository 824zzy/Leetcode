""" https://leetcode.com/problems/design-hit-counter/
use binary search to find the index of t-300
"""
from header import *

class HitCounter:
    def __init__(self):
        self.cnt = []

    def hit(self, t: int) -> None:
        self.cnt.append(t)

    def getHits(self, t: int) -> int:
        idx = bisect_right(self.cnt, t-300)
        return len(self.cnt)-idx