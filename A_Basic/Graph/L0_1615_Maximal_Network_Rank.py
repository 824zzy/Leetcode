""" https://leetcode.com/problems/maximal-network-rank/
brute force: build the graph then find maximum degrees among node pairs.
"""
from header import *

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        e = defaultdict(list)
        for i, j in roads:
            e[i].append(j)
            e[j].append(i)
            
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, len(e[i])+len(e[j])-(j in e[i]))
        return ans