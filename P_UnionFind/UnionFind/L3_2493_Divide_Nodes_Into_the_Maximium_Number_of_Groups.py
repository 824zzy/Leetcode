""" https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description/
1. If there is a odd-length cycle, it is impossible to divide the nodes, which is checked by the DFS part;
2. If it is possible, then we can enumerate all nodes via BFS to check for the largest number of division along each connected component, which is computed by the BFS part.
"""
from header import *


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        # check odd cycle by dfs
        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        def dfs(i, d):
            for j in G[i]:
                if seen[j] == 0:
                    union(i, j)
                    seen[j] = d + 1
                    dfs(j, d + 1)
                elif d % 2 == seen[j] % 2:
                    self.has_odd = True

        seen = [0] * (n + 1)
        A = list(range(n + 1))
        self.has_odd = False
        for i in range(n):
            if not seen[i]:
                seen[i] = 1
                dfs(i, 1)
        if self.has_odd:
            return -1

        A = [find(x) for x in A]
        comp = defaultdict(list)
        for i, x in enumerate(A):
            comp[x].append(i)

        # find max group by bfs
        def bfs(i):
            ans = 0
            seen = [0] * (n + 1)
            seen[i] = 1
            Q = [i]
            while Q:
                ans += 1
                for _ in range(len(Q)):
                    i = Q.pop(0)
                    for j in G[i]:
                        if not seen[j]:
                            seen[j] = True
                            Q.append(j)
            return ans

        ans = 0
        for k, v in comp.items():
            if k == 0:
                continue
            ans += max(bfs(x) for x in v)
        return ans
