""" https://leetcode.com/problems/painting-the-walls/
dp with pruning
"""
from header import *

class Solution:
    def paintWalls(self, C: List[int], T: List[int]) -> int:
        n = len(C)
        A = sorted(zip(C, T), key=lambda x: (x[0], -x[1]))
        
        @cache
        def dp(i, free):
            if i==n:
                if free>=0:
                    return 0
                else:
                    return inf
            # pruning: have to free is large than remained element
            if free>=n-i: return 0
            # use free
            ans = dp(i+1, free-1)
            # use paid
            ans = min(ans, A[i][0]+dp(i+1, free+A[i][1]))
            return ans
        return dp(0, 0)