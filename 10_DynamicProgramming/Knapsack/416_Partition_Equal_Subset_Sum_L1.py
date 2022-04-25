""" https://leetcode.com/problems/partition-equal-subset-sum/
at each index we just need to decide add integer or not

Time: O(N*n), where N=sum(A) and n=len
"""
class Solution:
    def canPartition(self, A: List[int]) -> bool:
        sm = sum(A)
        if sm&1: return False
        else: t = sm//2
        
        @cache
        def dp(i, sm):
            if sm==t: return True
            elif i==len(A): return False
            return dp(i+1, sm) or dp(i+1, sm+A[i])
        
        return dp(0, 0)
    
class Solution:
    def canPartition(self, A: List[int]) -> bool:
        if sum(A)%2 != 0: return False

        dp = [0]*(sum(A)+1)
        dp[0] = 1
        for n in A:
            for i in range(int(sum(A)/2), -1, -1):
                if dp[i]: dp[i+n] = 1
            if dp[sum(A)//2]: return True
        return False