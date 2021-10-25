""" L1: https://leetcode.com/problems/longest-palindromic-subsequence/
"""
# top down dp solution
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l==r: return 1
            elif l>r: return 0
            
            if s[l]==s[r]: return dfs(l+1, r-1)+2
            return max(dfs(l+1, r), dfs(l, r-1))
        
        return dfs(0, len(s)-1)

# bottom up dp solution
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        for i in range(1, len(s)):
            for j in range(len(s)-1, i-1, -1):
                x, y = j-i, j
                if s[x]==s[y]: dp[x][y] = dp[x+1][y-1] + 2
                else: dp[x][y] = max(dp[x][y-1], dp[x+1][y])
        return dp[0][-1]