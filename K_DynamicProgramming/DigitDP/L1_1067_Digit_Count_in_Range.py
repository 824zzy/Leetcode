""" https://leetcode.com/problems/digit-count-in-range/
digit dp with leading zero and low/high limit
"""
from header import *


class Solution:
    def digitsCount(self, target: int, low: int, high: int) -> int:
        high = str(high)
        n = len(high)
        low = str(low).zfill(n)

        @cache
        def dfs(i, limit_low, limit_high, is_num, cnt):
            if i == n:
                # update answer count
                return cnt
            ans = 0
            if not is_num and low[i] == "0":
                ans += dfs(i + 1, True, False, False, 0)

            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9

            d0 = 0 if is_num else 1
            for d in range(max(lo, d0), hi + 1):
                ans += dfs(
                    i + 1,
                    limit_low and d == lo,
                    limit_high and d == hi,
                    True,
                    cnt + (d == target),
                )
            return ans

        return dfs(0, True, True, False, 0)
