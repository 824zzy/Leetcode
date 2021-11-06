""" L2: https://leetcode.com/problems/single-number-ii/
count bit appearance by 1,2,3
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0          #bits appearing once & twice 
        for x in nums:
            two |= one & x     #bits appearing in both one and x should be pushed to two 
            one ^= x           #bits appearing in both one and x should be set to 0
            common = one & two #common bits in one and two should be removed 
            one &= ~common     #from one
            two &= ~common     #from two 
        return one             #return bits appearing once only