""" https://leetcode.com/problems/frog-jump-ii/description/
The best strategy for the frog is to jump skipping one stone.
Therefore, our answer is the longest jump between st[i] and st[i-2].
"""
from header import *


class Solution:
    def maxJump(self, A: List[int]) -> int:
        # when there are only two stones
        ans = A[1] - A[0]
        for i in range(2, len(A)):
            ans = max(ans, A[i] - A[i - 2])
        return ans
