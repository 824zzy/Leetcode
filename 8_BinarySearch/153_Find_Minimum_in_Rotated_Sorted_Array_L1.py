# Find pivot pattern
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h, comp = 0, len(nums)-1, nums[-1]
        while l<=h:
            m = (l+h)//2
            if nums[m]>comp:
                l = m + 1
            else:
                h = m - 1
        return nums[l]

# cheat solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)