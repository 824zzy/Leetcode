""" https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
left: A[i] * i - (prefix[i] - prefix[0])
right: prefix[-1] - prefix[i] - (len(A) - i)*A[i]
"""
from header import *

class Solution:
    def getSumAbsoluteDifferences(self, A: List[int]) -> List[int]:
        prefix = list(accumulate(A, initial=0))
        
        ans = []
        for i, _ in enumerate(A):
            l = A[i] * i - prefix[i]
            r = prefix[-1] - prefix[i] - (len(A) - i)*A[i]
            ans.append(l+r)
        return ans 