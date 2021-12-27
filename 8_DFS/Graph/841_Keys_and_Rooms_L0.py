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