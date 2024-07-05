""" https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
knap sack problem:
1. if white tile, try to find minimum of cover/skip
2. if black tile, just skip it
"""


class Solution:
    def minimumWhiteTiles(self, A: str, C: int, l: int) -> int:
        @cache
        def dp(i, c):
            if i >= len(A):
                return 0
            elif c == 0:
                return A[i:].count("1")
            # cover/skip if white
            if A[i] == "1":
                return min(dp(i + l, c - 1), 1 + dp(i + 1, c))
            # skip it if black
            else:
                return dp(i + 1, c)

        return dp(0, C)
