""" https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/
the same as 435: use ma to greedily keep track of maximum end value
"""
from header import *

class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: x[1])
        right_most = -inf
        ans = 0
        for i, j in A:
            if right_most<i:
                ans += 1
                right_most = j
        return ans