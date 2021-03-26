class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []            
        M, N = len(matrix), len(matrix[0])
        p_visited, a_visited = set(), set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<M and 0<=new_y<N and (new_x, new_y) not in visited and matrix[new_x][new_y]>=matrix[x][y]:
                    dfs(visited, new_x, new_y)
        for i in range(M):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, N-1)
        for j in range(N):
            dfs(p_visited, 0, j)
            dfs(a_visited, M-1, j)
        return list(p_visited.intersection(a_visited))