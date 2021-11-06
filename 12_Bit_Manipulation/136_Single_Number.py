""" L0: https://leetcode.com/problems/single-number/
find the number appears only once.
a ^ 0 = a
a ^ a = 0
Note that a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i  
        return a