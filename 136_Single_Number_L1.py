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