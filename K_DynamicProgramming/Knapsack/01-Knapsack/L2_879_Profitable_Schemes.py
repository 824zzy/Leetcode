""" https://leetcode.com/problems/profitable-schemes/
It is L2 simply because of the strict memory limit
"""


class Solution:
    def profitableSchemes(
            self,
            n: int,
            minProfit: int,
            group: List[int],
            profit: List[int]) -> int:
        dp = [[0] * (1 + n) for _ in range(1 + minProfit)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]
        return sum(dp[minProfit]) % (10**9 + 7)

# top down won't work due to the strict memory limit


class Solution:
    def profitableSchemes(
            self,
            n: int,
            minProfit: int,
            group: List[int],
            profit: List[int]) -> int:
        @cache
        def dp(i, p, n):
            if n < 0:
                return 0
            elif i == len(group):
                return p >= minProfit
            return dp(i + 1,
                      p + profit[i],
                      n - group[i]) % (10**9 + 7) + dp(i + 1,
                                                       p,
                                                       n) % (10**9 + 7)

        return dp(0, 0, n) % (10**9 + 7)
