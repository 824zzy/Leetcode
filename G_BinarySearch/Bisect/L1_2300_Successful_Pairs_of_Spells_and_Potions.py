""" https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
"""
from header import *


class Solution:
    def successfulPairs(self, S: List[int], P: List[int], k: int) -> List[int]:
        P.sort()
        ans = []
        for s in S:
            kk = k / s
            idx = bisect_left(P, kk)
            ans.append(len(P) - idx)
        return ans
