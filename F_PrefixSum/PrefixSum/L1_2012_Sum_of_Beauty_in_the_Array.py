""" https://leetcode.com/problems/sum-of-beauty-in-the-array/
use prefix max and suffix min to calculate the beauty of elements
"""
from header import *

class Solution:
    def sumOfBeauties(self, A: List[int]) -> int:
        prefix = list(accumulate(A, max))
        suffix = list(accumulate(A[::-1], min))[::-1]
        ans = 0
        for i in range(1, len(A)-1):
            if prefix[i-1]<A[i]<suffix[i+1]:
                ans += 2
            elif A[i-1]<A[i]<A[i+1]:
                ans += 1
        return ans