""" https://leetcode.com/problems/palindromic-substrings/
2d dp records if substring[i, j] is palindrome.
1. If s[i]==s[j] and i,j distance smaller than 2, the substring s[i:j] is palindrome.
2. If s[i]==s[j] and the substring s[i+1:j-1] is palindrome, the substring s[i:j] is palindrome.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j]:
                    res += 1
        return res
