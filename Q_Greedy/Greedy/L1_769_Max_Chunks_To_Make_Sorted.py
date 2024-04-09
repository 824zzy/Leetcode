""" https://leetcode.com/problems/max-chunks-to-make-sorted/
Iterate the array, if the max(A[0] ~ A[i]) = i,
then we can split the array into two chunks at this index.
"""
from header import *


class Solution:
    def maxChunksToSorted(self, A: List[int]) -> int:
        mx = 0
        ans = 0
        for i, x in enumerate(A):
            mx = max(mx, x)
            if i == mx:
                ans += 1
        return ans
