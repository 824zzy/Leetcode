""" https://leetcode.com/problems/separate-the-digits-in-an-array/
"""
from header import *


class Solution:
    def separateDigits(self, A: List[int]) -> List[int]:
        return [int(c) for a in A for c in str(a)]
