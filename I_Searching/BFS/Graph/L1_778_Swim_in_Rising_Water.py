""" https://leetcode.com/problems/swim-in-rising-water/
sentinel binary search + bfs
"""


class Solution:
    def swimInWater(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def fn(m):
            Q = [(0, 0)]
            seen = set()
            while Q:
                x, y = Q.pop(0)
                if A[x][y] <= m and (x, y) not in seen:
                    if x == N - 1 and y == N - 1:
                        return True
                    seen.add((x, y))
                    for dx, dy in D:
                        if 0 <= x + dx < N and 0 <= y + dy < N:
                            Q.append((x + dx, y + dy))
            return False

        N = len(A)
        l, r = A[0][0], N * N + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
