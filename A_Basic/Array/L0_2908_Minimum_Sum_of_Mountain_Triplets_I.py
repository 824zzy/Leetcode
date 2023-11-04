""" https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/
brute force
"""
from header import *

class Solution:
    def minimumSum(self, A: List[int]) -> int:
        ans = inf
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                for k in range(j+1, len(A)):
                    if A[i]<A[j] and A[j]>A[k]:
                        ans = min(ans, A[i]+A[j]+A[k])
        return ans if ans!=inf else -1
        
"""
[8,6,1,5,3]
[5,4,8,7,10,2]
[6,5,4,3,4,5]
"""