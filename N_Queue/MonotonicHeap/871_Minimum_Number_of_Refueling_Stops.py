""" https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""
from header import *


class Solution:
    def minRefuelStops(self, t: int, cur: int, S: List[List[int]]) -> int:
        pq = []
        ans = i = 0
        while cur < t:
            while i < len(S) and S[i][0] <= cur:
                heappush(pq, -S[i][1])
                i += 1
            if not pq:
                return -1
            cur += -heappop(pq)
            ans += 1
        return ans
