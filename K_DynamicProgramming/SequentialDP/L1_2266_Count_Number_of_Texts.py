""" https://leetcode.com/problems/count-number-of-texts/
The result is solely impacted by the following four digits at index i.
Note that using MOD everywhere can save you a lot of time!

Time: O(4*n)
"""
from header import *


class Solution:
    def countTexts(self, A: str) -> int:
        mp = set(["2", "22", "222",
                  "3", "33", "333",
                  '4', '44', '444',
                  '5', '55', '555',
                  '6', '66', '666',
                  '7', '77', '777', '7777',
                  '8', '88', '888',
                  '9', '99', '999', '9999'])
        MOD = 10**9 + 7

        @cache
        def dp(i):
            if i >= len(A):
                return 1
            ans = 0
            if i + 1 <= len(A) and A[i:i + 1] in mp:
                ans += dp(i + 1) % MOD
            if i + 2 <= len(A) and A[i:i + 2] in mp:
                ans += dp(i + 2) % MOD
            if i + 3 <= len(A) and A[i:i + 3] in mp:
                ans += dp(i + 3) % MOD
            if i + 4 <= len(A) and A[i:i + 4] in mp:
                ans += dp(i + 4) % MOD
            return ans % MOD

        return dp(0) % MOD

# efficient solution from ye, boost up by group by


class Solution:
    def countTexts(self, A: str) -> int:
        @cache
        def dp(i, k):
            if i < 0:
                return 0
            elif i == 0:
                return 1
            ans = 0
            for j in range(1, k + 1):
                ans += dp(i - j, k) % (10**9 + 7)
            return ans

        ans = 1
        for key, grp in groupby(A):
            if key in "79":
                k = 4
            else:
                k = 3
            ans = (ans * dp(len(list(grp)), k)) % (10**9 + 7)
        return ans % (10**9 + 7)
