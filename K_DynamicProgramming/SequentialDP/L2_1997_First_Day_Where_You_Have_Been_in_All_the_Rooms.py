""" https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/
"""


class Solution:
    def firstDayBeenInAllRooms(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            return (2 * dp(i - 1) - dp(A[i - 1]) + 2) % (10**9 + 7)

        return dp(len(A) - 1) % (10**9 + 7)


class Solution:
    def firstDayBeenInAllRooms(self, A: List[int]) -> int:
        dp = [0] * len(A)
        for i in range(1, len(A)):
            dp[i] = (2 * dp[i - 1] - dp[A[i - 1]] + 2) % (10**9 + 7)
        return dp[-1] % (10**9 + 7)
