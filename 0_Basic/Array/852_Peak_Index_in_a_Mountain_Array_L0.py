""" https://leetcode.com/problems/peak-index-in-a-mountain-array/
it can be solved by binary search or just simply return max of A
"""
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i]>A[i+1]: return i