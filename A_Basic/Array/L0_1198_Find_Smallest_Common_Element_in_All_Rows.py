""" https://leetcode.com/problems/find-smallest-common-element-in-all-rows/\
find set intersection of all rows
"""
from header import *

class Solution:
    def smallestCommonElement(self, A: List[List[int]]) -> int:
        seen = set(A[0])
        for i in range(1, len(A)):
            seen &= set(A[i])
        return min(seen, default=-1)