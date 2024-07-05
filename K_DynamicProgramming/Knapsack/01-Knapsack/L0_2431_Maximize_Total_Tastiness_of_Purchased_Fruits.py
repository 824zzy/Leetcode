""" https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/
three options knapsack problem:
1. skip the current fruit
2. buy the current fruit but not use coupon
3. buy the current fruit and use coupon
"""
from header import *


class Solution:
    def maxTastiness(self, P: List[int], T: List[int], maxAmt: int, maxCps: int) -> int:
        @cache
        def dp(i, amt, cps):
            if i == len(P):
                return 0
            # skip
            ans = dp(i + 1, amt, cps)
            # buy but not use coupon
            if amt - P[i] >= 0:
                ans = max(ans, T[i] + dp(i + 1, amt - P[i], cps))
            # buy ans use coupon
            if amt - P[i] // 2 >= 0 and cps:
                ans = max(ans, T[i] + dp(i + 1, amt - P[i] // 2, cps - 1))
            return ans

        return dp(0, maxAmt, maxCps)
