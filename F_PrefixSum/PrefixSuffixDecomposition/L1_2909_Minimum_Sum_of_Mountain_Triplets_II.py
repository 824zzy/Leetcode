""" https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/
prefix suffix decomposition + greedy
"""
from header import *

class Solution:
    def minimumSum(self, A: List[int]) -> int:
        suf = [0]*len(A)
        mn = inf
        for i in reversed(range(len(A))):
            mn = min(mn, A[i])
            suf[i] = mn
        
        ans = inf
        mn = inf
        for i in range(len(A)):
            mn = min(mn, A[i])
            if A[i]>suf[i] and A[i]>mn:
                ans = min(ans, A[i]+suf[i]+mn)
        return ans if ans!=inf else -1
        
        
        
"""
[5,4,4,4,4,2]
[2,2,2,2,2,2]
[x,x,x,x,x,x]
"""