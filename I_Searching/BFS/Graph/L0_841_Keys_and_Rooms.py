""" https://leetcode.com/problems/keys-and-rooms/description/
dfs solution
"""
from header import *


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        G = defaultdict(list)
        for i, j in enumerate(rooms):
            G[i].extend(j)

        seen = {0}

        def dfs(i):
            for j in G[i]:
                if j not in seen:
                    seen.add(j)
                    dfs(j)
        dfs(0)
        return len(seen) == len(rooms)
