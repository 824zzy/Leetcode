""" https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/
1. find the left most j that A[j:] is strictly increasing
2. enumerate i, use i as left end point, greedily find right most j that ensure A[:i]+A[j:] is sorted
3. n-j+1 is the number of prefix can be deleted
"""
from header import *

class Solution:
    def incremovableSubarrayCount(self, A: List[int]) -> int:
        n = len(A)
        # find left most j that A[j...] is strictly increasing
        j = n-1
        while j and A[j-1]<A[j]:
            j -= 1
        if j==0:
            return n*(n+1)//2
        
        # enumerate i
        # use i as left end point, greedily find right most j that ensure A[:i]+A[j:] is sorted
        # n-j+1 is the number of prefix can be deleted
        i = 0
        ans = n-j+1
        while i==0 or (i<n-1 and A[i-1]<A[i]):
            while j<len(A) and A[i]>=A[j]:
                j += 1
            ans += n-j+1
            i += 1
        return ans 
            

"""
[1,2,3,4]
[6,5,7,8]
[8,7,6,6]
"""
        