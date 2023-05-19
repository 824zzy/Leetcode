""" https://leetcode.com/problems/alternating-digit-sum/
simulation
"""
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        for i, c in enumerate(str(n)):
            if i&1: ans -= int(c)
            else: ans += int(c)
        return ans