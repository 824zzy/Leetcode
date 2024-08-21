""" https://leetcode.com/problems/2-keys-keyboard/
dp (n) refers to the minimum number of operations to get n.
For each n, we try all its prime factors x, and the steps are n//x.

time complexity: O(n^2)
"""

from header import *


class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(n):
            if n == 1:
                return 0
            ans = inf
            for x in range(1, n // 2 + 1):
                if n % x == 0:
                    ans = min(ans, n // x + dp(x))
            return ans

        return dp(n)


"""
3
1
5
8
9
18
"""
