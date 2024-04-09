""" https://leetcode.com/problems/maximum-ice-cream-bars/
sort and greedy
"""
from header import *


class Solution:
    def maxIceCream(self, A: List[int], coins: int) -> int:
        ans = 0
        for x in sorted(A):
            if coins >= x:
                ans += 1
                coins -= x
            else:
                break
        return ans
