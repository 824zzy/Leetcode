""" https://leetcode.com/problems/4sum/
1. sort the A to make sure we can use different direction two pointers
2. for every i and j, find the proper l and r by two sum
"""
from header import *

class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
        if len(A)<4: return []
        A.sort()
        ans = set()
        for i in range(len(A)-3):
            for j in range(i+1, len(A)-2):
                l, r = j+1, len(A)-1
                t = target-A[i]-A[j]
                while l<r:
                    if A[l]+A[r]==t: 
                        ans.add((A[i], A[j], A[l], A[r])) 
                        l, r = l+1, r-1
                    elif A[l]+A[r]>t: r -= 1
                    else: l += 1
        return ans