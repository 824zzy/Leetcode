""" Naive and straightforward
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l1 = len(set(nums))
        return l1 != len(nums)