""" https://leetcode.com/problems/partition-equal-subset-sum/
choose or not to choose
"""
class Solution:
    def canPartition(self, A: List[int]) -> bool:
        s = sum(A) 
        if s&1: return False
        t = s//2
        
        @lru_cache(None)
        def dfs(i, ss):
            if i==len(A): return False
            if ss==t: return True
            
            return dfs(i+1, ss+A[i]) or dfs(i+1, ss)
        
        return dfs(0, 0)
    
class Solution:
    def canPartition(self, A: List[int]) -> bool:
        if sum(A)%2 != 0:
            return False
        dp = [0]*(sum(A)+1)
        dp[0] = 1
        for n in A:
            for i in range(int(sum(A)/2), -1, -1):
                if dp[i]: dp[i+n] = 1
            if dp[sum(A)//2]: return True
        return False