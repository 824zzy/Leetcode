""" https://leetcode.com/problems/find-median-from-data-stream/
maintain a sorted list of data stream
"""
from header import *


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.L, num)

    def findMedian(self) -> float:
        if len(self.L) % 2 != 0:
            return self.L[len(self.L) // 2]  # odd
        else:
            return (self.L[len(self.L) // 2] +
                    self.L[len(self.L) // 2 - 1]) / 2  # even


# sorted containers implementation
class MedianFinder:
    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        l = len(self.sl)
        if l & 1:
            return self.sl[l // 2]
        else:
            return (self.sl[l // 2 - 1] + self.sl[l // 2]) / 2
