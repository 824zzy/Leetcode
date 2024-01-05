""" https://leetcode.com/problems/increasing-triplet-subsequence/
greedy + prefix suffix decomposition
"""
from header import *

class Solution:
    def increasingTriplet(self, A: List[int]) -> bool:
        pre = []
        suf = []
        mn = inf
        mx = -inf
        for x, y in zip(A, A[::-1]):
            mn = min(mn, x)
            mx = max(mx, y)
            pre.append(mn)
            suf.append(mx)
        suf.reverse()
        
        for i, (p, s) in enumerate(zip(pre, suf)):
            if p<A[i]<s:
                return True
        return False