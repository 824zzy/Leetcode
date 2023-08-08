""" https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
brute force using binary search/sliding window

1. sort
2. binary search/sliding window
"""
from header import *

class Solution:
    def maximumBeauty(self, A: List[int], k: int) -> int:
        A.sort()
        ans = 0
        for i, x in enumerate(A):
            ans = max(ans, bisect_right(A, x+2*k)-i)
        return ans
    
class Solution:
    def maximumBeauty(self, A: List[int], k: int) -> int:
        A.sort()
        i = 0
        ans = 0
        for j in range(len(A)):
            while A[j]-2*k>A[i]:
                i += 1
            ans = max(ans, j-i+1)
        return ans