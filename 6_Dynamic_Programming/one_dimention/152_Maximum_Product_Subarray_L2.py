class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_dp = [float('-inf')] * (len(nums))
        min_dp[0] = nums[0]
        max_dp = [float('-inf')] * (len(nums))
        max_dp[0] = nums[0]            
                
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
            min_dp[i] = min(min_dp[i-1]*nums[i], max_dp[i-1]*nums[i], nums[i])

        return max(max_dp+min_dp)