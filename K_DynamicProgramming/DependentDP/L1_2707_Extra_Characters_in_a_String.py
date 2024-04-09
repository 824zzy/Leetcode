""" https://leetcode.com/problems/extra-characters-in-a-string/
define dp(i) = min extra characters to make s[:i] valid
"""
from header import *


class Solution:
    def minExtraChar(self, s: str, D: List[str]) -> int:
        D = set(D)

        @cache
        def dp(i):
            if i < 0:
                return 0
            ans = dp(i - 1) + 1
            for j in range(i + 1):
                if s[j:i + 1] in D:  # O(n)
                    ans = min(ans, dp(j - 1))
            return ans
        return dp(len(s) - 1)


# KnapSack Solution
class Solution:
    def minExtraChar(self, s: str, D: List[str]) -> int:
        @cache
        def dp(i):
            if i >= len(s):
                return 0
            ans = 1 + dp(i + 1)
            for d in D:
                if s[i:i + len(d)] == d:
                    ans = min(ans, dp(i + len(d)))
            return ans
        return dp(0)


class Solution:
    def minExtraChar(self, s: str, D: List[str]) -> int:
        D = set(D)
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i] = dp[i - 1] + 1
            for j in range(i + 1):
                if s[j:i + 1] in D:
                    dp[i] = min(dp[i], dp[j - 1])
        return dp[n - 1]


# backtracking will close to TLE
class Solution:
    def minExtraChar(self, s: str, D: List[str]) -> int:
        D = set(D)

        @cache
        def dfs(l, r):
            ans = r - l
            for i in range(l, r):
                for d in D:
                    if i + len(d) <= r and s[i:i + len(d)] == d:
                        ans = min(ans, dfs(l, i) + dfs(i + len(d), r))
            return ans
        return dfs(0, len(s))


"""
"leetscode"
["leet","code","leetcode"]
"sayhelloworld"
["hello","world"]
"dwmodizxvvbosxxw"
["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
"""
