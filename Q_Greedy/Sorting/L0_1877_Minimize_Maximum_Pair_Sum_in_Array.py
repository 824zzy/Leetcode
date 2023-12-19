""" https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
the minimize pair sum is A[i] + A[n-1-i]
"""
from header import *

class Solution:
    def minPairSum(self, A: List[int]) -> int:
        A.sort()
        return max(A[i]+A[~i]for i in range(len(A)//2))