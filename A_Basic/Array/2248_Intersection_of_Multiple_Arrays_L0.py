""" https://leetcode.com/problems/intersection-of-multiple-arrays/
find intersection using set
"""
from header import *

class Solution:
    def intersection(self, A: List[List[int]]) -> List[int]:
        ans = set(A[0])
        for i in range(1, len(A)):
            ans &= set(A[i])
        return sorted(ans)