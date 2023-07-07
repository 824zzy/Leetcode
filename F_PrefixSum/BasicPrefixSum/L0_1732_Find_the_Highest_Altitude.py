""" https://leetcode.com/problems/find-the-highest-altitude/
"""
from header import *

class Solution:
    def largestAltitude(self, A: List[int]) -> int:
        A = list(accumulate(A, initial=0))
        return max(A)