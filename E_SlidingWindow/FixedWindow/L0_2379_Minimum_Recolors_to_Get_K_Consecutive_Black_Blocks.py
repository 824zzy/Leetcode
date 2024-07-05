""" https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""
from header import *


class Solution:
    def minimumRecolors(self, A: str, k: int) -> int:
        cntw = 0
        ans = inf
        for i in range(len(A)):
            if A[i] == "W":
                cntw += 1
            if i >= k - 1:
                ans = min(ans, cntw)
                if A[i - k + 1] == "W":
                    cntw -= 1
        return ans
