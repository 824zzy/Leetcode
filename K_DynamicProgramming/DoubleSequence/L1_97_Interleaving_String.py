""" https://leetcode.com/problems/interleaving-string/
"""
class Solution:
    def isInterleave(self, A: str, B: str, T: str) -> bool:
        if len(A)+len(B)!=len(T): return False
        @cache
        def dfs(i, j):
            if i==len(A) and j==len(B): return True
            
            ans = False
            if i<len(A) and A[i]==T[i+j]: ans = ans or dfs(i+1, j)
            if j<len(B) and B[j]==T[i+j]: ans = ans or dfs(i, j+1)
            return ans
        
        return dfs(0, 0)
    
    
# bottom up solution
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3): return False
        
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True
        
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        for i in range(1, len(s2)+1):
            dp[0][i] = dp[0][i-1] and s2[i-1]==s3[i-1]
            
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[j - 1 + i])
                
        return dp[len(s1)][len(s2)]