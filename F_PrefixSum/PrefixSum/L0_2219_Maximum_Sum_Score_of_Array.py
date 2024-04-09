""" https://leetcode.com/problems/maximum-sum-score-of-array/
compute max of the prefix and suffix sum
"""
from header import *


class Solution:
    def maximumSumScore(self, A: List[int]) -> int:
        prefix = list(accumulate(A, initial=0))
        suffix = list(accumulate(A[::-1], initial=0))[::-1]

        ans = -inf
        for i in range(1, len(prefix)):
            ans = max(ans, max(prefix[i], suffix[i - 1]))
        return ans
