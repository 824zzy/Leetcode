""" https://leetcode.com/problems/count-stepping-numbers-in-range/
digits dp with lower and upper bound and leading zero
"""
from header import *


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7

        high = str(high)
        n = len(high)
        low = str(low).zfill(n)

        @cache
        def dfs(i, limit_low, limit_high, is_num, pre):
            if i == n:
                return is_num
            ans = 0
            if not is_num and low[i] == '0':
                ans += dfs(i + 1, True, False, False, None)
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            d0 = 0 if is_num else 1
            for d in range(max(d0, lo), hi + 1):
                if pre is None or abs(d - pre) == 1:
                    ans += dfs(i + 1, limit_low and d == lo,
                               limit_high and d == hi, True, d)
            return ans % MOD
        return dfs(0, True, True, False, None) % MOD
