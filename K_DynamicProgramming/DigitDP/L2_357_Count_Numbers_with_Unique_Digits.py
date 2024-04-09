""" https://leetcode.com/problems/count-numbers-with-unique-digits/
dp[i] means the count of numbers with unique digits of length i and dp[i] = dp[i-1]*(11-i)
"""
from header import *

# bottom up solution


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 9
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)
        return sum(dp)

# top down solution


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 1
            if i == 1:
                return 9
            return dp(i - 1) * (11 - i)
        return sum(dp(i) for i in range(n + 1))


""" https://leetcode.com/problems/count-numbers-with-unique-digits/
digit dp with leading zero and mask

the same as 2376, 1012
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        high = str(10**n - 1)
        n = len(high)
        low = str(0).zfill(n)

        @cache
        def dfs(i, limit_low, limit_high, is_num, mask):
            if i == n:
                return 1 if is_num else 0
            # deal with leading zero
            ans = 0
            if not is_num and low[i] == '0':
                ans += dfs(i + 1, True, False, False, 0)
            # enumerate from lo to high
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            d0 = 0 if is_num else 1
            for d in range(max(lo, d0), hi + 1):
                if mask & (1 << d) == 0:
                    ans += dfs(i + 1, limit_low and d == lo,
                               limit_high and d == hi, True, mask ^ (1 << d))
            return ans
        return dfs(0, True, True, False, 0) + 1


""" math solution
For any number whose length is n, the count of all unique digit numbers is:
    A(10, n) - A(9, n-1)
as we need to choose n numbers from 0~9 and remove the leading zero numbers which is selecting from n-1 numbers from 1~9
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def A(n, k):
            ans = 1
            for i in range(n - k + 1, n + 1):
                ans *= i
            return ans

        ans = 1
        for i in range(1, n + 1):
            ans += A(10, i) - A(9, i - 1)
        return ans
