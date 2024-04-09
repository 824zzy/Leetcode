""" https://leetcode.com/problems/factorial-trailing-zeroes/
continuously count five factors since we don't need to care about 2 factors
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n != 0:
            n = n // 5
            ans += n
        return ans
