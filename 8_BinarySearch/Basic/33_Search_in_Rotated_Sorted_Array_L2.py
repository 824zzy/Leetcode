""" https://leetcode.com/problems/search-in-rotated-sorted-array/
Define l and r as the lower and higher bound of the array index that we are checking. 
Iteratively divide the array into two pieces, and discard the one that target is not in.
"""
class Solution:
    def search(self, A: List[int], t: int) -> int:
        l, r = 0, len(A)-1
        while l <= r: 
            m = (l+r)//2
            if A[m] == t: return m
            if A[l] <= A[m]: 
                if A[l] <= t < A[m]: r = m - 1
                else: l = m + 1
            else: 
                if A[m] < t <= A[r]: l = m + 1
                else: r = m - 1
        return -1