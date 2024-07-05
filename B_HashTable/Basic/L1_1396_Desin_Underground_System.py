""" https://leetcode.com/problems/design-underground-system/
use two hash tables

1. the first hash table is for saving the check-in time for a customer
2. the second hash table is for updating the prefix time sum between two stations.
"""
from header import *


class UndergroundSystem:
    def __init__(self):
        self.mp = {}
        self.ans = defaultdict(lambda: [0])

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.mp[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t1: int) -> None:
        startStation, t0 = self.mp.pop(id)
        self.ans[startStation + "|" + endStation].append(
            self.ans[startStation + "|" + endStation][-1] + (t1 - t0)
        )

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        x = self.ans[startStation + "|" + endStation][-1]
        t = len(self.ans[startStation + "|" + endStation]) - 1
        return x / t
