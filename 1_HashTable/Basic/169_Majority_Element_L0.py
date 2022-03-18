""" https://leetcode.com/problems/majority-element/
suboptimal solution: find major element by frequency table
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [k for k, v in collections.Counter(nums).items() if v>len(nums)//2][0]