""" https://leetcode.com/problems/number-of-1-bits/
check if lowest bit of n is 1
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans