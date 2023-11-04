""" https://leetcode.com/problems/stone-game/
minimax: maximize the profit by minimize opponent profit

take gain with minus sign, so we have options P[i] - dp(i+1, j) and P[j] - dp(i, j-1)
"""
from header import *

class Solution:
    def stoneGame(self, A: List[int]) -> bool:
        @cache
        def dp(i, j):
            if i>j: return 0
            return max(A[i]-dp(i+1, j, 1), A[j]-dp(i, j-1, 1))
        
        return dp(0, len(A)-1)>0