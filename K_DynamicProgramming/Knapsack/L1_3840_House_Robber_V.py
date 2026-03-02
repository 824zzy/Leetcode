""" https://leetcode.com/problems/house-robber-v/
House Robber variant: adjacent houses can both be robbed only if they have
different colors. dp(i, robbed) = max money from houses i..n-1, where robbed
indicates whether house i-1 was robbed. If previous was robbed, can only rob
current if colors differ. O(n) time and space.
"""


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        A = list(zip(nums, colors))

        @cache
        def dp(i, robbed):
            if i == len(A):
                return 0
            # skip
            ans = dp(i + 1, False)
            # try to rob it
            if not robbed:
                ans = max(ans, A[i][0] + dp(i + 1, True))
            # when robbed previous, check if we can rob
            if robbed:
                if A[i][1] != A[i - 1][1]:
                    ans = max(ans, A[i][0] + dp(i + 1, True))
            return ans

        return dp(0, False)
