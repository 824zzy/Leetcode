""" https://leetcode.com/problems/minimum-cost-to-convert-string-i/
floyd warshall template
"""
from header import *
class Solution:
    def minimumCost(self, S: str, T: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # floyd warshall
        n = 26
        dist = [[inf] * n for _ in range(n)]
        for i, j, w in zip(original, changed, cost): 
            i, j = ord(i)-97, ord(j)-97
            if w<dist[i][j]:
                dist[i][j] = w
        for i in range(n): dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        # sum up cost
        ans = 0
        for s, t in zip(S, T):
            s, t = ord(s)-97, ord(t)-97
            if dist[s][t]==inf: return -1
            ans += dist[s][t]
        return ans