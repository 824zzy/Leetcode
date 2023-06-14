""" https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
1. create a fixed window which size is ones' count.
2. minimum swaps is the zeros' count in the fixed window
"""
from header import *

class Solution:
    def minSwaps(self, A: List[int]) -> int:
        ones = A.count(1)
        zeros = 0
        if ones==0: return 0
        
        ans = A.count(0)
        n = len(A)
        for i in range(2*n):
            zeros += A[i%n]==0
            if i>=ones-1:
                ans = min(ans, zeros)
                zeros -= A[(i%n)-ones+1]==0
        return ans