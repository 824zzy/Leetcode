""" L0: https://leetcode.com/problems/guess-number-higher-or-lower/
consider middle m as guess api parameter
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l<=r:
            m = (l+r)//2
            val = guess(m)
            if val==0: return m
            elif val==-1: r = m - 1
            else: l = m + 1