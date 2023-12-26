""" https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
idea is the same as 2972.

1. find the left most j that A[j:] is strictly increasing
2. enumerate i, use i as left end point, greedily find right most j that ensure A[:i]+A[j:] is sorted
3. j-i-1 is the elements in the middle that can be deleted
"""
from header import *

class Solution:
    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        n = len(A)
        j = len(A)-1
        while j>0 and A[j-1]<=A[j]:
            j -= 1
        if j==0: return 0
        
        i = 0    
        ans = j
        while i==0 or (i<len(A)-1 and A[i-1]<=A[i]):
            while j<len(A) and A[i]>A[j]:
                j += 1
            ans = min(ans, j-i-1)
            i += 1
        return ans
        
        
    
"""
[1,2,3,10,4,2,3,5]
[5,4,3,2,1]
[1,2,3]
[1,2,3,10,0,7,8,9]
[6,3,10,11,15,20,13,3,18,12]
[2,2,2,1,1,1]
[16,10,0,3,22,1,14,7,1,12,15]
"""