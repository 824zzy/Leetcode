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