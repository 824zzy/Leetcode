""" https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
1. add the edges on the fly
2. calculate the shortest path between two nodes using Dijkstra's algorithm
"""
from header import *


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.G = defaultdict(dict)
        for i, j, c in edges:
            self.G[i][j] = c

    def addEdge(self, edge: List[int]) -> None:
        i, j, c = edge
        self.G[i][j] = c

    def shortestPath(self, src: int, dest: int) -> int:
        pq = [(0, src)]
        seen = {}
        while pq:
            c, i = heappop(pq)
            if i == dest:
                return c
            if i not in seen:
                seen[i] = c
                for j in self.G[i]:
                    heappush(pq, (c + self.G[i][j], j))
        return -1


# another way to implement the same thing


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.G = defaultdict(dict)
        for i, j, c in edges:
            self.G[i][j] = c

    def addEdge(self, edge: List[int]) -> None:
        i, j, c = edge
        self.G[i][j] = c

    def shortestPath(self, src: int, dest: int) -> int:
        pq = [(0, src)]
        seen = {src: 0}
        while pq:
            c, i = heappop(pq)
            if i == dest:
                return c
            for j in self.G[i]:
                if j not in seen or c + self.G[i][j] < seen[j]:
                    seen[j] = c + self.G[i][j]
                    heappush(pq, (c + self.G[i][j], j))
        return -1
