""" https://leetcode.com/problems/neighboring-bitwise-xor/
find property of the original and derived array
"""
from header import *

class Solution:
    def doesValidArrayExist(self, A: List[int]) -> bool:
        return reduce(xor, A)==0