""" https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
brain teaser: arithmetic progression
"""
from header import *

class Solution:
    def maximizeSum(self, A: List[int], k: int) -> int:
        mx = max(A)
        return int(k*mx+k*(k-1)/2)