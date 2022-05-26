""" https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Find how many numbers are less then mid in each row as sentinel
"""
class Solution:
    def kthSmallest(self, A: List[List[int]], k: int) -> int:
        def count(m):
            return sum([bisect_right(row, m) for row in A])
            
        l, r = A[0][0], A[-1][-1]
        while l<=r:
            m = (l+r)//2
            if count(m)<k: l = m+1
            else: r = m-1
        return l