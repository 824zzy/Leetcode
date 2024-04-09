""" https://leetcode.com/problems/two-sum/
subtrahend as key and minuend's index as value
"""
from header import *


class Solution:
    def twoSum(self, A: List[int], t: int) -> List[int]:
        seen = {}
        for i in range(len(A)):
            if A[i] in seen:
                return [seen[A[i]], i]
            seen[t - A[i]] = i
