""" https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        l, r = 0, 0
        for i in range(len(s) - 2, -1, -1):
            dp[i][i] = True
            for j in range(1, len(s)):
                if s[i] == s[j]:
                    if dp[i + 1][j - 1] or (dp[i][j - 1] and dp[i + 1][j]):
                        dp[i][j] = True
                        if j - i > r - l:
                            l, r = i, j
        return s[l:r + 1]


# convert from top down dp
class Solution:
    def longestPalindrome(self, A: str) -> str:
        dp = [[False for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            dp[i][i] = True
        for i in range(len(A) - 1):
            dp[i][i + 1] = (A[i] == A[i + 1])

        for i in reversed(range(len(A) - 1)):
            for j in reversed(range(1, len(A))):
                if A[i] == A[j]:
                    dp[i][j] |= dp[i + 1][j - 1]

        ans = ''
        for i in range(len(A)):
            for j in reversed(range(i, len(A))):
                if dp[i][j]:
                    ans = max(ans, A[i:j + 1], key=len)

        return ans
