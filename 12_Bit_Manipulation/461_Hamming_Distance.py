""" L1: bit-manipulation
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        ans = 0
        while diff:
            ans += diff ^ 1
            diff >>= 1
        return ans

# pythonic
class Solution:
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
