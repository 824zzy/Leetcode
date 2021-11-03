""" BFS solution using queue
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        Q = [0]
        while Q:
            cur_r = Q.pop(0)
            if cur_r not in seen:
                Q.extend(rooms[cur_r])
                seen.add(cur_r)
        return len(seen)==len(rooms)