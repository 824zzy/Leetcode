""" https://leetcode.com/problems/semi-ordered-permutation/
reading comprehension to find two cases
"""
from header import *

class Solution:
    def semiOrderedPermutation(self, A: List[int]) -> int:
        n = len(A)
        i = A.index(1)
        j = A.index(n)
        return i+n-j-1-(i>j)