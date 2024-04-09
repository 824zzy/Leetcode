""" https://leetcode.com/problems/maximum-sum-circular-subarray/
compute both maximum contiguous subarray and minimum contiguous subarray
"""
from header import *


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        mx = mn = -inf
        vx = vn = 0
        for x in A:
            vx = max(0, vx) + x
            vn = max(0, vn) - x
            mx = max(mx, vx)
            mn = max(mn, vn)
        return mx if mx < 0 else max(mx, sum(A) + mn)
