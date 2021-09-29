""" L1
dfs to paint two islands.
bfs to search the shortest path from one island to another.
"""
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y):
            A[x][y] = 2
            for dx, dy in D:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and A[x+dx][y+dy]==1 and (x+dx, y+dy) not in seen:
                    seen.add((x+dx, y+dy))
                    dfs(x+dx, y+dy)
                    
        def paint():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == 1:
                        seen.add((i, j))
                        dfs(i, j)
                        return i, j
        
        seen = set()
        s_i, s_j = paint()
        Q = [(0, s_i, s_j)]
        seen = set()
        seen.add((s_i, s_j))
        while Q:
            for _ in range(len(Q)):
                b, x, y = heapq.heappop(Q)
                if A[x][y]==1: return b
                for dx, dy in D:
                    if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and (x+dx, y+dy) not in seen:
                        if A[x+dx][y+dy]==2 or A[x+dx][y+dy]==1:
                            seen.add((x+dx, y+dy))
                            heapq.heappush(Q, (b, x+dx, y+dy))
                        elif A[x+dx][y+dy]==0:
                            seen.add((x+dx, y+dy))
                            heapq.heappush(Q, (b+1, x+dx, y+dy))