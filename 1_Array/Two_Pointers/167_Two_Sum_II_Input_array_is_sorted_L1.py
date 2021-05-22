""" Two Pointer template
Left pointer move right when sum is smaller then target
Right pointer move left when sum is larger then target
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        for _ in range(len(nums)):
            if nums[i]+nums[j] == target:
                return [i+1, j+1]
            elif nums[i]+nums[j] < target:
                i += 1
            else:
                j -= 1