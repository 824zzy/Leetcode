""" https://leetcode.com/problems/burst-balloons/submissions/
TODO: https://leetcode.com/problems/burst-balloons/discuss/970727/Python-5-lines-dp-explained
Every element in the given list has two roles:
   1. as the element to disappear lastly
   2. as the boundary for the subarray if it will disappear lastly

Time: O(n^3)
"""
from header import *

class Solution:
    def maxCoins(self, A: List[int]) -> int:
        A = [1] + A + [1]
        dp = [[0]*len(A) for _ in range(len(A))]
        
        for i in reversed(range(len(A))):
            for j in range(i, len(A)):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+A[i]*A[k]*A[j])
        return dp[0][-1]

# Top down solution from dba: https://leetcode.com/problems/burst-balloons/discuss/970727/Python-5-lines-dp-explained
class Solution:
    def maxCoins(self, nums):
        A = [1] + nums + [1]
        
        @lru_cache(None)
        def dfs(i, j):
            return max([A[i]*A[k]*A[j] + dfs(i,k) + dfs(k,j) for k in range(i+1, j)] or [0])
        
        return dfs(0, len(A) - 1)