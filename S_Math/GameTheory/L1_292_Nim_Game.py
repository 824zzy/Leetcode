""" https://leetcode.com/problems/nim-game/
dp solution will TLE due to the large test case.
Since the dp equation is: fn(i) = not fn(i-1) or not fn(i-2) or not fn(i-3),
we can simply check if n is a multiple of 4
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4


# TLE dp solution
class Solution:
    def canWinNim(self, n: int) -> bool:
        @cache
        def dp(n):
            if n <= 3:
                return True
            if any([not dp(n - x) for x in (1, 2, 3)]):
                return True
            else:
                return False

        return dp(n)
