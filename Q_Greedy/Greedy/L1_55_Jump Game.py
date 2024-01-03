""" https://leetcode.com/problems/jump-game/
Greedily find the maximum reachable index.
Return false immediately if cannot reach current num.
"""
from header import *

class Solution:
    def canJump(self, A: List[int]) -> bool:
        j = 0
        for i, x in enumerate(A):
            if i>j: return False
            j = max(j, i+x)
        return True