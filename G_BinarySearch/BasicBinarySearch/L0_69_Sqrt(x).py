""" https://leetcode.com/problems/sqrtx/
l, r = 0, x+1 for corner case 0 and 1
return value should be l-1 rather than l
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x + 1
        while l < r:
            m = (l + r) // 2
            if m * m > x:
                r = m
            else:
                l = m + 1
        return l - 1
