""" https://leetcode.com/problems/sum-of-matrix-after-queries/
1. think reversely
2. simulation while store the seen rows and columns
"""
from header import *

class Solution:
    def matrixSumQueries(self, n: int, A: List[List[int]]) -> int:
        ans = 0
        seen = [set(), set()]
        for t, i, v in reversed(A):
            if i not in seen[t]:
                ans += v*(n-len(seen[t^1]))
                seen[t].add(i)
        return ans
            
            
"""
3
[[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
3
[[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
8
[[0,6,30094],[0,7,99382],[1,2,18599],[1,3,49292],[1,0,81549],[1,1,38280],[0,0,19405],[0,4,30065],[1,4,60826],[1,5,9241],[0,5,33729],[0,1,41456],[0,2,62692],[0,3,30807],[1,7,70613],[1,6,9506],[0,5,39344],[1,0,44658],[1,1,56485],[1,2,48112],[0,6,43384]]
"""