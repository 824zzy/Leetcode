""" L0: https://leetcode.com/problems/search-insert-position/
"""
class Solution:
    def searchInsert(self, A: List[int], t: int) -> int:
        l, r = 0, len(A)-1
        while l<=r:
            m = (l+r)//2
            if A[m]<t: l = m + 1
            else : r = m - 1
        return l