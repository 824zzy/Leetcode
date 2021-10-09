""" L0: https://leetcode.com/problems/search-insert-position/
bisect usage
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)