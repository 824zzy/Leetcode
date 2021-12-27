"""L1: https://leetcode.com/problems/bitwise-and-of-numbers-range/
find the left most same bits of m and n.
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m!=n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift