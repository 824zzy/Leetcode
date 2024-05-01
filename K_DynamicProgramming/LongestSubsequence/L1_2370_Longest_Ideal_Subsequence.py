""" https://leetcode.com/problems/longest-ideal-subsequence/
Longest increasing subsequence - like problem
"""
from header import *

# the top down solution below will Memory Limit Exceeded :(
# Time complexity: O(N*k), (10^5)*25
# Space complexity: O(N*k), (10^5)*25


class Solution:
    def longestIdealString(self, A: str, k: int) -> int:
        A = [ord(x) for x in A]

        @cache
        def dp(i, prev):
            if i == len(A):
                return 0
            ans = dp(i + 1, prev)
            if prev is None or abs(A[i] - prev) <= k:
                ans = max(ans, 1 + dp(i + 1, A[i]))
            return ans
        return dp(0, None)


# bottom up version of the above solution which is accepted
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [[0 for _ in range(26)] for _ in range(len(s)+1)]
        for i in reversed(range(len(s))):
            cur = ord(s[i])-97
            for pre in range(26):
                dp[i][pre] = dp[i+1][pre]
                if abs(cur-pre) <= k:
                    dp[i][pre] = max(dp[i][pre], 1+dp[i+1][cur])
        return max(dp[0])


# bottom up version with optimization
class Solution:
    def longestIdealString(self, A: str, k: int) -> int:
        A = [ord(x) - 97 for x in A]
        dp = [0] * 26

        for x in A:
            mx = 0
            for y in range(max(x - k, 0), min(x + k + 1, 26)):
                mx = max(mx, dp[y])
            dp[x] = mx + 1
        return max(dp)
