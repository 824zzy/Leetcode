""" https://leetcode.com/problems/search-insert-position/
use bisect to find left position to insert
"""
from header import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)