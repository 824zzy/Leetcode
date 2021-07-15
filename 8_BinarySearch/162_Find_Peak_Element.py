""" L1
"""
# first reaction solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if nums[i]>nums[ans]:
                ans+=1
            else:
                break
        return ans

# binary search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
