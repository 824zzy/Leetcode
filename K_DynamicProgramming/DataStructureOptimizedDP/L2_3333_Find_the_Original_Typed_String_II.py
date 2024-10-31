""" https://leetcode.com/problems/find-the-original-typed-string-ii/
i: index
j: length of string
"""

from header import *


class Solution:
    def possibleStringCount(self, A: str, k: int) -> int:
        n = len(A)
        if n < k:
            return 0

        MOD = 10 ** 9 + 7
        A += "#"
        i = 0
        ans = 1
        cnt = []
        for j in range(1, len(A)):
            if A[j] != A[j - 1]:
                cnt.append(j - i)
                ans = ans * (j - i) % MOD
                i = j

        m = len(cnt)
        if m >= k:
            return ans
        dp = [[0] * k for _ in range(m + 1)]
        dp[0][0] = 1

        for i, c in enumerate(cnt):
            s = list(accumulate(dp[i], initial=0))
            for j in range(i + 1, k):
                dp[i + 1][j] = (s[j] - s[max(j - c, 0)]) % MOD
        return (ans - sum(dp[m][m:])) % MOD
