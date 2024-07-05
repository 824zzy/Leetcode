""" https://leetcode.com/problems/modify-G-edge-weights/
TODO: copy from ye https://leetcode.com/problems/modify-graph-edge-weights/discuss/3547216/Python3-Dijkstra's-algo-twice
"""
from header import *


class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], src: int, dst: int, t: int
    ) -> List[List[int]]:
        G = [[0] * n for _ in range(n)]
        for u, v, w in edges:
            G[u][v] = G[v][u] = w
        orig = [inf] * n
        orig[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heappop(pq)
            if d == orig[u]:
                for v, w in enumerate(G[u]):
                    if w and w != -1 and d + w < orig[v]:
                        orig[v] = d + w
                        heappush(pq, (orig[v], v))

        if orig[dst] < t:
            return []
        if orig[dst] == t:
            ans = []
            for u, v, w in edges:
                if w == -1:
                    w = 2_000_000_000
                ans.append([u, v, w])
            return ans
        dist = [inf] * n
        dist[src] = 0
        parent = [-1] * n
        pq = [(0, src)]
        while pq:
            d, u = heappop(pq)
            if u == dst:
                break
            if d == dist[u]:
                for v, w in enumerate(G[u]):
                    if w:
                        if w == -1:
                            dd = d + 1
                        else:
                            dd = d + w
                        if dd < dist[v]:
                            dist[v] = dd
                            parent[v] = u
                            heappush(pq, (dd, v))
        if d > t:
            return []
        while u >= 0:
            p = parent[u]
            if p >= 0:
                if G[p][u] == -1:
                    if orig[p] < t:
                        G[p][u] = G[u][p] = t - orig[p]
                        break
                    G[p][u] = G[u][p] = 1
                t -= G[u][p]
            u = p
        ans = []
        for u, v, w in edges:
            if G[u][v] == -1:
                G[u][v] = 2_000_000_000
            ans.append([u, v, G[u][v]])
        return ans
