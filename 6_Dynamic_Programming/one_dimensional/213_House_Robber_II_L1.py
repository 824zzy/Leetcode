class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0], nums[1])
        dp1 = [0] * (len(nums))
        dp1[0] = nums[0]
        dp1[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)-1):
            dp1[i] = max(nums[i]+dp1[i-2], dp1[i-1], nums[i]+dp1[i-3])
            
        dp2 = [0] * (len(nums))
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp2[i] = max(nums[i]+dp2[i-2], dp2[i-1], nums[i]+dp2[i-3])
        return max(dp1[-2], dp2[-1])