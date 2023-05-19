""" https://leetcode.com/problems/maximum-or/
1. Greedily apply the operation to one of the numbers in the array.
2. Decompose the array to prefix and suffix to find the maximum OR.
"""
from header import *

class Solution:
    def maximumOr(self, A: List[int], k: int) -> int:
        suf = [0] * len(A)
        for i in range(len(A)-2, -1, -1):
            suf[i] = suf[i+1] | A[i+1]
            
        ans = 0
        pre = 0
        for i in range(len(A)):
            ans = max(ans, pre|A[i]<<k|suf[i])
            pre |= A[i]
        return ans
