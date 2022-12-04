""" https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
1. calculate the target skill
2. greedily assign lowest and highest player to the same team
"""
from header import *

class Solution:
    def dividePlayers(self, A: List[int]) -> int:
        t, m = divmod(sum(A), len(A)//2)
        if m: return -1
        
        A.sort()
        ans = 0
        for i in range(len(A)//2):
            if A[i]+A[~i]!=t: return -1
            ans += A[i]*A[~i]
        return ans