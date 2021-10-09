""" L0: https://leetcode.com/problems/binary-search/
template
"""
class Solution:
    def search(self, A: List[int], t: int) -> int:
        l, r = 0, len(A)-1
        while l<=r:
            m = (l+r)//2
            if A[m]==t: return m
            if A[m]<t: l = m + 1
            else: r = m - 1
        return -1