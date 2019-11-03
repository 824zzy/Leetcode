class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            maxLen = 0
            for j in range(0, i):
                if nums[j]<nums[i] and maxLen<dp[j]:
                    maxLen = dp[j]
            dp[i] = maxLen + 1
        return max(dp)