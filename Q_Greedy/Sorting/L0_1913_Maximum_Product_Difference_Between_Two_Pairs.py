""" https://leetcode.com/problems/maximum-product-difference-between-two-pairs/submissions/
find the largest and second largest number and the smallest and second smallest number
"""
from header import *


class Solution:
    def maxProductDifference(self, A: List[int]) -> int:
        A.sort()
        return A[-1] * A[-2] - A[0] * A[1]
