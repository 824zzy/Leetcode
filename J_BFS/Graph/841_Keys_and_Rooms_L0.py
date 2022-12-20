""" https://leetcode.com/problems/keys-and-rooms/
BFS template
"""
from header import *

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        G = defaultdict(list)
        for i, j in enumerate(rooms):
            G[i].extend(j)
        
        Q = [0]
        seen = {0}
        while Q:
            i = Q.pop(0)
            for j in G[i]:
                if j not in seen:
                    seen.add(j)
                    Q.append(j)
        return len(seen)==len(rooms)