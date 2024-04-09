""" https://leetcode.com/problems/longest-increasing-subsequence/
Inspired by 2407,
Time complexity: O(N)
"""
from header import *


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0] * 2 * self.n

    def _set(self, i, val):
        i += self.n
        while i:
            self.T[i] = max(val, self.T[i])
            i //= 2

    def rangeMax(self, l, r):
        ans = 0
        l, r = l + self.n, r + self.n
        while l <= r:
            if l % 2:
                ans, l = max(ans, self.T[l]), l + 1  # if l is right child
            if not r % 2:
                ans, r = max(ans, self.T[r]), r - 1  # if r is left child
            l, r = l // 2, r // 2
        return ans


class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        v2i = {x: i for i, x in enumerate(sorted(set(A)))}
        n = len(v2i)
        ST = SegmentTree(n)
        ans = 1
        for x in A:
            x = v2i[x]
            mx = ST.rangeMax(0, x - 1)
            ST._set(x, mx + 1)
            ans = max(ans, mx + 1)
        return ans
