""" https://leetcode.com/problems/product-of-array-except-self/
"""
from header import *

class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        ans = [1] * len(A)
        prefix = suffix = 1
        for i in range(1, len(A)):
            prefix *= A[i-1]
            suffix *= A[~i+1]
            ans[i] *= prefix
            ans[~i] *= suffix
        return ans 

class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        prefix = [1] + list(accumulate(A, mul)) + [1]
        suffix = [1] + list(accumulate(A[::-1], mul))[::-1] + [1]
        
        ans = []
        for i in range(1, len(prefix)-1):
            ans.append(prefix[i-1]*suffix[i+1])
        return ans