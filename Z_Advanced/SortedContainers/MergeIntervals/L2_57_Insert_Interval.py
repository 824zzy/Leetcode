""" https://leetcode.com/problems/insert-interval/
create a sorted list and update intervals once
"""
from sortedcontainers import SortedList


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        SL = SortedList(intervals)
        l, r = newInterval
        k = SL.bisect_left([l, r])

        while k < len(SL) and SL[k][0] <= r:
            ll, rr = SL.pop(k)
            r = max(r, rr)
        if k and l <= SL[k - 1][1]:
            ll, rr = SL.pop(k - 1)
            l = ll
            r = max(r, rr)
        SL.add([l, r])
        return SL
