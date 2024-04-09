""" https://leetcode.com/problems/number-of-closed-islands/
opposite 1020
"""


class Solution:
    def closedIsland(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            Q = [(x, y)]
            ans = True
            while Q:
                x, y = Q.pop(0)
                A[x][y] = 1
                for dx, dy in D:
                    if 0 <= x + dx < len(A) and 0 <= y + \
                            dy < len(A[0]) and A[x + dx][y + dy] == 0:
                        if (x + dx == 0 or x + dx == len(A) - 1 or y +
                                dy == 0 or y + dy == len(A[0]) - 1):
                            ans = False
                        A[x + dx][y + dy] = 1
                        Q.append((x + dx, y + dy))
            return ans

            if not (0 <= x < len(A) and 0 <= y < len(A[0])):
                return False
            elif A[x][y] == 1:
                return True
            A[x][y] = 1
            ans = True
            for dx, dy in D:
                ans &= dfs(x + dx, y + dy)
            return ans

        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if not(
                        not i or not j or i == len(A) -
                        1 or j == len(
                            A[0]) -
                        1) and A[i][j] == 0:
                    if bfs(i, j):
                        ans += 1
        return ans
