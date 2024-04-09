""" https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
digit dp which consider leading zero

ensure the number has at least one 1 and previous digit is not the same
"""
from header import *

# new template


class Solution:
    def findIntegers(self, n: int) -> int:
        high = bin(n)[2:]
        n = len(high)

        @cache
        def dfs(i, limit_high, is_num, pre):
            if i == n:
                return is_num
            ans = 0
            if not is_num:
                ans += dfs(i + 1, False, False, pre)
            hi = int(high[i]) if limit_high else 1
            for d in range(hi + 1):
                if pre != d:
                    ans += dfs(i + 1, limit_high and d ==
                               int(high[i]), d == 1, d)
            return ans
        return dfs(0, True, False, None) + 1


# old template
class Solution:
    def findIntegers(self, n: int) -> int:
        A = list(map(int, bin(n)[2:]))

        @cache
        def dp(i, isPrefix, isBigger, hasOne):
            if i == len(A):
                return 0
            ans = 0
            for d in range(i == 0, 2):
                _isPrefix = isPrefix and d == A[i]
                _isBigger = isBigger or (isPrefix and d > A[i])
                if not(
                    hasOne and d == 1) and not(
                    i == len(A) -
                        1 and _isBigger):
                    ans += 1 + dp(i + 1, _isPrefix, _isBigger, d)
            return ans
        # add one for 0
        return dp(0, True, False, False) + 1
