""" https://leetcode.com/problems/min-cost-climbing-stairs/
dp[i] = cost[i]+min(dp[i-1], dp[i-2])
"""


class Solution:
    def minCostClimbingStairs(self, A: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(A):
                return 0
            return A[i] + min(dfs(i + 1), dfs(i + 2))

        return min(dfs(0), dfs(1))


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost) + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        dp[-1] = min(dp[-2], dp[-3])

        return dp[-1]
