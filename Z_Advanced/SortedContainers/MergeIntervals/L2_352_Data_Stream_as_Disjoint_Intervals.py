""" https://leetcode.com/problems/data-stream-as-disjoint-intervals/
"""
from sortedcontainers import SortedList


class SummaryRanges:
    def __init__(self):
        self.A = SortedList()

    def addNum(self, val: int) -> None:
        left, right = val, val
        k = self.A.bisect_left((left, right))

        while k < len(self.A) and self.A[k][0] <= right + 1:
            l, r = self.A.pop(k)
            right = max(right, r)

        if k and left <= self.A[k - 1][1] + 1:
            l, r = self.A.pop(k - 1)
            left = l
            right = max(right, r)

        self.A.add((left, right))

    def getIntervals(self) -> List[List[int]]:
        return self.A
