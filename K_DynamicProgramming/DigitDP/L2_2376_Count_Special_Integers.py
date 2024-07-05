""" https://leetcode.com/problems/count-special-integers/
dp with leading zero and mask

the same as 357, 1012
"""
from header import *


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        high = str(n)
        n = len(high)
        low = str(0).zfill(n)

        @cache
        def dfs(i, limit_low, limit_high, is_num, mask):
            if i == n:
                return 1 if is_num else 0
            # deal with leading zero
            ans = 0
            if not is_num and low[i] == "0":
                ans += dfs(i + 1, True, False, False, 0)
            # enumerate from lo to high
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            d0 = 0 if is_num else 1
            for d in range(max(lo, d0), hi + 1):
                if mask & (1 << d) == 0:
                    ans += dfs(
                        i + 1,
                        limit_low and d == lo,
                        limit_high and d == hi,
                        True,
                        mask ^ (1 << d),
                    )
            return ans

        return dfs(0, True, True, False, 0)
