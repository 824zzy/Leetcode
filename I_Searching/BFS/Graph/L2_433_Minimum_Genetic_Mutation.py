""" https://leetcode.com/problems/minimum-genetic-mutation/
the same as 127, it is medium for the sake of loose time limit.
1. create a graph by checking all possible candidates O(n*8*4) rather than double for loop O(n^2)
2. classic bfs to find minimum step
"""
from header import *


class Solution:
    def minMutation(self, S: str, E: str, B: List[str]) -> int:
        G = defaultdict(set)
        for b in B:
            for i in range(len(b)):
                for c in "ACGT":
                    G[b[:i] + c + b[i + 1 :]].add(b)

        Q = [(0, S)]
        seen = set([S])
        while Q:
            step, i = heappop(Q)
            if i == E:
                return step
            for j in G[i]:
                if j not in seen:
                    seen.add(j)
                    heappush(Q, (step + 1, j))
        return -1
