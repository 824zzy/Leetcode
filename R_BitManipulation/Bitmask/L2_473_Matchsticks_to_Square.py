""" https://leetcode.com/problems/matchsticks-to-square/
special case of 698
"""
# top down


class Solution:
    def makesquare(self, A: List[int]) -> bool:
        n = len(A)
        A.sort(reverse=True)
        k, rem = divmod(sum(A), 4)
        if rem or A[0] > k:
            return False

        @cache
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0
            for j in range(n):
                if not mask & (1 << j):
                    neib = dp(mask ^ (1 << j))
                    if neib >= 0 and neib + A[j] <= k:
                        return (neib + A[j]) % k
            return -1

        return dp(0) == 0


# bottom up
class Solution:
    def makesquare(self, nums):
        N = len(nums)
        nums.sort(reverse=True)
        basket, rem = divmod(sum(nums), 4)
        if rem or nums[0] > basket:
            return False

        dp = [-1] * (1 << N)
        dp[0] = 0
        for mask in range(1 << N):
            for j in range(N):
                if mask & 1 << j:
                    neib = dp[mask ^ 1 << j]
                    if neib >= 0 and neib + nums[j] <= basket:
                        dp[mask] = (neib + nums[j]) % basket
                        break
        return dp[-1] == 0
