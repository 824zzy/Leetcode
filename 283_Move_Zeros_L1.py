""" best solution using exchange.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                curr += 1

""" Another solution
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        nums[:] = nums[:index] + [0]*(len(nums)-index)

""" slow but readable solution
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        while count:
            nums.append(0)
            count -= 1