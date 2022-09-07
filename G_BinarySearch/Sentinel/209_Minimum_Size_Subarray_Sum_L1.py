""" https://leetcode.com/problems/minimum-size-subarray-sum/
prefix sum+binary search to find minimal size
"""
from header import *

class Solution:
    def minSubArrayLen(self, t: int, A: List[int]) -> int:
        prefix = list(accumulate(A, initial=0))
        
        def fn(m):
            for i in range(m, len(prefix)):
                if prefix[i]-prefix[i-m]>=t: return True
            return False
            
        l, r = 0, len(A)+1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l if l!=len(A)+1 else 0