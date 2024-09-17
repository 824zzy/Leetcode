""" https://leetcode.com/problems/minimum-time-difference/
simulation: 1. convert time to minutes 2. sort 3. find the minimum difference
"""

from header import *


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def fn(t):
            h, m = t.split(":")
            h, m = int(h), int(m)
            return h * 60 + m

        A = [fn(t) for t in timePoints]
        A.sort()
        # corner case: the last and first element
        ans = 1440 - A[-1] + A[0]
        for i in range(len(A) - 1):
            ans = min(ans, min(A[i + 1] - A[i], 1440 - A[i + 1] + A[i]))
        return ans


"""
["23:59","00:00"]
["00:00","23:59","00:00"]
["12:12","12:13"]
["00:00","04:00","22:00"]
["05:31","22:08","00:35"]
"""
