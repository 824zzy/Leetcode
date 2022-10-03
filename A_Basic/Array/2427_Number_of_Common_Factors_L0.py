""" https://leetcode.com/problems/number-of-common-factors/
For each integer in range [1, min(a, b)+1], check if it’s divisible by both A and B.
"""
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, min(a, b)+1):
            if a%i==0 and b%i==0:
                ans += 1
        return ans