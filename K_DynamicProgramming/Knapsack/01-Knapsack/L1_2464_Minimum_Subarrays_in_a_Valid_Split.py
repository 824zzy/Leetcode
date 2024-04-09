""" https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/description/
"""
from header import *


class Solution:
    def validSubarraySplit(self, A: List[int]) -> int:
        @cache
        def dp(i, prev):
            if i == len(A) - 1:
                if gcd(prev, A[i]) > 1:
                    return 1
                else:
                    return inf

            # skip
            ans = dp(i + 1, prev)
            # split
            if gcd(prev, A[i]) > 1:
                ans = min(ans, 1 + dp(i + 1, A[i + 1]))
            return ans

        ans = dp(0, A[0])
        return ans if ans != inf else -1
