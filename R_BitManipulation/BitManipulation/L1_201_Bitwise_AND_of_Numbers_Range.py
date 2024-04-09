""" https://leetcode.com/problems/bitwise-and-of-numbers-range/
The common prefix of m and n given the answer to this problem.
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift
