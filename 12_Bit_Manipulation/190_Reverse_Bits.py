""" L1: shift and Get lowest bit in x
x & 1
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans <<= 1
            ans += n & 1
            n >>= 1
        return ans

# Pythonic solution
class Solution:
    def reverseBits(self, n):
        n = str(bin(n))[:2]
        n = n.zfill(32)[::-1]
        return int(n, 2)