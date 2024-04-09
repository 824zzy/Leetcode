""" https://leetcode.com/problems/find-greatest-common-divisor-of-array/
use built-in function gcd
"""
from header import *


class Solution:
    def findGCD(self, A: List[int]) -> int:
        return gcd(min(A), max(A))
