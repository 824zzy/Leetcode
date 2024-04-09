""" https://leetcode.com/problems/max-area-of-island/
For each cell, apply dfs and mark all cells in island as visit
"""


class Solution:
    def maxAreaOfIsland(self, A: List[List[int]]) -> int:
        D = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        m, n = len(A), len(A[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = 0
                    cnt = 1
                    Q = [[i, j]]
                    while Q:
                        x, y = Q.pop(0)
                        for dx, dy in D:
                            if 0 <= x + dx < m and 0 <= y + \
                                    dy < n and A[x + dx][y + dy] == 1:
                                Q.append([x + dx, y + dy])
                                A[x + dx][y + dy] = 0
                                cnt += 1
                    ans = max(ans, cnt)
        return ans
