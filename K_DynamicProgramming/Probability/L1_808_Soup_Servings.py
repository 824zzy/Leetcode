""" https://leetcode.com/problems/soup-servings/
the tricky part is to determine 5000 as the threshold.
"""
from header import *


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1

        @cache
        def dp(x, y):
            if x <= 0 and y <= 0:
                return 0.5
            elif x <= 0:
                return 1
            elif y <= 0:
                return 0
            ans = 0
            for xx, yy in ((100, 0), (75, 25), (50, 50), (25, 75)):
                ans += 0.25 * dp(x - xx, y - yy)
            return ans
        return dp(n, n)
