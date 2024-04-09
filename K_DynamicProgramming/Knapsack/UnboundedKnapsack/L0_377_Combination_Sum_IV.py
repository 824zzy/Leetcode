""" https://leetcode.com/problems/combination-sum-iv/
the same as 518.
At state dp(t), the answer depends on all previous states
"""
from header import *


class Solution:
    def combinationSum4(self, A: List[int], target: int) -> int:
        @cache
        def dp(t):
            if t == 0:
                return 1
            ans = 0
            for x in A:
                if t - x >= 0:
                    ans += dp(t - x)
            return ans

        return dp(target)
