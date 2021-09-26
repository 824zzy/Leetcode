""" L1
note that where to use seen
"""
class Solution:
    def shortestPath(self, A: List[List[int]], k: int) -> int:
        Q = [(0, 0, k)]
        seen = set()
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        while Q:
            for _ in range(len(Q)):
                x, y, k = Q.pop(0)
                if x==len(A)-1 and y==len(A[0])-1: return step 
                for dx, dy in D:
                    if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]):
                        if A[x+dx][y+dy]==1 and k>0 and (x+dx, y+dy, k-1) not in seen:
                            Q.append((x+dx, y+dy, k-1))
                            seen.add((x+dx, y+dy, k-1))
                        elif A[x+dx][y+dy]==0 and (x+dx, y+dy, k) not in seen: 
                            Q.append((x+dx, y+dy, k))
                            seen.add((x+dx, y+dy, k))
            step += 1
        return -1
