""" https://leetcode.com/problems/pascals-triangle/
118, 119 are the same

The values of row[i] only depends on row[i-1]
initial state: dp = [[1], [1, 1]]
transition: row[i-1] = dp[-1][i]+dp[-1][i-1]
"""
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1: return [[1]]
        elif n==2: return [[1], [1, 1]]
        dp = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(i-1):
                row.append(dp[i-1][j]+dp[i-1][j+1])
            row.append(1)
            dp.append(row)
        return dp