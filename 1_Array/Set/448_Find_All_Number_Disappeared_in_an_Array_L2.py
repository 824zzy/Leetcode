# Google
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n_set = set(nums)
        n_all_set = set([i for i in range(1, len(nums)+1)])
        return list(n_all_set-n_set)
        
# Regard the list as a dict by indexes
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums: 
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        ans = [i + 1 for i, n in enumerate(nums) if n > 0]
        return ans