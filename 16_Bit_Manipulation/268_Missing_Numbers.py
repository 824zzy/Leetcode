""" L1: Variance of 136
XOR each number with complete one
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans ^= (i+1) ^ nums[i]
        return ans