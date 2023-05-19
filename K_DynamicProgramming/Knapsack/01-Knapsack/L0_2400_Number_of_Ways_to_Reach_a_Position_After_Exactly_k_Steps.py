""" https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
at index i, we can reach i-1 and i+1.
"""
from header import *

class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        @cache
        def dp(i, k):
            if k==0: return i==e
            return (dp(i+1, k-1)+dp(i-1, k-1))%(10**9+7)
            
        return dp(s, k)%(10**9+7)