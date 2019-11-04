# Amazon
""" trick of bit manipulation to find the number that appear only once.
a ^ 0 = 0
a ^ a = 0
Note that a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i  
        return a

# Counter Solution
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v==1:
                return k