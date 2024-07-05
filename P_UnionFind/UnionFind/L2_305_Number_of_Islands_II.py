""" https://leetcode.com/problems/number-of-islands-ii/
union find on 2D graph
"""
from header import *


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        A = list(range(m * n))

        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        ans = []
        island = 0
        G = [[0 for _ in range(n)] for _ in range(m)]
        seen = set()
        for x, y in positions:
            if (x, y) in seen:
                ans.append(island)
                continue

            seen.add((x, y))
            G[x][y] = 1
            island += 1
            for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
                if 0 <= x + dx < m and 0 <= y + dy < n and G[x + dx][y + dy] == 1:
                    a = x * n + y
                    b = (x + dx) * n + (y + dy)
                    if find(a) != find(b):
                        union(a, b)
                        island -= 1
            ans.append(island)
        return ans


"""
3
3
[[0,0],[0,1],[1,2],[2,1]]
1
1
[[0,0]]
2
2
[[0,0],[1,1],[0,1]]
3
3
[[0,0],[0,1],[1,2],[1,2]]
8
4
[[0,0],[7,1],[6,1],[3,3],[4,1]]
"""
