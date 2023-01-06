""" https://leetcode.com/problems/non-overlapping-intervals/submissions/
the same as 452
use ma to greedily keep track of maximum end value
or use an array to greedily find legit meeting end time
"""
from header import *

class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: x[1])
        ans = 0
        ma = -inf
        for i, j in A:
            if ma<=i: ma = j
            else: ans += 1
        return ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        A = []
        for i, j in intervals:
            if not A or A[-1]<=i:
                A.append(j)
        return len(intervals)-len(A)