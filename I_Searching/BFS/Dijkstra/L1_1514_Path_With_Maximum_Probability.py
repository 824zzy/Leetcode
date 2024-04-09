""" https://leetcode.com/problems/path-with-maximum-probability/
dijkstra template
"""
from header import *


class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succProb: List[float],
                       start: int,
                       end: int) -> float:
        G = defaultdict(list)
        for (i, j), w in zip(edges, succProb):
            G[i].append((j, w))
            G[j].append((i, w))

        pq = [(-1, start)]
        seen = {}
        while pq:
            p, i = heappop(pq)
            if i == end:
                return -p
            if i not in seen:
                seen[i] = p
                for j, w in G[i]:
                    heappush(pq, (p * w, j))
        return 0


# another implementation
class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succProb: List[float],
                       start: int,
                       end: int) -> float:
        G = defaultdict(list)
        for (i, j), w in zip(edges, succProb):
            G[i].append((j, w))
            G[j].append((i, w))

        pq = [(-1, start)]
        seen = {}
        seen[start] = -1

        while pq:
            x, i = heappop(pq)
            if i == end:
                return -x
            for j, w in G[i]:
                if j not in seen or x * w < seen[j]:
                    seen[j] = x * w
                    heappush(pq, (x * w, j))
        return 0
