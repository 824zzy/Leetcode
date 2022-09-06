""" https://leetcode.com/problems/bitwise-ors-of-subarrays/
Define vals to keep bitwise ORs of subarray ending at a given value. Due to the fact that OR cannot unset set bit, vals at any value cannot exceed 30.
"""
from header import *
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans, vals = set(), set()
        for x in A: 
            vals = {x | xx for xx in vals} | {x}
            ans |= vals
        return len(ans)