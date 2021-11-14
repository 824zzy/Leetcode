""" L0
subtrahend as key and minuend's index as value
"""
class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if n not in seen: seen[t-n] = i
            else: return [seen[n], i]