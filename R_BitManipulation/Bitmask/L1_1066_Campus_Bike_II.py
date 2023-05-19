""" https://leetcode.com/problems/campus-bikes-ii/description/
2D bitmask dp
"""
from header import *

class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> int:
        D = [[0 for _ in range(len(B))] for _ in range(len(W))]
        for i, (x1, y1) in enumerate(W):
            for j, (x2, y2) in enumerate(B):
                D[i][j] = abs(x1-x2)+abs(y1-y2)
            
        @cache
        def dp(i, mask):
            if i==len(W): return 0
            ans = inf
            for j in range(len(B)):
                if mask&(1<<j):
                    ans = min(ans, D[i][j]+dp(i+1, mask^(1<<j)))
            return ans

        return dp(0, (1<<len(B))-1)

        
class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> int:
        D = [[0 for _ in range(len(B))] for _ in range(len(W))]
        for i, (x1, y1) in enumerate(W):
            for j, (x2, y2) in enumerate(B):
                D[i][j] = abs(x1-x2)+abs(y1-y2)

        dp = [[inf for _ in range((1<<len(B)))] for _ in range(len(W)+1)]
        dp[-1] = [0 for _ in range((1<<len(B)))]
        for i in reversed(range(len(W))):
            for mask in range(1<<len(B)):
                for j in range(len(B)):
                    if mask&(1<<j):
                        dp[i][mask] = min(dp[i][mask], D[i][j]+dp[i+1][mask^(1<<j)])
        return dp[0][(1<<len(B))-1]