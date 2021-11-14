""" L1: data processing tricks
1. use two set
2. convert existing number to negative
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n_set = set(nums)
        n_all_set = set([i for i in range(1, len(nums)+1)])
        return list(n_all_set-n_set)
        
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums: 
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]