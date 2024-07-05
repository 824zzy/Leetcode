""" https://leetcode.com/problems/pascals-triangle/
118, 119 are the same

The values of row[i] only depends on row[i-1]
initial state: dp = [[1], [1, 1]]
transition: row[i-1] = dp[-1][i]+dp[-1][i-1]
"""
from header import *

# bottom up solution


class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        elif n == 1:
            return [1, 1]
        dp = [[1], [1, 1]]
        for i in range(2, n + 1):
            row = [1]
            for j in range(i - 1):
                row.append(dp[i - 1][j] + dp[i - 1][j + 1])
            row.append(1)
            dp.append(row)
        return dp[-1]


# top down solution


class Solution:
    def getRow(self, n: int) -> List[int]:
        @cache
        def dp(i):
            if i == 0:
                return [1]
            elif i == 1:
                return [1, 1]
            prev = dp(i - 1)
            return [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]

        return dp(n)
