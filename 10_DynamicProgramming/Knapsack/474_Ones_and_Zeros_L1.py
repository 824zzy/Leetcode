""" https://leetcode.com/problems/ones-and-zeroes/
classical knap-sack problem
"""
# top down
class Solution:
    def findMaxForm(self, A: List[str], M: int, N: int) -> int:
        
        @cache
        def dfs(i, m, n):
            if i==len(A): return 0
            
            if m+A[i].count('0')<=M and n+A[i].count('1')<=N:
                return max(1+dfs(i+1, m+A[i].count('0'), n+A[i].count('1')), dfs(i+1, m, n))
            else: return dfs(i+1, m, n)
            
        return dfs(0, 0, 0)
            

# bottom up
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]