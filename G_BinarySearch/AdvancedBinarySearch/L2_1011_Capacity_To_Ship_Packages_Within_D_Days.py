""" https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
the same as 410
Use binary search to check if the array can be splitted as multiple subarray whose sum is m.
Note that the lower bound is max(A)
"""
from header import *

class Solution:
    def splitArray(self, A: List[int], k: int) -> int:
        def fn(least):
            sm = 0
            _k = 1
            for x in A:
                if sm+x>least:
                    sm = x
                    _k += 1
                else:
                    sm += x
            return _k<=k
                    
        l, r = max(A), sum(A)
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l