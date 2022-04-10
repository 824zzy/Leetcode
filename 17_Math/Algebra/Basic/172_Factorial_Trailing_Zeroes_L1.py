""" https://leetcode.com/problems/factorial-trailing-zeroes/
count five
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n != 0:
            n = n // 5
            ans += n
        return ans