""" https://leetcode.com/problems/collecting-chocolates/
1. since N=1000, O(N^2) to enumerate all the solution is acceptable.
2. convert the problem to: find the minimum operations whose total chocolate cost is the lowest.
"""
from header import *

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = list(range(0, n * x, x))
        for i, mn in enumerate(nums):
            for j in range(i, n + i):
                mn = min(mn, nums[j % n])
                s[j - i] += mn
        return min(s)
    
    
class Solution:
    def minCost(self, A: List[int], x: int) -> int:
        N = len(A)
        mn = A[:]
        ans = sum(A)
        for i in range(N): # rotate i times
            for j in range(N): # the minimum for each type
                mn[j] = min(mn[j], A[(i+j)%N])
            ans = min(ans, sum(mn)+i*x)
        return ans