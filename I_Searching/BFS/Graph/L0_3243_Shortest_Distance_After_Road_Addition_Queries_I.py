""" https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
bfs simulation
"""

from header import *


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        def fn(G):
            Q = [0]
            ans = 0
            seen = {0}
            while Q:
                nxtQ = []
                for i in Q:
                    if i == n - 1:
                        return ans
                    for j in G[i]:
                        if j not in seen:
                            seen.add(j)
                            nxtQ.append(j)
                Q = nxtQ
                ans += 1

        def fn(G):
            Q = [(0, 0)]
            seen = {0}
            while Q:
                i, d = Q.pop(0)
                if i == n - 1:
                    return d
                for j in G[i]:
                    if j not in seen:
                        seen.add(j)
                        Q.append((j, d + 1))

        def fn(G):
            pq = [(0, 0)]
            dis = [inf] * n
            while pq:
                d, i = heappop(pq)
                if i == n - 1:
                    return d
                if d > dis[i]:
                    continue
                for j in G[i]:
                    new_d = d + 1
                    if new_d < dis[j]:
                        dis[j] = new_d
                        heappush(pq, (new_d, j))

        G = defaultdict(list)
        for x, y in pairwise(range(n)):
            G[x].append(y)

        ans = [0] * len(queries)
        for i, (u, v) in enumerate(queries):
            G[u].append(v)
            ans[i] = fn(G)
        return ans
