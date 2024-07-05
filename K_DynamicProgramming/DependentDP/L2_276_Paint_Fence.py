""" https://leetcode.com/problems/paint-fence/
derive the dp transition formula:
    f(n) = (f(n-1) + f(n-2))*(k-1), where f(1) = k and f(2) = k**2.
"""
from header import *


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return k
            if i == 1:
                return k * k
            return (dp(i - 1) + dp(i - 2)) * (k - 1)

        return dp(n - 1)


"""
n=1, k=2 ==> 2
n=2, k=2 ==> 4
n=3, k=2 ==> 6
"""
