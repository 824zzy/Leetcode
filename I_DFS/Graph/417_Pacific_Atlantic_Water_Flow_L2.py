""" https://leetcode.com/problems/pacific-atlantic-water-flow/
Think reversely, starting from ocean and move in increase way.
1. flood fill pacific
2. flood fill atlantic
3. find valid islands
"""
class Solution:
    def pacificAtlantic(self, A: List[List[int]]) -> List[List[int]]:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = defaultdict(list)
        
        def dfs(x, y, O):
            if O in seen[(x, y)]: return None
            seen[(x, y)].append(O)
            for dx, dy in D:        
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]):
                    print(x, y, x+dx, y+dy)
                    if A[x][y]<=A[x+dx][y+dy]:
                        dfs(x+dx, y+dy, O)
        
        # flood fill pacific
        for i in range(len(A)): dfs(i, 0, 'P')
        for j in range(len(A[0])): dfs(0, j, 'P')
        # flood fill atlantic
        for i in range(len(A)): dfs(i, len(A[0])-1, 'O')
        for j in range(len(A[0])): dfs(len(A)-1, j, 'O')

        return [k for k, v in seen.items() if len(v)==2]