""" https://leetcode.com/problems/4sum-ii/
1. compute the frequency of -(a+b) using a Counter
2. check if c+d in the Counter
"""
from header import *

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        cnt= Counter()
        for a in A:
            for b in B:
                cnt[-(a+b)] += 1
        for c in C:
            for d in D:
                if c+d in cnt: ans += cnt[c+d]
        return ans