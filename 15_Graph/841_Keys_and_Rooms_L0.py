""" dfs solution
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = []
        self.dfs(rooms, visited, 0)

    def dfs(self, rooms: List[List[int]], visited: [], curr:int) -> None:
        if curr in visited:
            return
        
        visited.append(curr)
        for key in visited:
            self.dfs(rooms, visited, key)

""" BFS solution using queue
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]
        queue = [0]

        while queue:
            curr = queue.pop(0)
            for nxt in rooms[curr]:
                if nxt not in visited:
                    queue.append(nxt)
                    visited.append(nxt)
        return len(visited) == len(rooms)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        enable = rooms[0]
        while enable:
            for i in range(len(enable)):
                key = enable.pop()
                if key not in visited:
                    enable.extend(rooms[key])
                visited.add(key)
        return len(visited)==len(rooms)