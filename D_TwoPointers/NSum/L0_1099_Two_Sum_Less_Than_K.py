""" https://leetcode.com/problems/two-sum-less-than-k/description/
1. can sort? ==> yes
2. two pointers
"""
from header import *

class Solution:
    def twoSumLessThanK(self, A: List[int], k: int) -> int:
        A.sort()
        l, r = 0, len(A)-1
        ans = -1
        while l<r:
            if A[l]+A[r]>=k:
                r -= 1
            else:
                ans = max(ans, A[l]+A[r])
                l += 1
        return ans
    

# brute force
class Solution:
    def twoSumLessThanK(self, A: List[int], k: int) -> int:
        ans = -1
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i]+A[j]<k:
                    ans = max(ans, A[i]+A[j])
        return ans