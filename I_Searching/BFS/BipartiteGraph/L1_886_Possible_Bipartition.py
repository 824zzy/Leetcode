""" https://leetcode.com/problems/possible-bipartition/
the same as 785,
classical bipartite problem:
1. traverse the graph by bfs
2. check if any node has painted the same color
"""
from header import *

# dfs solution


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(i):
            ans = True
            for j in G[i]:
                if seen[j] == 0:
                    seen[j] = -seen[i]
                    ans &= dfs(j)
                elif seen[j] == seen[i]:
                    return False
            return ans

        G = defaultdict(list)
        for i, j in dislikes:
            G[i].append(j)
            G[j].append(i)

        seen = [0] * (n + 1)
        for i in range(1, n + 1):
            if seen[i] == 0:
                seen[i] = 1
                if not dfs(i):
                    return False
        return True

# bfs solution


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        G = defaultdict(list)
        for i, j in dislikes:
            G[i].append(j)
            G[j].append(i)

        seen = {}

        for i in range(len(G)):
            if i not in seen:
                Q = [(i, 1)]
                while Q:
                    i, color = Q.pop(0)
                    for j in G[i]:
                        if j not in seen:
                            seen[j] = -color
                            Q.append((j, -color))
                        elif seen[j] * color > 0:
                            return False
        return True
