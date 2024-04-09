""" https://leetcode.com/problems/minimum-score-by-changing-two-elements/
greedy categorization
"""
from header import *


class Solution:
    def minimizeSum(self, A: List[int]) -> int:
        A.sort()
        return min(A[-1] - A[2], A[-3] - A[0], A[-2] - A[1])


"""
[1,4,3]
[1,4,7,8,5]
[59,27,9,81,33]
[58,42,8,75,28]
"""
