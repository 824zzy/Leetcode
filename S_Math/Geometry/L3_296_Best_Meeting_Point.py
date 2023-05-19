""" https://leetcode.com/problems/best-meeting-point/
TODO: from ye (https://leetcode.com/problems/best-meeting-point/discuss/1453149/Python3-sweep-the-grid)
"""
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]: 
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        
        ans = 0
        lo, hi = 0, len(rows)-1
        while lo < hi: 
            ans += rows[hi] - rows[lo] + cols[hi] - cols[lo]
            lo += 1
            hi -= 1
        return ans 