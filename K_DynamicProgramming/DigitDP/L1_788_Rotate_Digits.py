""" https://leetcode.com/problems/rotated-digits/
digit dp with leading zero

use has_diff to indicate whether the number has different digit from the original number
"""
from header import *


class Solution:
    def rotatedDigits(self, n: int) -> int:
        high = str(n)
        n = len(high)

        @cache
        def dfs(i, limit_high, is_num, has_diff):
            if i == n:
                return is_num and has_diff
            ans = 0
            if not is_num:
                ans += dfs(i + 1, False, False, False)

            lo = 0 if is_num else 1
            hi = int(high[i]) if limit_high else 9
            for d in range(lo, hi + 1):
                if d in (2, 5, 6, 9):
                    ans += dfs(i + 1, limit_high and d ==
                               int(high[i]), True, True)
                if d in (0, 1, 8):
                    ans += dfs(i + 1, limit_high and d ==
                               int(high[i]), True, has_diff or False)
            return ans
        return dfs(0, True, False, False)
