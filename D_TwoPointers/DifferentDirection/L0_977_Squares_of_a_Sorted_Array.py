""" https://leetcode.com/problems/squares-of-a-sorted-array/
find larger absolute value of two pointers
"""
from header import *


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                ans.append(A[l]**2)
                l += 1
            else:
                ans.append(A[r]**2)
                r -= 1
        return ans[::-1]
