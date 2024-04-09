""" https://leetcode.com/problems/consecutive-numbers-sum/
a1*n + n*(n-1)/2 = x
==> a1 = (x - n*(n-1)/2) / n
enumerate all the n and check if a1 is valid

the upper bound is n*(n-1)/2 <= x
=缩放=>  (n-1)*(n-1) <= 2*x
==> n <= sqrt(2*x)+1
"""
from header import *


class Solution:
    def consecutiveNumbersSum(self, x: int) -> int:
        ans = 0
        for n in range(1, isqrt(2 * x) + 1):
            if (x - n * (n - 1) / 2) % n == 0:
                ans += 1
        return ans
