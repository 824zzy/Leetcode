""" Basic dynamic programming
""" 
# by CSDojo
""" [-2, 3, 2, -1]
i  /   1   2   3
c -2   3   5   5
g -2   3   5   5
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr = max_global = nums[0]
        for i in range(1, len(nums)):
            max_curr = max(nums[i], max_curr+nums[i])
            if max_curr > max_global:
                max_global = max_curr
        return max_global
    
# by zzy824
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        dp = [0] * len(nums)
        ans = dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            ans = max(ans, dp[i])
        
        return ans