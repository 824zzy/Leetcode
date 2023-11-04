""" https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/
top down dp using index and remaining size
"""
from header import *

class Solution:
    def minIncrementOperations(self, A: List[int], k: int) -> int:
        @cache
        def dp(i, x):
            if x==0:
                return inf
            if i>=len(A):
                return 0
            # skip
            ans1 = dp(i+1, x-1)
            # choose
            ans2 = max(k-A[i], 0)+dp(i+1, 3)
            return min(ans1, ans2)
        return dp(0, 3)

# solution without remaining size
class Solution:
    def minIncrementOperations(self, A: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i>=len(A):
                return 0
            ans1 = max(k-A[i], 0)+dp(i+1)
            ans2 = max(k-A[i], 0)+dp(i+2)
            ans3 = max(k-A[i], 0)+dp(i+3)
            return min(ans1, ans2, ans3)
        return min(dp(0), dp(1), dp(2))