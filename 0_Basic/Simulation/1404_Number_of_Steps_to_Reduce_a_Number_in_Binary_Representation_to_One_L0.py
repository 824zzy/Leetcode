""" https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
reduce decimal of s to 1 by simulation
"""
class Solution:
    def numSteps(self, s: str) -> int:
        x = int(s, 2)
        ans = 0
        while x!=1:
            ans += 1
            if x&1: x += 1
            else: x //= 2
        return ans