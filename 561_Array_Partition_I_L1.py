"""
"""
# Based on sort solution
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # One line solution
        return sum([n for i, n in enumerate(sorted(nums)) if i%2==0])

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Avoid `if` by `step`
        nums = sorted(nums)
        return sum([nums[i] for i in range(0, len(nums)-1, 2)])
        # Or more pythonic
        return sum(sorted(nums)[::2])