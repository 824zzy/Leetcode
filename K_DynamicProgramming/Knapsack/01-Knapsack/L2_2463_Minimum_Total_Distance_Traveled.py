""" https://leetcode.com/problems/minimum-total-distance-traveled/solutions/
3D knap sack dp: for i-th robot, we can skip j-th factory or go to j-th factory if k is less than the limitation
"""
from header import *

class Solution:
    def minimumTotalDistance(self, A: List[int], F: List[List[int]]) -> int:
        A.sort()
        F.sort()

        @cache
        def dp(i, j, k):
            if i==len(A): return 0
            if j==len(F): return inf
            # skip j
            ans1 = dp(i, j+1, 0)
            # fix i in j
            if F[j][1]>k:
                ans2 = dp(i+1, j, k+1)+abs(A[i]-F[j][0])
            else:
                ans2 = inf
            return min(ans1, ans2)
        
        return dp(0, 0, 0)