""" L0: https://leetcode.com/problems/find-all-groups-of-farmland/
find top left and bottom right by bfs
"""
class Solution:
    def findFarmland(self, A: List[List[int]]) -> List[List[int]]:
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        ans = []
        
        def bfs(i, j):
            Q = [(i, j)]
            corr = [i, j]
            seen = set((i, j))
            while Q:
                for _ in range(len(Q)):
                    x, y = Q.pop(0)
                    A[x][y] = 0
                    seen.add((x, y))
                    for dx, dy in D:
                        if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]==1 and (x+dx, y+dy) not in seen:
                            seen.add((x+dx, y+dy))
                            Q.append([x+dx, y+dy])
            corr.extend([x, y])
            return corr
        
        for i in range(M):
            for j in range(N):
                if A[i][j]==1:
                    ans.append(bfs(i, j))
        return ans