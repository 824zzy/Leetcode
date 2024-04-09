""" https://leetcode.com/problems/find-the-peaks/
linear scan simulation
"""
from header import *


class Solution:
    def findPeaks(self, A: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                ans.append(i)
        return ans


"""
[2,4,4]
[1,4,3,8,5]
"""
