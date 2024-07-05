""" https://leetcode.com/problems/escape-the-spreading-fire/
two bfs + binary search:
1. from fires to each cell
2. use binary search to check if we can reach (-1, -1) after t minutes
"""


class Solution:
    def maximumMinutes(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        Q = [(i, j, 0) for i in range(len(A)) for j in range(len(A[0])) if A[i][j] == 1]

        def fire_bfs(Q):
            while Q:
                nextQ = []
                for x, y, t in Q:
                    seen[(x, y)] = t
                    for dx, dy in D:
                        if (
                            0 <= x + dx < len(A)
                            and 0 <= y + dy < len(A[0])
                            and A[x + dx][y + dy] not in [1, 2]
                            and t + 1 < seen[(x + dx, y + dy)]
                        ):
                            nextQ.append((x + dx, y + dy, t + 1))
                Q = nextQ

        def escape_bfs(t):
            Q = [(0, 0, t)]
            while Q:
                nextQ = []
                for x, y, t in Q:
                    if x == len(A) - 1 and y == len(A[0]) - 1:
                        return t <= seen[(x, y)]
                    if seen[(x, y)] <= t:
                        continue

                    for dx, dy in D:
                        if (
                            0 <= x + dx < len(A)
                            and 0 <= y + dy < len(A[0])
                            and A[x + dx][y + dy] not in [1, 2]
                            and (x + dx, y + dy) not in seen2
                        ):
                            seen2[(x + dx, y + dy)] = t + 1
                            nextQ.append((x + dx, y + dy, t + 1))
                Q = nextQ
            return False

        seen = {(i, j): inf for i in range(len(A)) for j in range(len(A[0]))}
        fire_bfs(Q)

        l, r = 0, 10 ** 9 + 1
        while l < r:
            m = (l + r) // 2
            seen2 = defaultdict(int)
            if not escape_bfs(m):
                r = m
            else:
                l = m + 1
        return l - 1
