""" https://leetcode.com/problems/power-of-four/
if n&(n-1) is true, n must be 2**x;
use mask to make sure x is power of 4: 0x55555555
"01010101...."
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n==n&(-n) and n&0x55555555