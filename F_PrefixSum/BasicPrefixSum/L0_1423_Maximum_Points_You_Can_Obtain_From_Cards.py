""" https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
maintain rolling suffix sum.
or find largest prefix[i]+suffix[k-i]
"""
from header import *
class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        ans = suffix = sum(A[-k:])
        
        for i in range(k):
            suffix -= A[-k+i]
            suffix += A[i]
            ans = max(ans, suffix)
        return ans
    
class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        prefix = list(accumulate(A, initial=0))
        suffix = list(accumulate(reversed(A), initial=0))
        
        ans = 0
        for i in range(k+1):
            ans = max(ans, prefix[i]+suffix[k-i])
        return ans