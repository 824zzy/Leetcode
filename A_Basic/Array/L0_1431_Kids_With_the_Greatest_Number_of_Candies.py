""" https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
check if x+ext>=mx
"""
from header import *

class Solution:
    def kidsWithCandies(self, A: List[int], ext: int) -> List[bool]:
        mx = max(A)
        ans = [False] * len(A)
        for i, x in enumerate(A):
            if x+ext>=mx:
                ans[i] = True
        return ans