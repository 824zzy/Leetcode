""" L0
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(1, len(nums)):
            ans = max(ans, nums[i]-nums[i-1])
        return ans