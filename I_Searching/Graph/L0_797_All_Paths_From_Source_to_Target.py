""" https://leetcode.com/problems/all-paths-from-source-to-target/
go over the DAG using BFS
"""
from header import *

class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        Q = [(0, [0])]
        ans = []
        while Q:
            i, path = Q.pop(0)
            if i==len(G)-1:
                ans.append(path)
            for j in G[i]:
                Q.append((j, path+[j]))
        return ans