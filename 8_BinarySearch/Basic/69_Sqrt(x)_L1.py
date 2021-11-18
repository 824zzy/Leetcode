""" https://leetcode.com/problems/sqrtx/
note that return value should be l-1 rather than l
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l<=r:
            m = (l+r)//2
            if m*m==x: return m
            elif m*m<x: l = m + 1
            else: r = m - 1
        return l-1