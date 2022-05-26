""" https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
top down is not working due to TLE
"""
class Solution:
    def maximumScore(self, A: List[int], M: List[int]) -> int:
        n, m = len(A), len(M)
        dp = [[0]*m for _ in range(m+1)]
        
        for i in reversed(range(m)):
            for j in range(i, m): 
                k = i + m - j - 1
                dp[i][j] = max(A[i] * M[k] + dp[i+1][j], A[j-m+n] * M[k] + dp[i][j-1])
        
        return dp[0][-1]