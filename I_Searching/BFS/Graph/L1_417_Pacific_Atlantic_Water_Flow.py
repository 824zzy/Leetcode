""" https://leetcode.com/problems/pacific-atlantic-water-flow/
Think reversely, starting from ocean and move in increase way.
1. flood fill pacific
2. flood fill atlantic
3. find valid islands
"""


class Solution:
    def pacificAtlantic(self, A: List[List[int]]) -> List[List[int]]:
        def bfs(ii, jj):
            seen = set()
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if i == ii or j == jj:
                        Q = [(i, j)]
                        seen.add((i, j))
                        while Q:
                            x, y = Q.pop(0)
                            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                                if (
                                    0 <= x + dx < len(A)
                                    and 0 <= y + dy < len(A[0])
                                    and A[x][y] <= A[x + dx][y + dy]
                                    and (x + dx, y + dy) not in seen
                                ):
                                    seen.add((x + dx, y + dy))
                                    Q.append((x + dx, y + dy))
            return seen

        P = bfs(0, 0)
        A = bfs(len(A) - 1, len(A[0]) - 1)
        return P & A
