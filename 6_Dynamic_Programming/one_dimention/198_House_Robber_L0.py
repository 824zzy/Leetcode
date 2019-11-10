# Google
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [2]: 0
        [2, 4]: max(nums[0], nums[1])
        [2, 4, 3]: max(num[0]+nums[2], nums[1])
        [5, 3, 4, 5]: dp[5, 5, 9, 10]
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[-1]