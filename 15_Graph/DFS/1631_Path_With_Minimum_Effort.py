""" L2: https://leetcode.com/problems/path-with-minimum-effort/discuss/1035940/Python-dfs-with-binary-search-explained
A comprehensive problem for binary search and dfs
Similar problem: 778. Swim in Rising Water
"""


class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        nr, nc = len(A), len(A[0])
        neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(LIMIT, x, y):
            seen.add((x, y))
            for dx, dy in neibs:
                if 0<=dx+x<nr and 0<=dy+y<nc and (dx+x, dy+y) not in seen:
                    if abs(A[x][y]-A[dx+x][dy+y])<=LIMIT:
                        dfs(LIMIT, dx+x, dy+y)
        
        l, r = -1, max(max(A, key=max))
        while l+1<r:
            m = (l+r)//2
            seen = set()
            dfs(m, 0, 0)
            if (nr-1, nc-1) in seen: r = m
            else: l = m
        return r