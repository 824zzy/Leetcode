""" https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
Brute force simulation

Time: O(n^2) ~= O(5*10^4 * 4 * 10^5) == O(2*10^10)
"""


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        A = [[0 for _ in range(n)] for _ in range(m)]
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in guards + walls:
            A[x][y] = 1

        def dfs(x, y, dx, dy):
            if not (0 <= x < m and 0 <= y < n) or A[x][y] == 1:
                return 0
            A[x][y] = 2
            dfs(x + dx, y + dy, dx, dy)

        ans = 0
        for i, j in guards:
            for dx, dy in D:
                dfs(i + dx, j + dy, dx, dy)

        return sum([1 for i in range(m) for j in range(n) if not A[i][j]])
