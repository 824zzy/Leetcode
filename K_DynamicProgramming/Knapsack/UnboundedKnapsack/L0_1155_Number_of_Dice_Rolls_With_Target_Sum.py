""" https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
i-th state is only related (i-1)-th state from x==1 to x==k+1
"""
from header import *


class Solution:
    def numRollsToTarget(self, n: int, k: int, t: int) -> int:
        @cache
        def dp(i, sm):
            if sm > t:
                return 0
            if i == n:
                if sm == t:
                    return 1
                else:
                    return 0

            ans = 0
            for x in range(1, k + 1):
                ans += dp(i + 1, sm + x)
            return ans % (10 ** 9 + 7)

        return dp(0, 0) % (10 ** 9 + 7)
