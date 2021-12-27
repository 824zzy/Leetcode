""" https://leetcode.com/problems/largest-divisible-subset/
Sort A in ascending order. Find dp[i] contains the largest subset containing A[i].
enhanced time sequential
"""
# bottom up
class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        A.sort()
        dp = []
        for i in range(len(A)):
            dp.append([A[i]])
            for j in range(i):
                if A[i]%A[j]==0:
                    dp[i] = max(dp[i], dp[j]+[A[i]], key=len)
        return max(dp, key=len)

# top down: not optimized
class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        A.sort(reverse=True)
        @lru_cache(None)
        def dfs(prev, i):
            if i<0: return []
            if not prev or A[i]%prev==0: n = [A[i]]+dfs(A[i], i-1)
            else: n = []
            nn =  dfs(prev, i-1)
            return max(n, nn, key=len)
        
        return dfs(None, len(A)-1)