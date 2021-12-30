""" https://leetcode.com/problems/delete-operation-for-two-strings/
use longest common subsequence to find least delete operations
"""

class Solution:
    def minDistance(self, A: str, B: str) -> int:
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+(A[i]==B[j]))
        return len(A)+len(B)-2*dp[-1][-1]