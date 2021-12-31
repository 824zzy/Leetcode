""" https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        l, r = 0, 0
        for i in range(len(s)-2, -1, -1):
            dp[i][i] = True
            for j in range(1, len(s)):
                if s[i]==s[j]:
                    if dp[i+1][j-1] or (dp[i][j-1] and dp[i+1][j]):
                        dp[i][j] = True
                        if j-i>r-l: l, r = i, j
        return s[l:r+1]