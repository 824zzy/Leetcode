""" https://leetcode.com/problems/snakes-and-ladders/
1. preprocess the board to a graph
2. BFS to find the shortest path
"""
from header import *

class Solution:
    def snakesAndLadders(self, A: List[List[int]]) -> int:
        G = defaultdict(lambda: -1)
        cnt = 1
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i&1==0:
                    G[cnt] = A[~i][j]
                else:
                    G[cnt] = A[~i][~j]
                cnt += 1
                
        Q = [(1, 0)]
        seen = {1}
        ans = inf
        while Q:            
            i, step = Q.pop(0)
            if i==len(A)*len(A):
                return step
            for j in range(i+1, i+7):
                if j<=len(A)*len(A) and j not in seen:
                    seen.add(j)
                    if G[j]!=-1:
                        Q.append((G[j], step+1))
                    else:
                        Q.append((j, step+1))
        return -1
    
"""
[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
[[-1,-1],[-1,3]]
[[1,1,-1],[1,1,1],[-1,1,1]]
[[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]
"""