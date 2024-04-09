""" https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
simulation
"""
from header import *


class Solution:
    def average(self, A: List[int]) -> float:
        A.sort()
        return sum(A[1:-1]) / (len(A) - 2)
