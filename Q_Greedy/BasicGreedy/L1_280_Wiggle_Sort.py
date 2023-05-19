""" https://leetcode.com/problems/wiggle-sort/
greedily swap adjacent elements if they are not in the correct order
"""
from header import *

class Solution:
    def wiggleSort(self, A: List[int]) -> None:
        for i in range(len(A)-1):
            if (i&1 and A[i]<A[i+1]) or (not i&1 and A[i]>A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]

                
class Solution:
    def wiggleSort(self, A: List[int]) -> None:
        # TC: O(nlogn), SC: O(1)
        A.sort()
        for i in range(len(A)-1):
            if i&1:
                A[i], A[i+1] = A[i+1], A[i]
