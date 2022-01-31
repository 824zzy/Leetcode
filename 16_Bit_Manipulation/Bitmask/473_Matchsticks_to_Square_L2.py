""" https://leetcode.com/problems/matchsticks-to-square/
special case of 698
"""
# top down
class Solution:
    def makesquare(self, nums):
        N = len(nums)
        nums.sort(reverse=True)
        basket, rem = divmod(sum(nums), 4)
        if rem or nums[0] > basket: return False
        
        @cache
        def dfs(mask):
            if mask == 0: return 0
            for j in range(N):
                if mask & 1<<j:
                    neib = dfs(mask ^ 1<<j)
                    if neib >= 0 and neib + nums[j] <= basket:
                        return (neib + nums[j]) % basket
            return -1
                    
        return dfs((1<<N) - 1) == 0


# bottom up
class Solution:
    def makesquare(self, nums):
        N = len(nums)
        nums.sort(reverse=True)
        basket, rem = divmod(sum(nums), 4)
        if rem or nums[0] > basket: return False

        dp = [-1] * (1<<N)
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                if mask & 1<<j:
                    neib = dp[mask ^ 1<<j]
                    if neib>=0 and neib+nums[j]<=basket:
                        dp[mask] = (neib+nums[j]) % basket
                        break
        return dp[-1]==0