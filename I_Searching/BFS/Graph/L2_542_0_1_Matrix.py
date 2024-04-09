""" https://leetcode.com/problems/01-matrix/
BFS by frontier set
"""


class Solution:
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if not A[i][j]:
                    seen.add((i, j))
        Q = seen.copy()
        k = 0
        while Q:
            nxt = set()
            for x, y in Q:
                A[x][y] = k
                for dx, dy in D:
                    if 0 <= x + \
                            dx < len(A) and 0 <= y + dy < len(A[0]) and (x + dx, y + dy) not in seen:
                        nxt.add((x + dx, y + dy))
            Q = nxt
            seen |= nxt
            k += 1
        return A
