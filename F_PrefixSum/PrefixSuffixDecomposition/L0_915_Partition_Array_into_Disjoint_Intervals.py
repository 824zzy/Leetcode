""" https://leetcode.com/problems/partition-array-into-disjoint-intervals/
prefix suffix decomposition + greedy
"""

from header import *


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        suf = []
        mn = inf
        for i in range(len(A) - 1, -1, -1):
            mn = min(mn, A[i])
            suf.append(mn)
        suf.reverse()

        mx = 0
        for i in range(len(A) - 1):
            mx = max(mx, A[i])
            if mx <= suf[i + 1]:
                return i + 1


"""
[5,0,3,8,6]
[1,1,1,0,6,12]
[1,1]
"""
