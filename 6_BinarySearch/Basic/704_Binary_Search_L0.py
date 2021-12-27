""" https://leetcode.com/problems/binary-search/
"""
class Solution:
    def search(self, A: List[int], t: int) -> int:
        l, r = 0, len(A) # r = len(A) for corner case ([1] 1)
        while l<r:
            m = (l+r)//2
            if A[m]==t: return m
            if A[m]>t: r = m
            else: l = m+1
        return -1

# bisect
class Solution:
    def search(self, A: List[int], t: int) -> int:
        idx = bisect_left(A, t)
        return idx if idx<len(A) and A[idx]==t else -1
        