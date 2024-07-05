""" https://leetcode.com/problems/01-matrix/
Two pass DP for 4 directions search.
dp[i][j] = min(dp[i][j], dp[i][j +/- 1]+1) &
dp[i][j] = min(dp[i][j], dp[i +/- 1][j]+1)
"""


class Solution:
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return []
        dp = [[float("inf") for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(A[0]) - 1, -1, -1):
                if A[i][j] != 0:
                    print(i, j)
                    if i < len(A) - 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    if j < len(A[0]) - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp
