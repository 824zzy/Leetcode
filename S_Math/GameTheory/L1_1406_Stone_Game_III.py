""" https://leetcode.com/problems/stone-game-iii/
minimax problem, dp(i) is the max gain of the first player when starting at i
"""
from header import *

class Solution:
    def stoneGameIII(self, A: List[int]) -> str:
        A = list(accumulate(A, initial=0))
        
        @cache
        def dp(i):
            if i>=len(A): return 0
            ans = -inf
            for j in 1,2,3:
                ans = max(ans, A[min(i+j, len(A)-1)]-A[i]-dp(i+j))
            return ans
        
        if dp(0)>0:
            return "Alice"
        elif dp(0)<0:
            return "Bob"
        else:
            return "Tie"