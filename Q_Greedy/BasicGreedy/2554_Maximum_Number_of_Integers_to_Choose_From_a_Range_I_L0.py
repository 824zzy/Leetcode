""" https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
greedily assign number from small to large
"""
from header import *

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0
        for x in range(1, n+1):
            if x not in banned and x<=maxSum:
                maxSum -= x
                ans += 1
        return ans