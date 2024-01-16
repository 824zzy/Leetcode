""" https://leetcode.com/problems/next-permutation/
two pointers + greedy

https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

1. find the right-most k where A[k]<A[k+1]. If no such k, reverse the array
2. find the right-most l where A[k]<A[l]
3. swap A[k] and A[l], and reverse A[k+1:]
"""
from header import *

class Solution:
    def nextPermutation(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(A)==1: return
        
        def rev(i, j):
            while i<j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            
        n = len(A)
        k = n-2
        while k>=0: # find k
            if A[k]<A[k+1]: # find l
                l = n-1
                while k<l:
                    if A[k]<A[l]:
                        A[k], A[l] = A[l], A[k]
                        rev(k+1, n-1)
                        return 
                    else:
                        l -= 1
            else:
                k -= 1
        A.reverse()
        
"""
[1,2,3]
[3,2,1]
[1,1,5]
[1,3,2]
[2,3,1]
"""