""" https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/
has at least one trailing zero ==> at least two even numbers
"""
from header import *

class Solution:
    def hasTrailingZeros(self, A: List[int]) -> bool:
        cnt = 0
        for x in A:
            if x&1==0:
                cnt += 1
        return cnt>1
        