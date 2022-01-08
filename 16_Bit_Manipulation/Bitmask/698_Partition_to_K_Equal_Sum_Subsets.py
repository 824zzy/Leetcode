""" L3: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained
mask & (1<<j): check the j-th number is selected
dp[mask^(1<<j)]: find dp value of next state
"""
# bottom up solution
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        nums.sort(reverse = True)

        basket, rem = divmod(sum(nums), k)
        if rem or nums[0] > basket: return False
        
        dp = [-1] * (1<<N) 
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                if mask & (1<<j):
                    neib = dp[mask^(1<<j)]
                    if neib >= 0 and neib + nums[j] <= basket: 
                        dp[mask] = (neib + nums[j]) % basket
                        break
        return dp[-1]==0

# top down solution
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        nums.sort(reverse = True)

        basket, rem = divmod(sum(nums), k)
        if rem or nums[0] > basket: return False
        
        @cache
        def dfs(mask):
            if mask==0: return 0
            for j in range(N):
                if mask & (1<<j):
                    neib = dfs(mask ^ (1<<j))
                    if neib >= 0 and neib + nums[j] <= basket: 
                        return (neib + nums[j]) % basket
            return -1
        
        return dfs((1<<N) - 1)==0
