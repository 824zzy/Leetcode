""" https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
build graph and do BFS
"""
from header import *

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        n = len(adjacentPairs)
        for i, j in adjacentPairs:
            G[i].append(j)
            G[j].append(i)

        i = next(i for i, x in G.items() if len(x)==1)
        Q = [i]
        ans = [i]
        seen = {i}
        while Q:
            i = Q.pop(0)
            for j in G[i]:
                if j not in seen:
                    seen.add(j)
                    Q.append(j)
                    ans.append(j)
        return ans