""" https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
bfs with state (k, x, y)
"""
class Solution:
    def shortestPath(self, A: List[List[int]], k: int) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        Q = [[k, 0, 0, 0]]
        seen = set((k, 0, 0))
        while Q:
            k, x, y, step = Q.pop(0)
            if x==len(A)-1 and y==len(A[0])-1: return step 
            for dx, dy in D:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]):
                    if A[x+dx][y+dy]==1:
                        if k>0 and (k-1, x+dx, y+dy) not in seen:
                            Q.append([k-1, x+dx, y+dy, step+1])
                            seen.add((k-1, x+dx, y+dy))
                    elif (k, x+dx, y+dy) not in seen:
                        Q.append([k, x+dx, y+dy, step+1])
                        seen.add((k, x+dx, y+dy))
        return -1