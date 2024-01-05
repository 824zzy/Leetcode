""" https://leetcode.com/problems/check-if-it-is-a-good-array/
based on Bezout's lemma, we need to ensure gcd(A)=1
"""
from header import *

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return gcd(*nums)==1