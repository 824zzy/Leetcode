""" https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
Prerequisite: a ^ b = res => a ^ res = b
From the highest bit to the lowest bit:
1. calculate the prefix set of all the numbers
2. for each bit, if we can find a pair of numbers that have the same bit, then we can set the bit to 1
"""
from header import *

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in reversed(range(32)):
            ans <<= 1
            prefixes = {x>>i for x in nums}
            for p in prefixes:
                if ans^1^p in prefixes:
                    ans += 1
                    break
        return ans