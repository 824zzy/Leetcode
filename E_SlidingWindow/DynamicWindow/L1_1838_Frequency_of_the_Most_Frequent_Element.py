""" https://leetcode.com/problems/frequency-of-the-most-frequent-element/
prefix sum + sliding window

consider A[j] as the right endpoint, if the cost of subarray A[i:j] > k, then move left point
"""
from header import *

# offline solution
class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        def check(i, j):
            cost = A[j]*(j+1-i) - (pre[j+1]-pre[i])
            return cost<=k
            
        A.sort()
        pre = list(accumulate(A, initial=0))
        
        i = 0
        ans = 0
        for j in range(len(A)):
            while not check(i, j):
                i += 1
            ans = max(ans, j-i+1)
        return ans
    
# online solution
class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        A.sort()
        ans = 1
        i = 0
        sm = 0
        for j in range(len(A)):
            sm += A[j]
            while (j-i+1)*A[j]-sm>k:
                sm -= A[i]
                i += 1
            ans = max(ans, j-i+1)
        return ans