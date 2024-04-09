""" https://leetcode.com/problems/smallest-number-in-infinite-set/
it is actually an easy problem due to 1<=num<=1000
"""
from header import *


class SmallestInfiniteSet:
    def __init__(self):
        self.sl = SortedList()
        self.idx = 1

    def popSmallest(self) -> int:
        if self.sl:
            return self.sl.pop(0)
        else:
            self.idx += 1
            return self.idx - 1

    def addBack(self, num: int) -> None:
        if num < self.idx and num not in self.sl:
            self.sl.add(num)


class SmallestInfiniteSet:
    def __init__(self):
        self.sl = SortedList(range(1, 1001))

    def popSmallest(self) -> int:
        return self.sl.pop(0)

    def addBack(self, num: int) -> None:
        if num not in self.sl:
            self.sl.add(num)
