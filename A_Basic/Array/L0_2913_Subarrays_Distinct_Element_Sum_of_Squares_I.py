""" https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
simulation
"""
from header import *

class Solution:
    def sumCounts(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)+1):
                x = len(set(A[i:j]))
                ans += x*x
        return ans