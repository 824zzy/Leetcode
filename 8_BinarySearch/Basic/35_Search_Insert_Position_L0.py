""" L0: https://leetcode.com/problems/search-insert-position/
note that the answer can be len(A)
"""
class Solution:
    def searchInsert(self, A: List[int], target: int) -> int:
        l, r = 0, len(A)
        while l<r:
            m = (l+r)//2
            if A[m]>=target: r = m
            else: l = m + 1
        return l