""" https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
bit manipulation + bfs/dfs

https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/discuss/446342/JavaPython-3-Convert-matrix-to-int%3A-BFS-and-DFS-codes-w-explanation-comments-and-analysis.

transfer the matrix to int: sum(cell<<(i*n+j) for i, row in enumerate(A) for j, cell in enumerate(row))
flip kth cell by: next ^ 1 << k
"""


class Solution:
    def minFlips(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        D = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        start = sum(
            cell << (i * n + j) for i, row in enumerate(A) for j, cell in enumerate(row)
        )
        Q = [(start, 0)]
        seen = {start: 0}

        while Q:
            cur, step = Q.pop(0)
            if not cur:
                return step
            for x in range(m):
                for y in range(n):
                    nxt = cur
                    for dx, dy in D:
                        if 0 <= x + dx < m and 0 <= y + dy < n:
                            nxt ^= 1 << ((x + dx) * n + (y + dy))
                    if nxt not in seen:
                        seen.add(nxt)
                        Q.append((nxt, step + 1))
        return -1


class Solution:
    def minFlips(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        D = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        start = sum(
            cell << (i * n + j) for i, row in enumerate(A) for j, cell in enumerate(row)
        )
        Q = [(start, 0)]
        seen = {start: 0}
        self.ans = inf

        def dfs(cur, step):
            if not cur:
                self.ans = min(self.ans, step)
                return

            for x in range(m):
                for y in range(n):
                    nxt = cur
                    for dx, dy in D:
                        if 0 <= x + dx < m and 0 <= y + dy < n:
                            nxt ^= 1 << ((x + dx) * n + (y + dy))
                    if seen.get(nxt, inf) > step + 1:
                        seen[nxt] = step + 1
                        dfs(nxt, step + 1)

        dfs(start, 0)
        return self.ans if self.ans != inf else -1
