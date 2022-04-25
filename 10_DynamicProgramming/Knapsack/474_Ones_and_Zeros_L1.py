""" https://leetcode.com/problems/ones-and-zeroes/
classical knap-sack problem

Time: O(m*n*k)
"""
# top down
class Solution:
    def findMaxForm(self, A: List[str], m: int, n: int) -> int:
        @cache
        def dp(i, m, n):
            if m<0 or n<0: return -1
            elif i==len(A): return 0
            return max(1+dp(i+1, m-A[i].count('0'), n-A[i].count('1')), dp(i+1, m, n))
        
        return dp(0, m, n)
            

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