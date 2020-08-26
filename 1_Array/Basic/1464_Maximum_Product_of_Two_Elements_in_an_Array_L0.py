# pythonic solution O(nlogn)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (sorted(nums)[-1]-1)*(sorted(nums)[-2]-1)
    
# 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0
        for n in nums:
            if n>=first:
                second = first
                first = n
            elif n>=second:
                second = n
                
        return (first-1)*(second-1)
