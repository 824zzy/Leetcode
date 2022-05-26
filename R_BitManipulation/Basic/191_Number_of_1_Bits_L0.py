""" https://leetcode.com/problems/number-of-1-bits/
right shift n while checking if lowest bit of n is 1 by `n&1`
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans