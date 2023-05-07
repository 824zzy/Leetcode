""" https://leetcode.com/problems/first-completely-painted-row-or-column/
simulation using hash table
"""
from header import *

class Solution:
    def firstCompleteIndex(self, A: List[int], mat: List[List[int]]) -> int:
        mp = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mp[mat[i][j]] = (i, j)
        
        rows = Counter()
        cols = Counter()
        for i, x in enumerate(A):
            rows[mp[x][0]] += 1
            cols[mp[x][1]] += 1
            if rows[mp[x][0]]==len(mat[0]) or cols[mp[x][1]]==len(mat):
                return i
            
            
            
""" 2 3 2
[1,3,4,2]
[[1,4],[2,3]]
[2,8,7,4,1,3,5,6,9]
[[3,2,5],[1,4,6],[8,7,9]]
[6,2,3,1,4,5]
[[5,1],[2,4],[6,3]]
"""