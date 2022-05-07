""" https://leetcode.com/problems/132-pattern/
use monotonic decreasing stack to find a reference(2), when find a n(1) then return True
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        ref = -inf
        for n in nums[::-1]:
            if n<ref: return True
            while stk and stk[-1]<n:
                ref = stk.pop()
            stk.append(n)
            
        return False