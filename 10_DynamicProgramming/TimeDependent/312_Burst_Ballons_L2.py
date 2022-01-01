""" https://leetcode.com/problems/burst-balloons/submissions/
**Top down solution will TLE**

Every element in the given list has two roles:
   1. as the element to disappear lastly
   2. as the boundary for the subarray if it will disappear lastly
"""
class Solution:
    def maxCoins(self, A: List[int]) -> int:
        A = [1] + A + [1]
        dp = [[0]*len(A) for _ in range(len(A))]
        
        for i in reversed(range(len(A))):
            for j in range(i, len(A)):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+A[i]*A[k]*A[j])
        return dp[0][-1]