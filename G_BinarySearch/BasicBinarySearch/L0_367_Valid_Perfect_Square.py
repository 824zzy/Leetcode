""" https://leetcode.com/problems/valid-perfect-square/
straightforward binary search
"""
from header import *

class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        def fn(m):
            return m*m>=x
            
        l, r = 0, x
        while l<r:
            m = (l+r)//2
            if fn(m):
                r = m
            else:
                l = m+1
        return l*l==x