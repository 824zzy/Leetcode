""" https://leetcode.com/problems/nth-magical-number/
binary search + math(inclusive-exclusive principle)

use a*b//gcd(a, b) to find the joint set.
"""


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        ab = a * b // gcd(a, b)
        l, r = min(a, b), n * min(a, b)
        while l < r:
            m = (l + r) // 2
            if m // a + m // b - m // ab >= n:
                r = m
            else:
                l = m + 1
        return l % (10**9 + 7)
