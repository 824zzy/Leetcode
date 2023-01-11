""" https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
post order traversal on all the nodes along with the distance and the flag of whether the node's subtree has apple
"""
from header import *

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
            
        def dfs(i, p):
            d, f = 0, hasApple[i]
            for j in G[i]:
                if j!=p:
                    _d, _f = dfs(j, i)
                    d += 2+_d if _f else 0
                    f |= _f
            return d, f
        
        return dfs(0, None)[0]

# backtracking solution
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        self.ans = set()

        def dfs(i, path):
            if hasApple[i]:
                self.ans |= path
                
            for j in G[i]:
                path.add((i, j))
                dfs(j, path)
                path.remove((i, j))
                    
        
        dfs(0, set())
        return len(self.ans)*2
        
"""
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,true,false,true,true,false]
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,true,false,false,true,false]
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,false,false,false,false,false]
"""