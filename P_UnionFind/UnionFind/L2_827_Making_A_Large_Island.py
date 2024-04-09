""" https://leetcode.com/problems/making-a-large-island/
union find + bfs

1. union find to find all connected components
2. for each 0, bfs to find all connected components and add them up
"""
from header import *


class Solution:
    def largestIsland(self, G: List[List[int]]) -> int:
        n = len(G)
        A = list(range(n * n + 1))

        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        for x in range(n):
            for y in range(n):
                if G[x][y] == 1:
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        if 0 <= x + dx < n and 0 <= y + \
                                dy < n and G[x + dx][y + dy] == 1:
                            union(x * n + y, (x + dx) * n + (y + dy))

        cnt = Counter()
        for i in range(n * n + 1):
            cnt[find(i)] += 1

        ans = 0
        for x in range(n):
            for y in range(n):
                cand = 1
                seen = set()
                if G[x][y] == 1:
                    ans = max(ans, cnt[find(x * n + y)])
                elif G[x][y] == 0:
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        if 0 <= x + dx < n and 0 <= y + \
                                dy < n and G[x + dx][y + dy] == 1:
                            key = find((x + dx) * n + (y + dy))
                            if key not in seen:
                                seen.add(key)
                                cand += cnt[key]
                    ans = max(ans, cand)
        return ans
