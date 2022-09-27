""" https://leetcode.com/problems/find-all-good-indices/
The same as 2100_Find_Good_Days_to_Rob_the_Bank_L1.py

1. two passes for calculate consecutive increasing and decreasing subarray
2. linear scan to find good indices
"""
from header import *

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        A = [1]*len(nums)
        for i in range(1, len(nums)):
            if nums[i-1]>=nums[i]: A[i] = A[i-1]+1
                
        _A = [1]*len(nums)
        for i in reversed(range(len(nums)-1)):
            if nums[i]<=nums[i+1]: _A[i] = _A[i+1]+1
        
        ans = []
        for i in range(1, len(nums)-1):
            if A[i-1]>=k and _A[i+1]>=k:
                ans.append(i)
        return ans