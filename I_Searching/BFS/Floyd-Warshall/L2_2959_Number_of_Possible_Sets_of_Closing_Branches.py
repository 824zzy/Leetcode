""" https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/
1. brute force using bitmask
2. floyd-warshall
"""
from header import *


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, G: List[List[int]]) -> int:
        def bfs(mask):
            N = len(G)
            dist = [[inf] * n for _ in range(n)]
            for i in range(n):
                dist[i][i] = 0

            for i, j, w in G:
                if mask & (1 << i) and mask & (1 << j):
                    dist[i][j] = min(dist[i][j], w)
                    dist[j][i] = min(dist[j][i], w)

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

            for i in range(n):
                for j in range(n):
                    if mask & (1 << i) and mask & (1 << j) and dist[i][j] > maxDistance:
                        return False
            return True

        ans = 0
        for mask in range(1 << n):  # enumerate subset
            ans += bfs(mask)
        return ans


"""
3
5
[[0,1,2],[1,2,10],[0,2,10]]
3
5
[[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
1
10
[]
3
3
[[2,0,14],[1,0,15],[1,0,7]]
"""
