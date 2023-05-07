""" https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
1. add the edges on the fly
2. calculate the shortest path between two nodes using Dijkstra's algorithm
"""
from header import *

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.G = defaultdict(dict)
        for i, j, w in edges: 
            self.G[i][j] = w
        self.dis = defaultdict(dict)

    def addEdge(self, edge: List[int]) -> None:
        src, dst, w = edge
        self.G[src][dst] = w
        

    def shortestPath(self, src: int, dst: int) -> int:
        pq = [(0, src)]
        seen = {}
        while pq:
            cost, i = heappop(pq)
            if i not in seen:
                seen[i] = cost
                for j in self.G[i]:
                    heappush(pq, (cost+self.G[i][j], j))
        for _dst in range(self.n):
            self.dis[src][_dst] = seen.get(_dst, -1)
        return self.dis[src].get(dst)