""" https://leetcode.com/problems/merge-intervals/
use sweep line to find out where the count is 0 to build intervals
"""
from header import *


class Solution:
    def insert(self, A: List[List[int]], new: List[int]) -> List[List[int]]:
        A += [new]
        SL = []
        for i, j in A:
            SL.extend([(i, 1), (j + 1, -1)])
        SL.sort()

        cnt = 0
        ans = []
        prev = None
        for i, x in SL:
            if prev is None:
                prev = i
            cnt += x
            if not cnt:
                ans.append([prev, i - 1])
                prev = None
        return ans
