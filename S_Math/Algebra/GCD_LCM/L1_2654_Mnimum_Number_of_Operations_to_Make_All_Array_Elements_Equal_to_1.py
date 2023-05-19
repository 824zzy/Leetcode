""" https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
brute force to find the minimal subarray that gcd is 1.
"""
from header import *

class Solution:
    def minOperations(self, A: List[int]) -> int:
        ones = A.count(1)
        if ones: return len(A)-ones
        ans = inf
        for i in range(len(A)):
            x = A[i]
            for j in range(i+1, len(A)):
                x = gcd(x, A[j]) 
                if x==1:
                    ans = min(ans, len(A)+j-i-1)
                    break
        return ans if ans!=inf else -1
    
"""
[2,6,3,4]
[2,10,6,14]
[1,1]
"""