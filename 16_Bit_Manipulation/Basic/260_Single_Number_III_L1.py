""" https://leetcode.com/problems/single-number-iii/
Get the xor of the whole array. 
Retrieve the last set bit and use that as a differentiator to separate the array into two groups. 
Each group would contain only one single number then.
"""
class Solution:
    def singleNumber(self, A: List[int]) -> List[int]:
        diff = 0
        for a in A: diff ^= a
        diff &= -diff # get lowest "1" bit
        ans = [0, 0]
        for a in A:
            if diff&a: ans[0] ^= a
            else: ans[1] ^= a
        return ans