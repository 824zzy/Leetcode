""" https://leetcode.com/problems/majority-element-ii/
suboptimal solution: find major element by frequency table
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v > len(nums) // 3]
