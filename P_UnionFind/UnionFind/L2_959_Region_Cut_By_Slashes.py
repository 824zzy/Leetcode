# Disjoint Set Union Template
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def merge(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(4 * n * n)
        for r in range(n):
            for c in range(n):
                idx = 4 * (r * n + c)
                if grid[r][c] == '/':
                    dsu.merge(idx + 0, idx + 3)
                    dsu.merge(idx + 1, idx + 2)
                elif grid[r][c] == '\\':
                    dsu.merge(idx + 0, idx + 1)
                    dsu.merge(idx + 2, idx + 3)
                elif grid[r][c] == ' ':
                    dsu.merge(idx + 0, idx + 1)
                    dsu.merge(idx + 1, idx + 2)
                    dsu.merge(idx + 2, idx + 3)
                if r + 1 < n:
                    dsu.merge(idx + 2, idx + 4 * n + 0)
                if c + 1 < n:
                    dsu.merge(idx + 1, idx + 4 + 3)

        return len(set([dsu.find(i) for i in range(len(dsu.p))]))
