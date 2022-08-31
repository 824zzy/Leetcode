""" https://leetcode.com/problems/minimum-health-to-beat-game/
"""
from header import *

class Solution:
    def minimumHealth(self, A: List[int], a: int) -> int:
        A.sort()
        return sum(A)-min(a, A[-1])+1