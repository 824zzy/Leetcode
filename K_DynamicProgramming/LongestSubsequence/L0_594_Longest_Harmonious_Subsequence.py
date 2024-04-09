""" https://leetcode.com/problems/longest-harmonious-subsequence/
greedy
"""
from header import *


class Solution:
    def findLHS(self, A: List[int]) -> int:
        cnt = Counter(A)
        ans = 0
        for k, v in cnt.items():
            if cnt[k + 1]:
                ans = max(ans, v + cnt[k + 1])
            if cnt[k - 1]:
                ans = max(ans, v + cnt[k - 1])
        return ans
