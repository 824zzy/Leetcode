""" https://leetcode.com/problems/strange-printer/
"""

from header import *


class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(ch for i, ch in enumerate(s) if i == 0 or s[i - 1] != ch)

        @cache
        def dp(lo, hi):
            if lo == hi:
                return 0
            ans = 1 + dp(lo + 1, hi)
            for mid in range(lo + 1, hi):
                if s[lo] == s[mid]:
                    ans = min(ans, dp(lo, mid) + dp(mid + 1, hi))
            return ans

        return dp(0, len(s))
