""" https://leetcode.com/problems/count-number-of-ways-to-place-houses/
"""
# based on observation: one side has no effect on the other side, the
# number of ways on one side is fibonacci sequence.


class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 1
            if i == 1:
                return 2
            return dp(i - 1) + dp(i - 2)

        ans = dp(n)
        return (ans * ans) % (10**9 + 7)

# or consider the problem as knapsack problem:


class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def dp(i, canPlace):
            if i == n:
                return 0
            if canPlace:
                return 1 + dp(i + 1, False) + dp(i + 1, True)
            else:
                return dp(i + 1, True)

        ans = dp(0, True) + 1
        return (ans * ans) % (10**9 + 7)
