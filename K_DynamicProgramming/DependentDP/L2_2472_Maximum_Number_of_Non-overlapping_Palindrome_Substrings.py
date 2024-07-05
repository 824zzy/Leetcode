""" https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/
hack the problem by the special case "aaa...aaa"
"""
from header import *


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        if len(set(s)) == 1:
            return len(s) // k

        def is_palindrome(l, r):
            r -= 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        @cache
        def dp(i):
            if i >= len(s):
                return 0
            ans = dp(i + 1)
            for j in range(i + k, len(s) + 1):
                if is_palindrome(i, j):
                    ans = max(ans, 1 + dp(j))
            return ans

        return dp(0)


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        if len(set(s)) == 1:
            return len(s) // k

        def is_palindrome(l, r):
            r -= 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        dp = [0 for _ in range(len(s) + 2)]
        for i in reversed(range(len(s))):
            dp[i] = dp[i + 1]
            for j in range(i + k, len(s) + 1):
                if is_palindrome(i, j):
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[0]
