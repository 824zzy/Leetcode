""" https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/
time complexity: O(n * m^2)
"""

from header import *


class Solution:
    def countOfPairs(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(i, pre1):
            if i == len(A):
                return 1
            ans = 0
            for x in range(pre1, A[i] + 1):
                if i == 0 or A[i - 1] - pre1 >= A[i] - x:
                    ans += dp(i + 1, x)
            return ans

        return dp(0, 0) % mod


class Solution:
    def countOfPairs(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(A)
        m = max(A)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(m + 1):
            dp[-1][i] = 1

        for i in range(n - 1, -1, -1):
            for pre1 in range(m + 1):
                for x in range(pre1, A[i] + 1):
                    if i == 0 or A[i - 1] - pre1 >= A[i] - x:
                        dp[i][pre1] += dp[i + 1][x]
        return dp[0][0] % mod
