""" https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/
prefix sum + binary search

use binary search to find the index of the first element >= q and calculate the cost of the left part and right part through prefix sum array
"""
from header import *

class Solution:
    def minOperations(self, A: List[int], queries: List[int]) -> List[int]:
        A.sort()
        n = len(A)
        pre = list(accumulate(A, initial=0))
        
        ans = [0]*len(queries)
        for i, q in enumerate(queries):
            x = bisect_left(A, q)
            l = q*x - pre[x]
            r = (pre[n]-pre[x]) - q*(n-x)
            ans[i] = l+r
        return ans