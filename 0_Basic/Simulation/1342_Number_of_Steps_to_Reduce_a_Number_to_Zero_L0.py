""" https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""
class Solution:
    def numberOfSteps(self, x: int) -> int:
        ans = 0
        while x:
            ans += 1
            if x&1: x -= 1
            else: x//=2
        return ans