""" best solution using exchange.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                curr += 1