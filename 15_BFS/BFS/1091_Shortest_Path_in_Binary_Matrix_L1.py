class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        if grid[0][0] or grid[nr-1][nc-1]: return -1
        queue = [(0, 0)]
        seen = set()
        ans = 1
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                if i==nr-1 and j==nc-1: return ans
                for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), \
                             (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                    if 0<=x<nr and 0<=y<nc and not grid[x][y] and (x, y) not in seen:
                        queue.append((x, y))
                        seen.add((x, y))
            ans += 1
            
        return -1