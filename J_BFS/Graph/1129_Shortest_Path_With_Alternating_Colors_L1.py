""" https://leetcode.com/problems/shortest-path-with-alternating-colors/
bfs with colors as extra state
"""
from header import *

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for i, j in redEdges: G[i].append((j, 'r'))
        for i, j in blueEdges: G[i].append((j, 'b'))
            
        ans = [-1] * n
        Q = [(0, 0, None)]
        seen = {(0, 'r'), (0, 'b')}
        while Q:
            step, i, c1 = Q.pop(0)
            if ans[i]==-1: ans[i] = step
            for j, c2 in G[i]:
                if c1!=c2 and (j, c2) not in seen:
                    seen.add((j, c2))
                    Q.append((step+1, j, c2))
        return ans
            
"""
3
[[0,1],[1,2]]
[]
3
[[0,1]]
[[2,1]]
5
[[0,1],[1,2],[2,3],[3,4]]
[[1,2],[2,3],[3,1]]
"""   