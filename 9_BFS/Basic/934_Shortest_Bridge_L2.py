""" https://leetcode.com/problems/shortest-bridge/submissions/
1. dfs to paint two islands.
2. bfs to search the shortest path from one island to another.
"""
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        D = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        seen = set()

        def dfs(x, y):
            seen.add((x, y))
            for dx, dy in D:
                if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]==1 and (x+dx, y+dy) not in seen:
                    dfs(dx+x, dy+y)
        
        i, j = next((i, j) for i in range(M) for j in range(N) if A[i][j])
        dfs(i, j)
        
        Q = list(seen)
        ans = 0
        while Q:
            nextQ = []
            for x, y in Q:
                for dx, dy in D:
                    if 0<=x+dx<M and 0<=y+dy<N and (x+dx, y+dy) not in seen:
                        if A[x+dx][y+dy]==1: return ans
                        nextQ.append((x+dx, y+dy))
                        seen.add((x+dx, y+dy))
            Q = nextQ
            ans += 1
                    
                
#         while Q:
#             for _ in range(len(Q)):
#                 x, y = Q.pop(0)
#                 for dx, dy in D:
#                     if 0<=x+dx<M and 0<=y+dy<N and (x+dx, y+dy) not in seen:
#                         if A[x+dx][y+dy]==1: return ans
#                         Q.append((x+dx, y+dy))
#                         seen.add((x+dx, y+dy))
#             ans += 1
                    