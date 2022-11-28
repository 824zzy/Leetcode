""" https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/description/
only three conditions:
1. n==1, no cuts is needed
2. n==odd, cut n times
3. n==even, cut n//2 times
"""
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n==1: return 0
        elif n&1: return n
        else: return n//2