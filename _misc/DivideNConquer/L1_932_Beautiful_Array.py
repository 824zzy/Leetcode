""" https://leetcode.com/problems/beautiful-array/
obtain beautiful array by rearranging elements in nums
"""
from header import *

# top down divide and conquer
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def fn(A):
            if len(A)<=1: return A
            return fn(A[::2])+fn(A[1::2])
        
        return fn([i for i in range(1, n+1)])

# bottom up
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n: 
            ans = [2*x-1 for x in ans] + [2*x for x in ans]
        return [x for x in ans if x <= n]