""" https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
knap-sack dp
"""

from header import *


class Solution:
    def subsequencePairCount(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(i, x, y):
            if i == len(A):
                return x == y
            # skip
            ans = dp(i + 1, x, y)
            # save in x
            ans += dp(i + 1, gcd(x, A[i]), y)
            # save in y
            ans += dp(i + 1, x, gcd(y, A[i]))
            return ans % MOD

        return dp(0, 0, 0) - 1
