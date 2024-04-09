# neat solution
from collections import defaultdict


class Solution:
    def calcEquation(self,
                     e: List[List[str]],
                     v: List[float],
                     queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for items, val in zip(e, v):
            x, y = items
            g[x].add((y, val))
            g[y].add((y, 1.0 / val))

        def dfs(n0, n1):
            if n0 == n1 and graph[n0]:
                return 1
            visit.add(n0)
            for neigh, val in graph[start]:
                if neigh not in visit:
                    tmp = dfs(n1, neigh)
                    if tmp > 0:
                        return val * tmp
            return -1

        ans = []
        for q in queries:
            graph = g.copy()
            visit = set()
            res.append(dfs(q[0], q[1]))
