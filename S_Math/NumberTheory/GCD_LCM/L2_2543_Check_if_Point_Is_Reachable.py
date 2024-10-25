""" https://leetcode.com/problems/check-if-point-is-reachable/
1.  (x, y-x), (x - y, y) ==> find GCD of x, y
2.  (2*x, y), (x, 2*y) ==> check if the GCD is power of 2
"""
from header import *


class Solution:
    def isReachable(self, x: int, y: int) -> bool:
        n = gcd(x, y)
        return n & (n - 1) == 0
