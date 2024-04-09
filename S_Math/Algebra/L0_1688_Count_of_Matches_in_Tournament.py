""" https://leetcode.com/problems/count-of-matches-in-tournament/
"""
from header import *


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += n // 2
            n -= n // 2
        return ans
