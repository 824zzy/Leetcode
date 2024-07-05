""" https://leetcode.com/problems/count-the-number-of-powerful-integers/
digit dp with lower and upper bound
"""
from header import *


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = str(finish)
        n = len(high)
        low = str(start).zfill(n)
        diff = n - len(s)

        @cache
        def dfs(i, limit_low, limit_high):
            if i == n:
                return 1
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            ans = 0
            if i < diff:
                for d in range(lo, min(hi, limit) + 1):
                    ans += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:
                x = int(s[i - diff])
                if lo <= x <= min(hi, limit):
                    ans = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return ans

        return dfs(0, True, True)
