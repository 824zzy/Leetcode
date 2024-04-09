""" https://leetcode.com/problems/word-break/
"""
from header import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        @cache
        def dfs(i):
            if i > len(s):
                return False
            if i == len(s):
                return True
            ans = False
            for w in wordDict:
                if s[i:i + len(w)] == w:
                    ans |= dfs(i + len(w))
            return ans

        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for w in wordDict:
                    if s[i:i + len(w)] == w:
                        dp[i + len(w)] = True
        return dp[-1]
