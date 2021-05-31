""" L2:
Diff is the XOR result of two different numbers/
"""
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v==1]
    
# follow up
class Solution(object):
    def singleNumber(self, nums):
        diff = 0
        for num in nums: diff ^= num
        # Get lowest "1" bit in diff
        diff &= -diff
        a = b = 0
        for num in nums:
            if diff & num:
                a ^= num
            else:
                b ^= num
        return [a, b]