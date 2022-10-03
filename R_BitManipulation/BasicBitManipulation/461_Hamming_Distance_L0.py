""" https://leetcode.com/problems/hamming-distance/
count how many 1s in XOR of x and y
or check if lowest bit of x and y are the same
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        ans = 0
        while diff:
            ans += diff ^ 1
            diff >>= 1
        return ans

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            ans += x&1!=y&1
            x, y = x>>1, y>>1
        return ans