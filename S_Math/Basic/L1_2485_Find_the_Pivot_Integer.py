""" https://leetcode.com/problems/find-the-pivot-integer/description/
Observation: 2*( x*(x+1)/2 ) - x = n*(n+1)/2 ===> x = sqrt(n*(n+1)/2)
"""
from header import *

# O(1) math solution
class Solution:
    def pivotInteger(self, n: int) -> int:
        val = n*(n+1)//2
        return isqrt(val) if isqrt(val)**2 == val else -1 

# brute force solution for small n
class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = list(accumulate(range(1, n+1)))
        suffix = list(accumulate(reversed(range(1, n+1))))[::-1]
        for i, (x, y) in enumerate(zip(prefix, suffix)):
            if x==y:
                return i+1
        return -1