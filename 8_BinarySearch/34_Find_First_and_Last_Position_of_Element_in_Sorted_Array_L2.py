# Binary Search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(l, h, t, mode):
            while l<=h:
                m = (l+h)//2
                if nums[m]==t:
                    return m
                elif nums[m]>t:
                    h = m - 1
                else:
                    l = m + 1
            return l
            
        l, h = binSearch(0, len(nums)-1, target-0.5, 'l'), binSearch(0, len(nums)-1, target+0.5, 'h')-1
        if l<=h:
            return [l, h]
        else:
            return [-1, -1]

# Reverse trick
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            left = nums.index(target)
            right = len(nums)-1-(nums[::-1].index(target))
            return [left, right]
        except:
            return [-1, -1]