""" https://leetcode.com/problems/find-the-duplicate-number/
TC: O(nlogn), find the first element where more than x elements smaller than x
"""
class Solution:
    def findDuplicate(self, A: List[int]) -> int:
        def fn(x):
            # return True if more than x elements smaller than x
            return sum([1 for y in A if y<=x])>x
            
        l, r = 1, len(A)
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m + 1
        return l