""" https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
1. precalculate the power of 2 array
2. use two pointer to find the count of subsequence
"""
from header import *
class Solution:
    def numSubseq(self, A: List[int], target: int) -> int:
        mp = [0]*len(A)
        mp[0] = 1
        for i in range(1, len(A)):
            mp[i] = 2*mp[i-1]
            
        A.sort()
        ans = 0
        i, j = 0, len(A)-1
        while i<=j:
            while j>=0 and A[i]+A[j]>target:
                j -= 1
            if i<=j:
                ans += mp[j-i]%(10**9+7)
                i += 1
        return ans%(10**9+7)