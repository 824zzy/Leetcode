""" https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
Solution 1: try to union stones in the same row/column while check if they are in the same group, if not, then answer plus one
Solution 2: dfs to count groups
"""

from header import *


# Solution 1
class Solution:
    def removeStones(self, A: List[List[int]]) -> int:
        p = list(range(len(A)))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p[find(x)] = find(y)

        row, col = defaultdict(list), defaultdict(list)
        ans = 0
        for i, (x, y) in enumerate(A):
            row[x].append(i)
            col[y].append(i)
        for k, v in row.items():
            for i in range(len(v) - 1):
                if find(v[i]) != find(v[i + 1]):
                    union(v[i], v[i + 1])
                    ans += 1

        for k, v in col.items():
            for i in range(len(v) - 1):
                if find(v[i]) != find(v[i + 1]):
                    union(v[i], v[i + 1])
                    ans += 1
        return ans


# Solution 1
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def removeStones(self, A: List[List[int]]) -> int:
        X = []
        for i, j in A:
            X.extend([i, j])
        dsu = DSU(len(X))

        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i][0] == A[j][0] and dsu.find(i) != dsu.find(j):
                    dsu.union(i, j)
                    ans += 1

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i][1] == A[j][1] and dsu.find(i) != dsu.find(j):
                    dsu.union(i, j)
                    ans += 1

        return ans


# Solution 2:
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [tuple(x) for x in stones]
        G = defaultdict(list)

        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                x, y = stones[i]
                xx, yy = stones[j]
                if xx == x or y == yy:
                    G[(x, y)].append((xx, yy))
                    G[(xx, yy)].append((x, y))

        def dfs(x, y):
            for xx, yy in G[(x, y)]:
                if (xx, yy) not in seen:
                    seen.add((xx, yy))
                    dfs(xx, yy)

        seen = set()
        grp = 0
        for i in range(len(stones)):
            if stones[i] not in seen:
                seen.add(stones[i])
                grp += 1
                dfs(*stones[i])
        return len(stones) - grp


"""
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
[[0,0],[0,2],[1,1],[2,0],[2,2]]
[[0,0]]
[[0,1],[1,0],[1,1]]
"""
