""" https://leetcode.com/problems/points-that-intersect-with-cars/
use sweep line to find the number of overlapping intervals at each point.
"""
from header import *


class Solution:
    def numberOfPoints(self, A: List[List[int]]) -> int:
        n = max(x for _, x in A)
        diff = [0] * (n + 2)
        for i, j in A:
            diff[i] += 1
            diff[j + 1] -= 1

        cnt = 0
        ans = 0
        for i in range(1, n + 1):
            cnt += diff[i]
            ans += (cnt > 0)
        return ans


"""
[[3,6],[1,5],[4,7]]
[[1,3],[5,8]]
"""
