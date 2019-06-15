class Solution:
    def wallsAndGates(rooms: List[List]):
        for i in range(len(rooms)):
            for j in range(len(i)):
                if rooms[i][j] == 0:
                    self.dfs(i, j, 0, rooms)

    def dfs(i: int, j: int, count: int, rooms: List[List]):
        if i<0 or i>=len(rooms) or j<0 or j>=len(rooms[i]) or rooms[i][j] <　count:
            return
        rooms[i][j] = count
        dfs(i+1, j, count+1, rooms)
        dfs(i-1, j, count+1, rooms)
        dfs(i, j+1, count+1, rooms)
        dfs(i, j-1, count+1, rooms) 