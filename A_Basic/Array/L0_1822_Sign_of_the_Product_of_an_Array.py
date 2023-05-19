""" https://leetcode.com/problems/sign-of-the-product-of-an-array/
simulate
"""
from header import *

class Solution:
    def arraySign(self, A: List[int]) -> int:
        x = reduce(mul, A)
        if x>0: return 1
        elif x<0: return -1
        else: return 0